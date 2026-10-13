#!/usr/bin/env python3
"""Build the v0 candidate pool of approved small-molecule drugs and measure how well a diverse sample covers it.

Run from the repository root:
    uv run --no-project --python 3.12 --with rdkit --with requests --with pandas --with numpy \
        eval/select_benchmark.py

Funnel (docs/research/03-data-and-rag.md, section 2.1), applied in this order:
  F1  approved: ChEMBL max_phase=4, molecule_type=Small molecule, parent records only
  F2  has an INN synonym (syn_type == "INN")
  F3  unambiguous small molecule (RDKit fragment parent; metals, MW > 900, long peptides, isotopes excluded)
      -> the survivors of F1-F3 are the reference population for the coverage report
  F4  US patent/exclusivity status from the FDA Orange Book (informational, SAFE-005); keep off_patent_us
  F6  regulated-substance exclusion, FAIL-CLOSED (SAFE-002): openFDA NDC active ingredients with a DEA
      schedule + 21 CFR 1308.11-1308.15 text (eCFR). If either source fails, the run aborts before writing.
  F5  documentation proxy: Europe PMC hit count for the INN with "synthesis"/"process development"; keep >= 2
  F7  scaffold de-duplication: one representative per generic Bemis-Murcko scaffold (most documented first)
  F8  sample of 40: greedy MaxMin (Morgan r=2, 2048 bits) constrained by class quotas taken from the reference
      shares of the structure-level classes (N-heterocycle, fluorine, >=1 stereocentre); the unconstrained
      MaxMin pick is also computed and reported as a baseline, so the cost of the quota is visible

Outputs (identifiers and computed properties only; no synthesis information of any kind):
  eval/benchmark/candidates_v0.csv   final pool with labels and the selected_in_40 flag
  eval/reports/coverage.json|.md     funnel counts and coverage statistics (EVAL-001)
  eval/reports/exclusions.csv        per-molecule exclusion reasons for F2-F5

Safety: names of substances matched by the F6 gate are never printed, logged or written; only counts. Gate
sources are fetched live on every run and held in memory only (not cached). Molecules matched by the gate are
also omitted from exclusions.csv, whatever stage excluded them. Other raw API responses are cached under
data/cache/ (gitignored, DATA-002); pass --refresh to re-download them.
"""

from __future__ import annotations

import argparse
import csv
import gzip
import hashlib
import html
import io
import json
import math
import platform
import re
import subprocess
import sys
import threading
import time
import uuid
import zipfile
from collections import Counter, defaultdict
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass, field
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any

import numpy as np
import pandas
import requests
from rdkit import Chem, DataStructs, RDLogger, rdBase
from rdkit.Chem import Crippen, Descriptors, rdFingerprintGenerator, rdMolDescriptors
from rdkit.Chem.MolStandardize import rdMolStandardize
from rdkit.Chem.Scaffolds import MurckoScaffold
from rdkit.SimDivFilters.rdSimDivPickers import MaxMinPicker
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

RDLogger.DisableLog("rdApp.*")

ROOT = Path(__file__).resolve().parent.parent
CACHE = ROOT / "data" / "cache"
OUT_CANDIDATES = ROOT / "eval" / "benchmark" / "candidates_v0.csv"
OUT_REPORT_MD = ROOT / "eval" / "reports" / "coverage.md"
OUT_REPORT_JSON = ROOT / "eval" / "reports" / "coverage.json"
OUT_EXCLUSIONS = ROOT / "eval" / "reports" / "exclusions.csv"

RUN_COMMAND = (
    "uv run --no-project --python 3.12 --with rdkit --with requests --with pandas --with numpy "
    "eval/select_benchmark.py"
)
USER_AGENT = "synthroute-select-benchmark/0.1 (academic research; polite client)"

CHEMBL_API = "https://www.ebi.ac.uk/chembl/api/data"
CHEMBL_FIELDS = (
    "molecule_chembl_id,pref_name,first_approval,max_phase,molecule_type,molecule_hierarchy,"
    "molecule_synonyms,molecule_structures,inorganic_flag,polymer_flag"
)
ORANGE_BOOK_ZIP = "https://www.fda.gov/media/76860/download"
ORANGE_BOOK_PAGE = (
    "https://www.fda.gov/drugs/drug-approvals-and-databases/orange-book-data-files"
)
OPENFDA_NDC = "https://api.fda.gov/drug/ndc.json"
ECFR_TITLES = "https://www.ecfr.gov/api/versioner/v1/titles.json"
ECFR_FULL = "https://www.ecfr.gov/api/versioner/v1/full/{date}/title-21.xml"
CFR_SCHEDULE_SECTIONS = ("1308.11", "1308.12", "1308.13", "1308.14", "1308.15")
EPMC_SEARCH = "https://www.ebi.ac.uk/europepmc/webservices/rest/search"

SEED = 42
N_BOOT = 1000
SAMPLE_SIZE = 40
EPMC_MIN_HITS = 2
EPMC_MAX_RPS = 4.0  # stay under the 5 requests/s politeness ceiling
MW_MAX = 900.0
PEPTIDE_MIN_AMIDES = 8
COVERAGE_TOLERANCE = (
    0.10  # +-10 percentage points (docs/research/03-data-and-rag.md, section 2.2)
)
# F8 quota window around the reference share: half the coverage tolerance, so a sample that satisfies the
# quota lands inside the +-10 pp band with room to spare.
QUOTA_TOLERANCE = 0.05
EMPTY_CELL_MIN_SHARE = 0.05  # reference share >= 5% with zero in the sample is a blocking defect (section 3.2)

# Synonym types that are drug names (not trade names, research codes or systematic names).
NAME_SYN_TYPES = frozenset(
    {
        "INN",
        "USAN",
        "BAN",
        "JAN",
        "USP",
        "FDA",
        "ATC",
        "MERCK_INDEX",
        "BNF",
        "DCF",
        "NATIONAL_FORMULARY",
    }
)
# Counter-ions, hydrates and salt qualifiers removed when matching names across sources.
SALT_WORDS = frozenset(
    """
    HYDROCHLORIDE DIHYDROCHLORIDE TRIHYDROCHLORIDE HCL HYDROBROMIDE HYDROIODIDE HYDROGEN DIHYDROGEN
    SULFATE SULPHATE BISULFATE HEMISULFATE PHOSPHATE DIPHOSPHATE MONOBASIC DIBASIC MALEATE DIMALEATE
    FUMARATE HEMIFUMARATE MESYLATE DIMESYLATE MESILATE METHANESULFONATE CITRATE BROMIDE CHLORIDE IODIDE
    TARTRATE BITARTRATE HEMITARTRATE SUCCINATE LACTATE BESYLATE BESILATE TOSYLATE TOSILATE SODIUM DISODIUM
    TRISODIUM MONOSODIUM POTASSIUM DIPOTASSIUM CALCIUM MAGNESIUM ZINC MEGLUMINE DIMEGLUMINE TROMETHAMINE
    LYSINE ARGININE OLAMINE DIOLAMINE ERBUMINE GLUCONATE NITRATE MALATE NAPSYLATE ADIPATE PAMOATE EMBONATE
    XINAFOATE HYCLATE EDISYLATE ESYLATE CAMSYLATE ISETHIONATE OXALATE SACCHARATE ASPARTATE STEARATE ESTOLATE
    CARBONATE BICARBONATE ACETATE MONOHYDRATE DIHYDRATE TRIHYDRATE HEMIHYDRATE SESQUIHYDRATE PENTAHYDRATE
    HEPTAHYDRATE HYDRATE ANHYDROUS
    """.split()
)
# Extra ester words stripped only by the F6 gate: wider matching is the conservative direction there.
GATE_EXTRA_WORDS = frozenset(
    """
    PROPIONATE DIPROPIONATE PHENPROPIONATE CYPIONATE ENANTHATE DECANOATE UNDECANOATE UNDECYLENATE VALERATE
    BUTYRATE ISOBUTYRATE BENZOATE PALMITATE HEXANOATE CAPROATE LAURATE DIACETATE TRIACETATE
    """.split()
)
# Elements accepted in an organic small molecule; anything else is treated as a metal/metalloid (F3).
ORGANIC_ELEMENTS = frozenset(
    {1, 5, 6, 7, 8, 9, 14, 15, 16, 17, 34, 35, 53}
)  # H B C N O F Si P S Cl Se Br I
PEPTIDE_BOND = Chem.MolFromSmarts("[NX3][CX4][CX3](=[OX1])[NX3][CX4]")
FRAGMENT_REMOVER = rdMolStandardize.FragmentRemover()  # RDKit default salt/solvent list

RUN_ID = uuid.uuid4().hex[:12]


# --------------------------------------------------------------------------------------------- logging + HTTP


def log(event: str, **fields: Any) -> None:
    """Structured JSON log line on stderr (PY-007). Never pass names of gate-matched substances here."""
    record = {
        "ts": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "run_id": RUN_ID,
        "event": event,
    }
    record.update(fields)
    print(
        json.dumps(record, ensure_ascii=False, default=str), file=sys.stderr, flush=True
    )


class RateLimiter:
    """Thread-safe minimum interval between requests (process-level, so a module-level instance is fine)."""

    def __init__(self, max_per_second: float) -> None:
        self._interval = 1.0 / max_per_second
        self._lock = threading.Lock()
        self._next = 0.0

    def wait(self) -> None:
        with self._lock:
            now = time.monotonic()
            delay = self._next - now
            self._next = max(now, self._next) + self._interval
        if delay > 0:
            time.sleep(delay)


def make_session() -> requests.Session:
    retry = Retry(
        total=5,
        connect=5,
        read=5,
        backoff_factor=1.5,
        status_forcelist=(429, 500, 502, 503, 504),
        allowed_methods=frozenset({"GET"}),
        respect_retry_after_header=True,
        raise_on_status=False,
    )
    session = requests.Session()
    adapter = HTTPAdapter(max_retries=retry, pool_maxsize=8)
    session.mount("https://", adapter)
    session.headers.update(
        {"User-Agent": USER_AGENT, "Accept-Encoding": "gzip, deflate"}
    )
    return session


def read_gz_json(path: Path) -> Any:
    with gzip.open(path, "rt", encoding="utf-8") as fh:
        return json.load(fh)


def write_gz_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(path.name + ".tmp")
    with gzip.open(tmp, "wt", encoding="utf-8") as fh:
        json.dump(data, fh)
    tmp.replace(path)


def cached_get_json(
    session: requests.Session,
    url: str,
    params: dict[str, Any],
    cache_file: Path,
    *,
    refresh: bool,
    limiter: RateLimiter | None = None,
    timeout: tuple[float, float] = (10.0, 120.0),
) -> Any:
    if cache_file.exists() and not refresh:
        return read_gz_json(cache_file)
    if limiter is not None:
        limiter.wait()
    response = session.get(url, params=params, timeout=timeout)
    response.raise_for_status()
    data = response.json()
    write_gz_json(cache_file, data)
    return data


# --------------------------------------------------------------------------------------------- names


_NON_ALNUM = re.compile(r"[^A-Z0-9]+")


def norm_name(name: str) -> str:
    return _NON_ALNUM.sub(" ", name.upper()).strip()


def strip_words(normalized: str, words: frozenset[str]) -> str:
    kept = [tok for tok in normalized.split() if tok not in words]
    return " ".join(kept) if kept else normalized


def gate_keys(names: list[str]) -> set[str]:
    keys: set[str] = set()
    for name in names:
        n = norm_name(name)
        if not n:
            continue
        keys.add(n)
        keys.add(strip_words(n, SALT_WORDS))
        keys.add(strip_words(n, SALT_WORDS | GATE_EXTRA_WORDS))
    keys.discard("")
    return keys


# --------------------------------------------------------------------------------------------- molecules


@dataclass
class Molecule:
    chembl_id: str
    pref_name: str | None
    first_approval: int | None
    inn: str | None
    names: list[str]
    smiles: str | None
    inorganic_flag: bool
    polymer_flag: bool
    mol: Chem.Mol | None = None
    inchikey: str | None = None
    labels: dict[str, Any] = field(default_factory=dict)
    patent_status: str | None = None
    patent_status_all_products: str | None = None
    substance_patent_active: bool = False
    gate_hits: tuple[bool, bool] = (
        False,
        False,
    )  # (openFDA NDC, 21 CFR 1308); never serialised
    epmc_hits: int | None = None
    scaffold_smiles: str | None = None
    scaffold_id: str | None = None
    selected: bool = False

    @property
    def display_name(self) -> str:
        return self.inn or (self.pref_name or "").lower()

    @property
    def sort_key(self) -> tuple[int, str]:
        digits = re.sub(r"\D", "", self.chembl_id)
        return (int(digits) if digits else 0, self.chembl_id)


def pick_inn(record: dict[str, Any]) -> str | None:
    inns = sorted(
        {
            s["molecule_synonym"].strip()
            for s in record.get("molecule_synonyms") or []
            if s.get("syn_type") == "INN" and s.get("molecule_synonym")
        },
        key=lambda s: (len(s), s.lower()),
    )
    if not inns:
        return None
    pref = (record.get("pref_name") or "").upper()
    for inn in inns:
        if inn.upper() == pref:
            return inn.lower()
    return inns[0].lower()


def to_molecule(record: dict[str, Any]) -> Molecule:
    names = [record["pref_name"]] if record.get("pref_name") else []
    for syn in record.get("molecule_synonyms") or []:
        if syn.get("syn_type") in NAME_SYN_TYPES and syn.get("molecule_synonym"):
            names.append(syn["molecule_synonym"])
    structures = record.get("molecule_structures") or {}
    approval = record.get("first_approval")
    return Molecule(
        chembl_id=record["molecule_chembl_id"],
        pref_name=record.get("pref_name"),
        first_approval=int(approval) if approval else None,
        inn=pick_inn(record),
        names=sorted(set(names)),
        smiles=structures.get("canonical_smiles"),
        inorganic_flag=bool(record.get("inorganic_flag") == 1),
        polymer_flag=bool(record.get("polymer_flag")),
    )


def standardize(m: Molecule) -> str | None:
    """Apply F3. Sets m.mol (largest-fragment parent) and m.inchikey; returns an exclusion reason or None."""
    try:
        return _standardize(m)
    except Exception as exc:  # noqa: BLE001 - RDKit sanitisation errors become an explicit F3 reason
        m.mol = None
        return f"rdkit_error_{type(exc).__name__}"


def _standardize(m: Molecule) -> str | None:
    if not m.smiles:
        return "no_structure"
    mol = Chem.MolFromSmiles(m.smiles)
    if mol is None:
        return "smiles_parse_error"
    if m.polymer_flag:
        return "chembl_polymer_flag"
    if m.inorganic_flag:
        return "chembl_inorganic_flag"
    if any(atom.GetIsotope() for atom in mol.GetAtoms()):
        return "isotope_labelled"
    if any(atom.GetAtomicNum() not in ORGANIC_ELEMENTS for atom in mol.GetAtoms()):
        return "metal_or_metalloid"
    if not any(atom.GetAtomicNum() == 6 for atom in mol.GetAtoms()):
        return "no_carbon"
    desalted = FRAGMENT_REMOVER.remove(mol)
    if len(Chem.GetMolFrags(desalted)) > 1:
        return "multi_component"
    parent = rdMolStandardize.FragmentParent(mol)
    if Descriptors.MolWt(parent) > MW_MAX:
        return "mw_gt_900"
    amide_bonds = {
        (match[2], match[4])
        for match in parent.GetSubstructMatches(PEPTIDE_BOND, uniquify=False)
    }
    if len(amide_bonds) >= PEPTIDE_MIN_AMIDES:
        return "peptide_ge_8_amide_bonds"
    inchikey = Chem.MolToInchiKey(parent)
    if not inchikey:
        return "no_inchikey"
    m.mol = parent
    m.inchikey = inchikey
    m.labels = compute_labels(parent)
    return None


def count_ring_systems(mol: Chem.Mol) -> int:
    systems: list[set[int]] = []
    for ring in mol.GetRingInfo().AtomRings():
        merged = set(ring)
        rest = []
        for system in systems:
            if system & merged:
                merged |= system
            else:
                rest.append(system)
        systems = rest + [merged]
    return len(systems)


def compute_labels(mol: Chem.Mol) -> dict[str, Any]:
    rings = mol.GetRingInfo().AtomRings()
    has_n_heterocycle = any(
        any(mol.GetAtomWithIdx(i).GetAtomicNum() == 7 for i in ring) for ring in rings
    )
    n_stereo = len(Chem.FindMolChiralCenters(mol, includeUnassigned=True))
    return {
        "n_heterocycle": has_n_heterocycle,
        "has_F": any(atom.GetAtomicNum() == 9 for atom in mol.GetAtoms()),
        "n_stereo": n_stereo,
        "chiral": n_stereo >= 1,
        "n_ring_systems": count_ring_systems(mol),
        "mw": Descriptors.MolWt(mol),
        "clogp": Crippen.MolLogP(mol),
        "hbd": rdMolDescriptors.CalcNumHBD(mol),
        "hba": rdMolDescriptors.CalcNumHBA(mol),
        "tpsa": rdMolDescriptors.CalcTPSA(mol),
        "fsp3": rdMolDescriptors.CalcFractionCSP3(mol),
        "n_heavy_atoms": mol.GetNumHeavyAtoms(),
    }


def generic_scaffold(mol: Chem.Mol) -> str:
    core = MurckoScaffold.GetScaffoldForMol(mol)
    if core.GetNumAtoms() == 0:
        return ""
    return Chem.MolToSmiles(MurckoScaffold.MakeScaffoldGeneric(core))


# --------------------------------------------------------------------------------------------- sources


def fetch_chembl(
    session: requests.Session, refresh: bool
) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    status = cached_get_json(
        session,
        f"{CHEMBL_API}/status.json",
        {},
        CACHE / "chembl" / "status.json.gz",
        refresh=refresh,
    )
    records: list[dict[str, Any]] = []
    offset, total = 0, None
    limiter = RateLimiter(1.0)
    while total is None or offset < total:
        params = {
            "max_phase": 4,
            "molecule_type": "Small molecule",
            "limit": 1000,
            "offset": offset,
            "only": CHEMBL_FIELDS,
        }
        page = cached_get_json(
            session,
            f"{CHEMBL_API}/molecule.json",
            params,
            CACHE / "chembl" / f"molecule_phase4_small_{offset:05d}.json.gz",
            refresh=refresh,
            limiter=limiter,
            timeout=(10.0, 300.0),
        )
        total = int(page["page_meta"]["total_count"])
        records.extend(page["molecules"])
        log("chembl_page", offset=offset, n=len(page["molecules"]), total=total)
        if not page["molecules"]:
            break
        offset += len(page["molecules"])
    if len(records) != total:
        raise RuntimeError(f"ChEMBL returned {len(records)} records, expected {total}")
    meta = {
        "release": status.get("chembl_db_version"),
        "release_date": status.get("chembl_release_date"),
        "api": f"{CHEMBL_API}/molecule.json",
        "query": "max_phase=4&molecule_type=Small molecule",
        "n_records": total,
    }
    return records, meta


def fetch_orange_book(
    session: requests.Session, refresh: bool
) -> tuple[bytes, dict[str, Any]]:
    folder = CACHE / "orange_book"
    zip_path, meta_path = folder / "orange_book.zip", folder / "meta.json"
    if zip_path.exists() and meta_path.exists() and not refresh:
        return zip_path.read_bytes(), json.loads(meta_path.read_text(encoding="utf-8"))
    url = ORANGE_BOOK_ZIP
    response = session.get(url, timeout=(10.0, 300.0))
    if response.status_code != 200 or not response.content.startswith(b"PK"):
        log("orange_book_direct_link_failed", status=response.status_code)
        page = session.get(ORANGE_BOOK_PAGE, timeout=(10.0, 60.0))
        page.raise_for_status()
        found = re.search(
            r'href="(/media/\d+/download[^"]*)"[^>]*title="Orange Book Data Files compressed"',
            page.text,
        )
        if not found:
            raise RuntimeError("Orange Book ZIP link not found on the data files page")
        url = "https://www.fda.gov" + html.unescape(found.group(1))
        response = session.get(url, timeout=(10.0, 300.0))
        response.raise_for_status()
        if not response.content.startswith(b"PK"):
            raise RuntimeError("Orange Book download is not a ZIP archive")
    disposition = response.headers.get("content-disposition", "")
    name = re.search(r'filename="?([^";]+)"?', disposition)
    meta = {
        "url": url,
        "filename": name.group(1) if name else None,
        "retrieved_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "sha256": hashlib.sha256(response.content).hexdigest(),
        "bytes": len(response.content),
    }
    folder.mkdir(parents=True, exist_ok=True)
    zip_path.write_bytes(response.content)
    meta_path.write_text(json.dumps(meta, indent=2), encoding="utf-8")
    return response.content, meta


def read_tilde_table(archive: zipfile.ZipFile, member: str) -> list[dict[str, str]]:
    names = {n.lower(): n for n in archive.namelist()}
    if member not in names:
        raise RuntimeError(f"Orange Book archive has no {member}")
    text = archive.read(names[member]).decode("latin-1")
    return list(csv.DictReader(io.StringIO(text), delimiter="~"))


def parse_ob_date(text: str) -> date | None:
    try:
        return datetime.strptime(text.strip(), "%b %d, %Y").date()
    except ValueError:
        return None


@dataclass
class OrangeBook:
    full_index: dict[str, set[tuple[tuple[str, str, str], bool]]]
    stripped_index: dict[str, set[tuple[tuple[str, str, str], bool]]]
    active: set[tuple[str, str, str]]
    active_substance_patent: set[tuple[str, str, str]]
    stats: dict[str, Any]


def build_orange_book(blob: bytes, as_of: date) -> OrangeBook:
    archive = zipfile.ZipFile(io.BytesIO(blob))
    products = read_tilde_table(archive, "products.txt")
    patents = read_tilde_table(archive, "patent.txt")
    exclusivity = read_tilde_table(archive, "exclusivity.txt")
    full_index: dict[str, set] = defaultdict(set)
    stripped_index: dict[str, set] = defaultdict(set)
    for row in products:
        components = [
            c.strip() for c in (row.get("Ingredient") or "").split(";") if c.strip()
        ]
        key = (
            row["Appl_Type"].strip(),
            row["Appl_No"].strip(),
            row["Product_No"].strip(),
        )
        single = len(components) == 1
        for component in components:
            n = norm_name(component)
            full_index[n].add((key, single))
            stripped_index[strip_words(n, SALT_WORDS)].add((key, single))
    active: set = set()
    active_substance: set = set()
    unparsed = 0
    for row in patents:
        key = (
            row["Appl_Type"].strip(),
            row["Appl_No"].strip(),
            row["Product_No"].strip(),
        )
        expiry = parse_ob_date(row.get("Patent_Expire_Date_Text") or "")
        if expiry is None:
            unparsed += 1
        if (
            expiry is None or expiry > as_of
        ):  # unparseable dates count as active (conservative)
            active.add(key)
            if (row.get("Drug_Substance_Flag") or "").strip().upper() == "Y":
                active_substance.add(key)
    for row in exclusivity:
        key = (
            row["Appl_Type"].strip(),
            row["Appl_No"].strip(),
            row["Product_No"].strip(),
        )
        expiry = parse_ob_date(row.get("Exclusivity_Date") or "")
        if expiry is None:
            unparsed += 1
        if expiry is None or expiry > as_of:
            active.add(key)
    stats = {
        "n_products": len(products),
        "n_patent_rows": len(patents),
        "n_exclusivity_rows": len(exclusivity),
        "n_products_with_active_patent_or_exclusivity": len(active),
        "n_unparsed_dates": unparsed,
    }
    return OrangeBook(full_index, stripped_index, active, active_substance, stats)


def patent_status(m: Molecule, ob: OrangeBook, scope: str) -> None:
    normalized = {norm_name(n) for n in m.names if norm_name(n)}
    hits: set = set()
    for n in normalized:
        hits |= ob.full_index.get(n, set())
    if not hits:  # fall back to salt-stripped names on both sides
        for n in normalized:
            hits |= ob.stripped_index.get(strip_words(n, SALT_WORDS), set())
    if not hits:
        m.patent_status = m.patent_status_all_products = "unknown"
        return
    all_keys = {key for key, _ in hits}
    single_keys = {key for key, single in hits if single}
    scoped = single_keys if (scope == "single-first" and single_keys) else all_keys
    m.patent_status = "protected" if scoped & ob.active else "off_patent_us"
    m.patent_status_all_products = (
        "protected" if all_keys & ob.active else "off_patent_us"
    )
    m.substance_patent_active = bool(scoped & ob.active_substance_patent)


@dataclass
class Gate:
    """F6 regulated-substance gate. Holds name keys in memory only; never serialised or logged."""

    openfda_keys: frozenset[str]
    cfr_ngrams: frozenset[str]
    meta: dict[str, Any]

    def match(self, m: Molecule) -> tuple[bool, bool]:
        keys = gate_keys(m.names + ([m.inn] if m.inn else []))
        openfda_hit = bool(keys & self.openfda_keys)
        cfr_hit = any(len(k) >= 4 and k in self.cfr_ngrams for k in keys)
        return openfda_hit, cfr_hit


def load_gate(session: requests.Session) -> Gate:
    """Fetch both gate sources live. Any failure or implausible result aborts the run (fail-closed, SAFE-002)."""
    try:
        params = {
            "search": "_exists_:dea_schedule",
            "count": "active_ingredients.name.exact",
            "limit": 1000,
        }
        response = session.get(OPENFDA_NDC, params=params, timeout=(10.0, 120.0))
        response.raise_for_status()
        payload = response.json()
        terms = [r["term"] for r in payload.get("results", []) if r.get("term")]
        if len(terms) < 50:
            raise RuntimeError(
                f"openFDA returned an implausibly short list ({len(terms)} terms)"
            )
        if len(terms) >= params["limit"]:
            raise RuntimeError(
                "openFDA count result may be truncated (count queries cannot be paged)"
            )
        openfda_keys = frozenset(gate_keys(terms))

        titles = session.get(ECFR_TITLES, timeout=(10.0, 60.0))
        titles.raise_for_status()
        title21 = next(t for t in titles.json()["titles"] if t["number"] == 21)
        cfr_date = title21["up_to_date_as_of"]
        texts = []
        for section in CFR_SCHEDULE_SECTIONS:
            r = session.get(
                ECFR_FULL.format(date=cfr_date),
                params={"part": "1308", "section": section},
                timeout=(10.0, 120.0),
            )
            r.raise_for_status()
            texts.append(html.unescape(re.sub(r"<[^>]+>", " ", r.text)))
        words = norm_name(" ".join(texts)).split()
        if len(words) < 3000:
            raise RuntimeError(
                f"eCFR schedules text is implausibly short ({len(words)} words)"
            )
        ngrams = {
            " ".join(words[i : i + k])
            for k in range(1, 9)
            for i in range(len(words) - k + 1)
        }
    except Exception as exc:  # noqa: BLE001 - any failure must close the gate
        log(
            "f6_gate_unavailable_abort",
            error_type=type(exc).__name__,
            error=str(exc)[:300],
        )
        raise SystemExit(
            "F6 gate source unavailable: aborting without writing any output (fail-closed, SAFE-002)"
        )
    meta = {
        "openfda_ndc": {
            "query": "search=_exists_:dea_schedule&count=active_ingredients.name.exact&limit=1000",
            "last_updated": payload.get("meta", {}).get("last_updated"),
            "n_terms": len(terms),
            "sha256_sorted_terms": hashlib.sha256(
                "\n".join(sorted(terms)).encode()
            ).hexdigest(),
        },
        "ecfr_21_cfr_1308": {
            "sections": list(CFR_SCHEDULE_SECTIONS),
            "up_to_date_as_of": cfr_date,
            "n_words": len(words),
            "sha256_text": hashlib.sha256(" ".join(words).encode()).hexdigest(),
        },
        "retrieved_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "cached": False,
    }
    log(
        "f6_gate_loaded",
        openfda_terms=len(terms),
        cfr_words=len(words),
        cfr_date=cfr_date,
    )
    return Gate(openfda_keys, frozenset(ngrams), meta)


def epmc_query(inn: str) -> str:
    term = inn.replace('"', "")
    return f'TITLE_ABS:"{term}" AND (TITLE_ABS:"synthesis" OR TITLE_ABS:"process development")'


def fetch_epmc_hits(
    session: requests.Session, molecules: list[Molecule], refresh: bool
) -> int:
    limiter = RateLimiter(EPMC_MAX_RPS)
    errors = 0
    lock = threading.Lock()

    def one(m: Molecule) -> None:
        nonlocal errors
        query = epmc_query(m.inn or "")
        cache_file = (
            CACHE / "epmc" / (hashlib.sha1(query.encode()).hexdigest() + ".json.gz")
        )
        params = {
            "query": query,
            "format": "json",
            "pageSize": 1,
            "resultType": "idlist",
        }
        try:
            data = cached_get_json(
                session,
                EPMC_SEARCH,
                params,
                cache_file,
                refresh=refresh,
                limiter=limiter,
                timeout=(10.0, 60.0),
            )
            m.epmc_hits = int(data["hitCount"])
        except Exception as exc:  # noqa: BLE001 - recorded per molecule, the molecule leaves the pool
            with lock:
                errors += 1
            log("epmc_error", chembl_id=m.chembl_id, error_type=type(exc).__name__)

    with ThreadPoolExecutor(max_workers=4) as pool:
        list(pool.map(one, molecules))
    return errors


# --------------------------------------------------------------------------------------------- statistics


def bootstrap_ci(
    values: np.ndarray, seed: int = SEED, n_boot: int = N_BOOT
) -> tuple[float, float]:
    rng = np.random.default_rng(seed)
    idx = rng.integers(0, len(values), size=(n_boot, len(values)))
    means = values[idx].mean(axis=1)
    return float(np.percentile(means, 2.5)), float(np.percentile(means, 97.5))


def ks_statistic(a: np.ndarray, b: np.ndarray) -> float:
    a, b = np.sort(a), np.sort(b)
    grid = np.concatenate([a, b])
    cdf_a = np.searchsorted(a, grid, side="right") / len(a)
    cdf_b = np.searchsorted(b, grid, side="right") / len(b)
    return float(np.max(np.abs(cdf_a - cdf_b)))


def ks_pvalue_asymptotic(d: float, n: int, m: int) -> float:
    """Two-sample KS p-value, asymptotic Kolmogorov distribution with the Stephens small-sample correction."""
    en = math.sqrt(n * m / (n + m))
    lam = (en + 0.12 + 0.11 / en) * d
    if lam < 0.27:
        return 1.0
    total = sum(
        2 * (-1) ** (j - 1) * math.exp(-2 * j * j * lam * lam) for j in range(1, 101)
    )
    return float(min(1.0, max(0.0, total)))


def wasserstein(a: np.ndarray, b: np.ndarray) -> float:
    a, b = np.sort(a), np.sort(b)
    grid = np.sort(np.concatenate([a, b]))
    deltas = np.diff(grid)
    cdf_a = np.searchsorted(a, grid[:-1], side="right") / len(a)
    cdf_b = np.searchsorted(b, grid[:-1], side="right") / len(b)
    return float(np.sum(np.abs(cdf_a - cdf_b) * deltas))


SHARE_CLASSES = (
    (
        "n_heterocycle",
        "N-гетероцикл",
        "≈59% малых молекул, одобренных FDA (doi:10.1021/jm501100b)",
    ),
    ("has_F", "атом F", "≈20% коммерческих препаратов (doi:10.1021/acsomega.0c00830)"),
    ("chiral", "≥1 стереоцентр", "—"),
)
CONTINUOUS = (
    ("mw", "MW, Да"),
    ("clogp", "cLogP"),
    ("tpsa", "TPSA, Å²"),
    ("fsp3", "Fsp3"),
    ("hbd", "HBD"),
    ("hba", "HBA"),
    ("n_ring_systems", "кольцевые системы"),
)


def share_row(key: str, groups: dict[str, list[Molecule]]) -> dict[str, Any]:
    row: dict[str, Any] = {"label": key}
    for gname, members in groups.items():
        values = np.array([1.0 if m.labels[key] else 0.0 for m in members])
        lo, hi = bootstrap_ci(values)
        row[gname] = {"n": len(values), "share": float(values.mean()), "ci95": [lo, hi]}
    ref = row["reference"]
    for gname in [g for g in ("pool", "sample", "sample_unquoted") if g in row]:
        share = row[gname]["share"]
        within_ci = ref["ci95"][0] <= share <= ref["ci95"][1]
        within_tol = abs(share - ref["share"]) <= COVERAGE_TOLERANCE + 1e-12
        blocking = ref["share"] >= EMPTY_CELL_MIN_SHARE and share == 0.0
        row[gname]["delta_pp"] = 100.0 * (share - ref["share"])
        row[gname]["status"] = (
            "covered" if (within_ci or within_tol) and not blocking else "gap"
        )
        row[gname]["blocking_empty_cell"] = blocking
    return row


def continuous_row(key: str, groups: dict[str, list[Molecule]]) -> dict[str, Any]:
    arrays = {
        g: np.array([float(m.labels[key]) for m in ms]) for g, ms in groups.items()
    }
    row: dict[str, Any] = {
        "label": key,
        "mean": {g: float(a.mean()) for g, a in arrays.items()},
        "median": {g: float(np.median(a)) for g, a in arrays.items()},
    }
    for gname in [g for g in ("pool", "sample", "sample_unquoted") if g in arrays]:
        d = ks_statistic(arrays[gname], arrays["reference"])
        row[f"{gname}_vs_reference"] = {
            "ks": d,
            "ks_p_asymptotic": ks_pvalue_asymptotic(
                d, len(arrays[gname]), len(arrays["reference"])
            ),
            "wasserstein": wasserstein(arrays[gname], arrays["reference"]),
        }
    return row


# --------------------------------------------------------------------------------------------- selection


@dataclass
class Quota:
    """How many positions of the sample a structure-level class must and may take (F8)."""

    key: str
    title: str
    reference_share: float
    target: int
    lo: int  # window from the reference share: ceil((share - QUOTA_TOLERANCE) * n)
    hi: int
    lo_effective: int  # window after checking how many candidates F7 actually left
    hi_effective: int
    available: int
    complement_available: int

    @property
    def feasible(self) -> bool:
        return self.lo_effective == self.lo and self.hi_effective == self.hi

    def as_dict(self, selected: int, n: int) -> dict[str, Any]:
        return {
            "class": self.key,
            "reference_share": self.reference_share,
            "target": self.target,
            "window": [self.lo, self.hi],
            "window_effective": [self.lo_effective, self.hi_effective],
            "available_after_f7": self.available,
            "selected": selected,
            "share": (selected / n) if n else None,
            "satisfied": self.lo_effective <= selected <= self.hi_effective,
            "feasible": self.feasible,
        }


def plan_quotas(
    reference: list[Molecule], candidates: list[Molecule], n: int
) -> list[Quota]:
    """Turn the reference shares of the structure-level classes into per-class windows for a sample of n."""
    plans = []
    for key, title, _ in SHARE_CLASSES:
        share = float(np.mean([1.0 if m.labels[key] else 0.0 for m in reference]))
        lo = max(0, math.ceil((share - QUOTA_TOLERANCE) * n - 1e-9))
        hi = min(n, math.floor((share + QUOTA_TOLERANCE) * n + 1e-9))
        available = sum(1 for m in candidates if m.labels[key])
        complement = len(candidates) - available
        lo_effective = min(lo, available)
        plans.append(
            Quota(
                key=key,
                title=title,
                reference_share=share,
                target=int(round(share * n)),
                lo=lo,
                hi=hi,
                lo_effective=lo_effective,
                hi_effective=max(hi, n - complement, lo_effective),
                available=available,
                complement_available=complement,
            )
        )
    return plans


def tanimoto_distances(fps: list[Any]) -> list[float]:
    """Every pairwise Tanimoto distance inside a set of fingerprints."""
    return [
        1.0 - s
        for i in range(len(fps))
        for s in DataStructs.BulkTanimotoSimilarity(fps[i], fps[i + 1 :])
    ]


def select_with_quotas(
    candidates: list[Molecule], fps: list[Any], quotas: list[Quota], n: int
) -> tuple[list[int], dict[str, int], list[dict[str, Any]]]:
    """Greedy MaxMin selection under class quotas (F8).

    Phase A fills the lower bound of every quota, rarest class first; phase B spends the remaining positions on
    diversity alone. Upper bounds hold in both phases. Each step takes the candidate farthest from everything
    already taken (MaxMin); ties go to the better documented molecule, then to the lower ChEMBL id. There is no
    random start, so the result depends only on the inputs.
    """
    chosen: list[int] = []
    counts = {q.key: 0 for q in quotas}
    nearest = [1.0] * len(candidates)  # distance to the closest already chosen molecule
    taken = [False] * len(candidates)
    trace: list[dict[str, Any]] = []

    def allowed(i: int) -> bool:
        labels = candidates[i].labels
        return not taken[i] and all(
            not labels[q.key] or counts[q.key] < q.hi_effective for q in quotas
        )

    def rank(i: int) -> tuple[float, int, tuple[int, str]]:
        m = candidates[i]
        return (-nearest[i], -(m.epmc_hits or 0), m.sort_key)

    def take(i: int, reason: str) -> None:
        taken[i] = True
        chosen.append(i)
        for q in quotas:
            if candidates[i].labels[q.key]:
                counts[q.key] += 1
        for j, sim in enumerate(DataStructs.BulkTanimotoSimilarity(fps[i], fps)):
            nearest[j] = min(nearest[j], 1.0 - sim)
        trace.append({"chembl_id": candidates[i].chembl_id, "picked_for": reason})

    for q in sorted(quotas, key=lambda x: (x.available, x.key)):
        while counts[q.key] < q.lo_effective and len(chosen) < n:
            options = [
                i
                for i in range(len(candidates))
                if allowed(i) and candidates[i].labels[q.key]
            ]
            if not options:
                log(
                    "f8_quota_stuck",
                    quota=q.key,
                    have=counts[q.key],
                    want=q.lo_effective,
                )
                break
            take(min(options, key=rank), f"quota:{q.key}")
    while len(chosen) < n:
        options = [i for i in range(len(candidates)) if allowed(i)]
        if not options:
            log("f8_short_pool", wanted=n, got=len(chosen))
            break
        take(min(options, key=rank), "diversity")
    return chosen, counts, trace


# --------------------------------------------------------------------------------------------- outputs


def git_sha() -> str:
    try:
        sha = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=True,
        )
        dirty = subprocess.run(
            ["git", "status", "--porcelain", "--", "eval/"],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=True,
        )
        return sha.stdout.strip() + (
            "+uncommitted-eval" if dirty.stdout.strip() else ""
        )
    except (OSError, subprocess.CalledProcessError):
        return "unknown"


def fmt_share(cell: dict[str, Any]) -> str:
    lo, hi = cell["ci95"]
    return (
        f"{100 * cell['share']:.1f}% [{100 * lo:.1f}; {100 * hi:.1f}] (n={cell['n']})"
    )


def write_candidates(pool: list[Molecule]) -> None:
    OUT_CANDIDATES.parent.mkdir(parents=True, exist_ok=True)
    columns = [
        "chembl_id",
        "inn",
        "first_approval",
        "patent_status",
        "epmc_hits",
        "n_heterocycle",
        "has_F",
        "n_stereo",
        "mw",
        "clogp",
        "tpsa",
        "fsp3",
        "scaffold_id",
        "selected_in_40",
        "ru_list_check",
        "hbd",
        "hba",
        "n_ring_systems",
        "n_heavy_atoms",
        "inchikey",
    ]
    with OUT_CANDIDATES.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.writer(fh, lineterminator="\n")
        writer.writerow(columns)
        for m in pool:
            lab = m.labels
            writer.writerow(
                [
                    m.chembl_id,
                    m.inn,
                    m.first_approval if m.first_approval else "",
                    m.patent_status,
                    m.epmc_hits,
                    str(lab["n_heterocycle"]).lower(),
                    str(lab["has_F"]).lower(),
                    lab["n_stereo"],
                    f"{lab['mw']:.2f}",
                    f"{lab['clogp']:.2f}",
                    f"{lab['tpsa']:.2f}",
                    f"{lab['fsp3']:.3f}",
                    m.scaffold_id,
                    str(m.selected).lower(),
                    "pending_manual",
                    lab["hbd"],
                    lab["hba"],
                    lab["n_ring_systems"],
                    lab["n_heavy_atoms"],
                    m.inchikey,
                ]
            )


def write_exclusions(rows: list[tuple[str, str, str, str]]) -> None:
    OUT_EXCLUSIONS.parent.mkdir(parents=True, exist_ok=True)
    with OUT_EXCLUSIONS.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.writer(fh, lineterminator="\n")
        writer.writerow(["chembl_id", "name", "stage", "reason"])
        writer.writerows(rows)


LIMITATIONS = """\
1. **F5 — прокси, а не критерий.** Критерий воронки из `docs/research/03-data-and-rag.md` («не менее двух
   независимых открытых источников с восстановимыми промежуточными веществами») здесь заменён числом записей
   Europe PMC, где МНН и слово «synthesis» или «process development» встречаются в заголовке или аннотации.
   Запрос шумит: «synthesis» часто означает биосинтез белка, синтез ДНК или простагландинов, а короткие или
   общеупотребимые МНН дают ложные совпадения. Патенты, ORD и PaRoutes не учитываются. Это фильтр отсечения
   «совсем не описанных» веществ, а не проверка документированности маршрута.
2. **F4 — только США и только по названиям.** Статус берётся из Orange Book (одна ежемесячная выгрузка) с
   сопоставлением названий без учёта регистра и с удалением слов-солей; `unknown` (нет в Orange Book, в том числе
   препараты, не продаваемые в США) из пула исключены. Учитываются любые строки Patent.txt и Exclusivity.txt,
   включая формуляционные патенты, поэтому старое вещество в новой лекарственной форме получает `protected`.
   Для веществ, у которых есть монопрепараты, статус считается по монопрепаратам (комбинации с новыми
   веществами не делают старое вещество «защищённым»); буквальное правило «любой продукт» дано в разделе F4 как
   чувствительность. Это справка с источником и датой, а не юридический вывод (SAFE-005). EMA и патенты РФ не
   проверялись.
3. **F6 — гейт по названиям, а не по структурам.** openFDA NDC покрывает только продукты, которые сейчас
   числятся в справочнике NDC, и включает все действующие вещества комбинированных продуктов с DEA-schedule,
   поэтому гейт намеренно перекрывает с запасом (fail-closed). Текстовое сопоставление с 21 CFR 1308.11–1308.15
   ловит только вещества, названные в тексте; аналоги, изомеры и соли под другими названиями не ловятся.
   Перечень ПП РФ № 681 машинно не проверялся: у всех кандидатов `ru_list_check=pending_manual`, ручная сверка
   обязательна до заморозки бенчмарка. Перечни INCB и OPCW не проверялись.
4. **F1 и F2 — только ChEMBL.** Подтверждение одобрения вторым регулятором (Drugs@FDA, EMA) и сверка МНН со
   списками WHO ещё не сделаны. МНН берётся из синонимов ChEMBL с `syn_type = INN`.
5. **F3 — эвристики.** Пептиды определяются числом α-аминоацильных амидных связей, металлы — по списку
   элементов, многокомпонентность — после удаления стандартных солей и растворителей RDKit.
6. **F7 и F8 — только структурные классы.** MaxMin выбирает структурно далёкие молекулы и по построению
   смещается к редким каркасам; правило «одна молекула на обобщённый каркас Bemis–Murcko» усиливает это
   смещение. Квоты F8 возвращают в допуск доли трёх структурных классов (N-гетероцикл, фтор, стереоцентр), но
   это не стратифицированная выборка: окна квот взяты от долей референса, внутри окна решает только
   разнообразие, а балансировки по ATC-классам и по году одобрения нет. Классы уровня маршрута (защитные
   группы, каталитические стадии, биокатализ, длина и конвергентность маршрута) здесь не измеряются вообще:
   маршрутов ещё нет, и квоты по ним можно будет задать только после их сбора.
7. **Статистика.** Выборка вложена в пул, пул — в референс, то есть группы не независимы; p-значение KS
   асимптотическое и дано только как ориентир. На 40 позициях доверительные интервалы широкие, а допуск ±10 п.п.
   мягкий. Референс — все одобренные малые молекулы ChEMBL после F1–F3 (включая вещества, которые гейт F6
   исключил бы; в отчёт они входят только агрегатно), а не только пероральные препараты.
8. **Дрейф источников.** ChEMBL, Orange Book и Europe PMC кэшируются в `data/cache/`; источники гейта F6
   запрашиваются заново при каждом запуске и не кэшируются (их хэши записаны в `coverage.json`), поэтому повтор
   в другой день может дать другие числа.
"""


def render_markdown(report: dict[str, Any]) -> str:
    src = report["sources"]
    funnel_rows = "\n".join(
        f"| {s['stage']} | {s['criterion']} | {s['n_out']} | {s['n_excluded'] if s['n_excluded'] is not None else '—'} |"
        for s in report["funnel"]
    )
    f3 = (
        "\n".join(f"| `{k}` | {v} |" for k, v in report["f3_exclusion_reasons"].items())
        or "| — | 0 |"
    )
    f4 = report["f4"]
    f6 = report["f6"]
    f5 = report["f5"]
    f7 = report["f7"]
    f8 = report["f8"]
    share_lines = []
    for row, (_, title, lit) in zip(report["shares"], SHARE_CLASSES):
        unq = row["sample_unquoted"]
        share_lines.append(
            f"| {title} | {fmt_share(row['reference'])} | {fmt_share(row['pool'])} | {fmt_share(row['sample'])} "
            f"| {row['sample']['delta_pp']:+.1f} | **{row['sample']['status']}** "
            f"| {100 * unq['share']:.1f}% ({unq['delta_pp']:+.1f}) | {unq['status']} | {row['pool']['status']} | {lit} |"
        )
    cont_lines = []
    for row, (_, title) in zip(report["continuous"], CONTINUOUS):
        mean, pv, sv = row["mean"], row["pool_vs_reference"], row["sample_vs_reference"]
        cont_lines.append(
            f"| {title} | {mean['reference']:.2f} | {mean['pool']:.2f} | {mean['sample']:.2f} "
            f"| {pv['ks']:.3f} | {pv['wasserstein']:.3f} | {sv['ks']:.3f} (p≈{sv['ks_p_asymptotic']:.2f}) "
            f"| {sv['wasserstein']:.3f} |"
        )
    covered = [
        t
        for row, (_, t, _) in zip(report["shares"], SHARE_CLASSES)
        if row["sample"]["status"] == "covered"
    ]
    gaps = [
        t
        for row, (_, t, _) in zip(report["shares"], SHARE_CLASSES)
        if row["sample"]["status"] == "gap"
    ]
    shifted = [
        t
        for row, (_, t) in zip(report["continuous"], CONTINUOUS)
        if row["sample_vs_reference"]["ks_p_asymptotic"] < 0.05
    ]
    gaps_unquoted = [
        t
        for row, (_, t, _) in zip(report["shares"], SHARE_CLASSES)
        if row["sample_unquoted"]["status"] == "gap"
    ]
    quota_lines = "\n".join(
        f"| {title} | {100 * q['reference_share']:.1f}% | {q['target']} | {q['window'][0]}–{q['window'][1]} "
        f"| {q['available_after_f7']} | **{q['selected']}** ({100 * q['share']:.1f}%) "
        f"| {'да' if q['satisfied'] else 'НЕТ'} |"
        for q, (_, title, _) in zip(f8["quotas"], SHARE_CLASSES)
    )
    summary = [
        f"- Покрыты выборкой из {f8['n_selected']}: {', '.join(covered) if covered else 'нет'}.",
        f"- Пробелы (gap): {', '.join(gaps) if gaps else 'нет'}.",
        f"- Квоты F8 выполнены: {'да' if f8['all_quotas_satisfied'] else 'НЕТ'}"
        f" (все окна достижимы при данном пуле: {'да' if f8['all_quotas_feasible'] else 'НЕТ'}). "
        f"Без квот пробелы были бы: {', '.join(gaps_unquoted) if gaps_unquoted else 'нет'}.",
        "- Непрерывные свойства со сдвигом выборки относительно референса (KS, p≈ < 0,05): "
        f"{', '.join(shifted) if shifted else 'не обнаружено'}.",
        "- Классы уровня маршрута (защитные группы, катализ, биокатализ, длина, конвергентность) не оценивались: "
        "маршрутов ещё нет.",
    ]
    return f"""# Покрытие реальных классов задачи: пул кандидатов v0 и выборка из {f8['n_selected']}

> Файл сгенерирован скриптом `eval/select_benchmark.py` (EVAL-001); правки руками будут перезаписаны.
> Только идентификаторы и вычисленные свойства молекул: маршрутов, реагентов и условий здесь нет (SAFE-004,
> `RESPONSIBLE_USE.md`). Патентный статус — справка с источником и датой, а не юридический вывод (SAFE-005).

- **Дата среза:** {report['as_of']} · **сгенерировано:** {report['generated_at']} · **run_id:** `{report['run_id']}`
- **Команда:** `{report['command']}`
- **Коммит:** `{report['git_sha']}` · **sha256 скрипта:** `{report['script_sha256'][:16]}…`
- **Версии:** Python {report['versions']['python']}, RDKit {report['versions']['rdkit']}, NumPy {report['versions']['numpy']}, requests {report['versions']['requests']}
- **Источники:** {src['chembl']['release']} (релиз {src['chembl']['release_date']}); Orange Book `{src['orange_book']['filename']}`
  (загружен {src['orange_book']['retrieved_at']}); openFDA NDC (last_updated {src['gate']['openfda_ndc']['last_updated']});
  eCFR 21 CFR 1308.11–1308.15 (up to date as of {src['gate']['ecfr_21_cfr_1308']['up_to_date_as_of']});
  Europe PMC REST (запросы {src['europe_pmc']['retrieved']})
- **Параметры:** seed {report['params']['seed']}, bootstrap {report['params']['n_boot']} повторов, Morgan r=2 2048 бит,
  патентная область `{report['params']['patent_scope']}`, порог Europe PMC ≥ {report['params']['epmc_min_hits']}

## Воронка отбора F1 → F8

| Фильтр | Критерий | Осталось | Отсеяно |
|---|---|---|---|
{funnel_rows}

Порядок применения: F1 → F2 → F3 → F4 → F6 → F5 → F7 → F8, чтобы запросы к Europe PMC не отправлялись по
веществам, которые отсекает гейт. Причины исключения по молекулам: `eval/reports/exclusions.csv`
({report['exclusions_written']} строк; ещё {report['exclusions_redacted']} строк не записаны, потому что
соответствующие вещества совпали с гейтом F6, а их названия не выводятся).

### F3: причины исключения

| Причина | Число |
|---|---|
{f3}

### F4: патентный статус в США (справочно, SAFE-005)

| Статус (область `{report['params']['patent_scope']}`) | Число |
|---|---|
| `off_patent_us` | {f4['off_patent_us']} |
| `protected` | {f4['protected']} |
| `unknown` (нет в Orange Book) | {f4['unknown']} |

Чувствительность: по буквальному правилу «любой продукт, включая комбинации» `protected` было бы
{f4['protected_if_all_products']}, `off_patent_us` — {f4['off_patent_us_if_all_products']}. Из `protected`
у {f4['protected_with_active_substance_patent']} есть действующий патент с флагом Drug Substance; у остальных
защита держится на формуляционных патентах, патентах на применение или эксклюзивности. Строк Orange Book с
неразобранной датой (считаются действующими): {src['orange_book_stats']['n_unparsed_dates']}.

### F6: регуляторные перечни (fail-closed)

- Исключено: **{f6['excluded']}** (только openFDA: {f6['openfda_only']}, только 21 CFR 1308: {f6['cfr_only']},
  оба источника: {f6['both']}). Названия исключённых веществ не выводятся нигде, только количество.
- Источники гейта запрашиваются при каждом запуске; при недоступности любого из них запуск прерывается до записи
  результатов. Хэши ответов: `coverage.json` → `sources.gate`.
- Перечень ПП РФ № 681: у всех {f6['remaining']} оставшихся кандидатов `ru_list_check=pending_manual`.

### F5: документированность (прокси)

Запрос Europe PMC: `TITLE_ABS:"<МНН>" AND (TITLE_ABS:"synthesis" OR TITLE_ABS:"process development")`, порог
≥ {report['params']['epmc_min_hits']}. Запрошено {f5['queried']}, ошибок {f5['errors']}, ниже порога {f5['below_threshold']};
медиана числа записей у прошедших — {f5['median_hits_kept']}.

### F7: дедупликация каркасов

В пуле {f7['pool']} молекул и {f7['n_scaffolds']} обобщённых каркасов Bemis–Murcko (из них ациклических молекул:
{f7['n_acyclic']}). На каждый каркас оставлен один представитель — с наибольшим числом записей Europe PMC, при
равенстве с меньшим ChEMBL ID. Осталось {f7['n_representatives']} кандидатов на выборку.

### F8: квоты структурных классов + разнообразие

Окно квоты для каждого класса — доля в референсной популяции ±{f8['quota_tolerance_pp']:.0f} п.п. (половина
допуска покрытия), пересчитанная в число позиций выборки.

| Класс | Доля в референсе | Цель | Окно квоты, позиций | Доступно после F7 | Отобрано | Квота выполнена |
|---|---|---|---|---|---|---|
{quota_lines}

Отбор: жадный MaxMin по Morgan r=2, 2048 бит. Фаза А добирает нижнюю границу каждой квоты, начиная с самого
редкого класса; фаза Б тратит остальные позиции только на разнообразие; верхние границы действуют в обеих фазах.
На каждом шаге берётся кандидат, максимально удалённый от всех уже отобранных, при равенстве — более
документированный, затем с меньшим ChEMBL ID. Случайного старта нет, поэтому результат зависит только от входных
данных. Позиций, занятых в фазе квот: {f8['picked_for_quota']}; в фазе разнообразия: {f8['picked_for_diversity']}.
Порядок отбора с причиной каждой позиции записан в `coverage.json` → `f8.selection_order`.

Разнообразие выборки: минимальное попарное расстояние Танимото {f8['min_pairwise_tanimoto_distance']:.3f},
медиана {f8['median_pairwise_tanimoto_distance']:.3f}. Для сравнения, тот же отбор без квот
(`MaxMinPicker.LazyBitVectorPick`, seed {report['params']['seed']}): минимум
{f8['baseline_maxmin_no_quota']['min_pairwise_tanimoto_distance']:.3f}, медиана
{f8['baseline_maxmin_no_quota']['median_pairwise_tanimoto_distance']:.3f} — это цена квоты в разнообразии.
Состав выборки без квот: `coverage.json` → `f8.baseline_maxmin_no_quota.chembl_ids`.

## Доли классов: референс (F1–F3) vs пул vs выборка

Доля и 95% bootstrap-интервал ({report['params']['n_boot']} повторов, seed {report['params']['seed']}). Статус
`covered`, если доля в выборке попадает в интервал референса или отличается от доли референса не более чем на
±10 п.п.; `gap` иначе, а также при пустой ячейке (доля в референсе ≥ 5%, в выборке 0).

Колонка «без квот» — та же выборка, собранная чистым MaxMin (F7 + seed {report['params']['seed']}, без F8):
она показывает, что именно квоты исправили.

| Класс | Референс | Пул | Выборка (F8) | Δ выборка − референс, п.п. | Статус выборки | Без квот (Δ, п.п.) | Статус без квот | Статус пула | Литература (справочно) |
|---|---|---|---|---|---|---|---|---|---|
{chr(10).join(share_lines)}

Литературные доли посчитаны на других популяциях и с другими определениями, поэтому служат только проверкой
порядка величины для референса.

## Непрерывные свойства

KS — статистика Колмогорова–Смирнова, W — расстояние Вассерштейна-1 (в единицах свойства); p≈ —
асимптотическое значение для пары «выборка vs референс».

| Свойство | Среднее: референс | пул | выборка | KS пул↔реф | W пул↔реф | KS выборка↔реф | W выборка↔реф |
|---|---|---|---|---|---|---|---|
{chr(10).join(cont_lines)}

## Итог (сформирован автоматически)

{chr(10).join(summary)}

## Ограничения

{LIMITATIONS}"""


# --------------------------------------------------------------------------------------------- main


def main() -> int:
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument(
        "--as-of",
        default="2026-10-13",
        help="cut-off date for patent/exclusivity expiry",
    )
    parser.add_argument(
        "--refresh",
        action="store_true",
        help="ignore data/cache and re-download sources",
    )
    parser.add_argument(
        "--patent-scope",
        choices=("single-first", "all-products"),
        default="single-first",
        help="which Orange Book products decide F4 (see Limitations in the report)",
    )
    args = parser.parse_args()
    as_of = date.fromisoformat(args.as_of)
    log(
        "start",
        as_of=as_of.isoformat(),
        patent_scope=args.patent_scope,
        refresh=args.refresh,
    )
    session = make_session()

    # F6 sources first: no gate, no pool (SAFE-002). Nothing has been written yet if this aborts.
    gate = load_gate(session)

    records, chembl_meta = fetch_chembl(session, args.refresh)
    funnel: list[dict[str, Any]] = []

    def stage(name: str, criterion: str, n_out: int, n_in: int | None) -> None:
        excluded = None if n_in is None else n_in - n_out
        funnel.append(
            {
                "stage": name,
                "criterion": criterion,
                "n_out": n_out,
                "n_excluded": excluded,
            }
        )
        log("filter", stage=name, kept=n_out, excluded=excluded)

    stage("F1a", "ChEMBL max_phase=4, molecule_type=Small molecule", len(records), None)
    parents = [
        r
        for r in records
        if (r.get("molecule_hierarchy") or {}).get(
            "parent_chembl_id", r["molecule_chembl_id"]
        )
        == r["molecule_chembl_id"]
    ]
    molecules = sorted((to_molecule(r) for r in parents), key=lambda m: m.sort_key)
    stage(
        "F1",
        "только родительские записи (соли и формы отброшены)",
        len(molecules),
        len(records),
    )

    for m in molecules:
        m.gate_hits = gate.match(m)
    exclusions: list[tuple[str, str, str, str]] = []
    redacted = 0

    def exclude(m: Molecule, stage_name: str, reason: str) -> None:
        nonlocal redacted
        if any(
            m.gate_hits
        ):  # never write anything that identifies a gate-matched substance
            redacted += 1
        else:
            exclusions.append((m.chembl_id, m.display_name, stage_name, reason))

    with_inn = []
    for m in molecules:
        if m.inn:
            with_inn.append(m)
        else:
            exclude(m, "F2", "no_inn_synonym")
    stage("F2", "есть синоним ChEMBL с syn_type = INN", len(with_inn), len(molecules))

    reference: list[Molecule] = []
    f3_reasons: Counter[str] = Counter()
    for m in with_inn:
        reason = standardize(m)
        if reason:
            f3_reasons[reason] += 1
            exclude(m, "F3", reason)
        else:
            reference.append(m)
    stage(
        "F3",
        "однозначная малая молекула (RDKit), = референсная популяция",
        len(reference),
        len(with_inn),
    )
    log("f3_reasons", **dict(f3_reasons))

    blob, ob_meta = fetch_orange_book(session, args.refresh)
    ob = build_orange_book(blob, as_of)
    log("orange_book_loaded", **ob.stats)
    for m in reference:
        patent_status(m, ob, args.patent_scope)
    f4_counts = Counter(m.patent_status for m in reference)
    f4_literal = Counter(m.patent_status_all_products for m in reference)
    off_patent = []
    for m in reference:
        if m.patent_status == "off_patent_us":
            off_patent.append(m)
        else:
            exclude(m, "F4", m.patent_status or "unknown")
    stage(
        "F4",
        f"нет действующих патентов и эксклюзивности в Orange Book на {as_of.isoformat()} (off_patent_us)",
        len(off_patent),
        len(reference),
    )

    gate_counts = Counter()
    cleared = []
    for m in off_patent:
        openfda_hit, cfr_hit = m.gate_hits
        if openfda_hit or cfr_hit:
            gate_counts[
                "both"
                if openfda_hit and cfr_hit
                else ("openfda_only" if openfda_hit else "cfr_only")
            ] += 1
            redacted += 1  # counted, never written
        else:
            cleared.append(m)
    stage(
        "F6",
        "нет совпадений с DEA-schedule (openFDA NDC) и 21 CFR 1308.11–15; fail-closed",
        len(cleared),
        len(off_patent),
    )

    epmc_errors = fetch_epmc_hits(session, cleared, args.refresh)
    pool = []
    below = 0
    for m in cleared:
        if m.epmc_hits is None:
            exclude(m, "F5", "epmc_error")
        elif m.epmc_hits < EPMC_MIN_HITS:
            below += 1
            exclude(m, "F5", f"epmc_hits={m.epmc_hits}")
        else:
            pool.append(m)
    stage(
        "F5",
        f"Europe PMC (прокси): ≥ {EPMC_MIN_HITS} записей с МНН и synthesis/process development",
        len(pool),
        len(cleared),
    )

    # F7: one representative per generic scaffold (most documented, then lowest ChEMBL id).
    by_scaffold: dict[str, list[Molecule]] = defaultdict(list)
    for m in pool:
        m.scaffold_smiles = generic_scaffold(m.mol)
        m.scaffold_id = (
            "gs_" + hashlib.sha1(m.scaffold_smiles.encode()).hexdigest()[:10]
            if m.scaffold_smiles
            else "acyclic"
        )
        by_scaffold[m.scaffold_smiles].append(m)
    representatives = sorted(
        (
            min(members, key=lambda x: (-(x.epmc_hits or 0), x.sort_key))
            for members in by_scaffold.values()
        ),
        key=lambda x: x.sort_key,
    )
    stage(
        "F7",
        "≤1 молекулы на обобщённый каркас Bemis–Murcko (представитель — наиболее документированный)",
        len(representatives),
        len(pool),
    )

    # F8: quotas from the reference shares + greedy MaxMin; the plain MaxMin pick is kept as a baseline.
    generator = rdFingerprintGenerator.GetMorganGenerator(radius=2, fpSize=2048)
    fps = [generator.GetFingerprint(m.mol) for m in representatives]
    n_pick = min(SAMPLE_SIZE, len(representatives))
    quotas = plan_quotas(reference, representatives, n_pick)
    picks, quota_counts, quota_trace = select_with_quotas(
        representatives, fps, quotas, n_pick
    )
    sample = [representatives[i] for i in picks]
    for m in sample:
        m.selected = True
    distances = tanimoto_distances([fps[i] for i in picks])

    baseline_picks = list(
        MaxMinPicker().LazyBitVectorPick(fps, len(fps), n_pick, seed=SEED)
    )
    sample_unquoted = [representatives[i] for i in baseline_picks]
    baseline_distances = tanimoto_distances([fps[i] for i in baseline_picks])

    stage(
        "F8",
        f"квоты структурных классов (±{100 * QUOTA_TOLERANCE:.0f} п.п. от референса) + MaxMin до {SAMPLE_SIZE}",
        len(sample),
        len(representatives),
    )
    if n_pick < SAMPLE_SIZE:
        log("f8_short_pool", wanted=SAMPLE_SIZE, got=n_pick)
    log(
        "f8_quotas",
        **{
            q.key: f"{quota_counts[q.key]}/[{q.lo_effective};{q.hi_effective}]"
            for q in quotas
        },
    )

    groups = {
        "reference": reference,
        "pool": pool,
        "sample": sample,
        "sample_unquoted": sample_unquoted,
    }
    shares = [share_row(key, groups) for key, _, _ in SHARE_CLASSES]
    continuous = [continuous_row(key, groups) for key, _ in CONTINUOUS]

    report: dict[str, Any] = {
        "schema": "synthroute.coverage/v0",
        "run_id": RUN_ID,
        "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "as_of": as_of.isoformat(),
        "command": RUN_COMMAND,
        "git_sha": git_sha(),
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "versions": {
            "python": platform.python_version(),
            "rdkit": rdBase.rdkitVersion,
            "numpy": np.__version__,
            "requests": requests.__version__,
            "pandas": pandas.__version__,
        },
        "params": {
            "seed": SEED,
            "n_boot": N_BOOT,
            "sample_size": SAMPLE_SIZE,
            "epmc_min_hits": EPMC_MIN_HITS,
            "mw_max": MW_MAX,
            "peptide_min_amide_bonds": PEPTIDE_MIN_AMIDES,
            "coverage_tolerance_pp": 100 * COVERAGE_TOLERANCE,
            "fingerprint": "Morgan r=2, 2048 bits",
            "patent_scope": args.patent_scope,
        },
        "sources": {
            "chembl": chembl_meta,
            "orange_book": ob_meta,
            "orange_book_stats": ob.stats,
            "gate": gate.meta,
            "europe_pmc": {
                "api": EPMC_SEARCH,
                "retrieved": epmc_retrieval_dates(),
                "query_template": epmc_query("<INN>"),
                "max_requests_per_second": EPMC_MAX_RPS,
            },
        },
        "funnel": funnel,
        "f3_exclusion_reasons": dict(f3_reasons.most_common()),
        "f4": {
            "off_patent_us": f4_counts["off_patent_us"],
            "protected": f4_counts["protected"],
            "unknown": f4_counts["unknown"],
            "protected_if_all_products": f4_literal["protected"],
            "off_patent_us_if_all_products": f4_literal["off_patent_us"],
            "protected_with_active_substance_patent": sum(
                1
                for m in reference
                if m.patent_status == "protected" and m.substance_patent_active
            ),
        },
        "f6": {
            "excluded": sum(gate_counts.values()),
            "openfda_only": gate_counts["openfda_only"],
            "cfr_only": gate_counts["cfr_only"],
            "both": gate_counts["both"],
            "remaining": len(cleared),
            "ru_list_check": "pending_manual",
        },
        "f5": {
            "queried": len(cleared),
            "errors": epmc_errors,
            "below_threshold": below,
            "median_hits_kept": float(np.median([m.epmc_hits for m in pool]))
            if pool
            else None,
        },
        "f7": {
            "pool": len(pool),
            "n_scaffolds": len(by_scaffold),
            "n_acyclic": len(by_scaffold.get("", [])),
            "n_representatives": len(representatives),
        },
        "f8": {
            "n_selected": len(sample),
            "quota_tolerance_pp": 100 * QUOTA_TOLERANCE,
            "quotas": [q.as_dict(quota_counts[q.key], len(sample)) for q in quotas],
            "all_quotas_satisfied": all(
                q.lo_effective <= quota_counts[q.key] <= q.hi_effective for q in quotas
            ),
            "all_quotas_feasible": all(q.feasible for q in quotas),
            "picked_for_quota": sum(
                1 for t in quota_trace if t["picked_for"].startswith("quota:")
            ),
            "picked_for_diversity": sum(
                1 for t in quota_trace if t["picked_for"] == "diversity"
            ),
            "selection_order": quota_trace,
            "min_pairwise_tanimoto_distance": float(min(distances))
            if distances
            else float("nan"),
            "median_pairwise_tanimoto_distance": float(np.median(distances))
            if distances
            else float("nan"),
            "baseline_maxmin_no_quota": {
                "note": "MaxMinPicker.LazyBitVectorPick over the same F7 representatives, seed "
                f"{SEED}, no quotas: the comparison shows what the quota costs in diversity",
                "n_selected": len(sample_unquoted),
                "min_pairwise_tanimoto_distance": float(min(baseline_distances))
                if baseline_distances
                else float("nan"),
                "median_pairwise_tanimoto_distance": float(np.median(baseline_distances))
                if baseline_distances
                else float("nan"),
                "chembl_ids": sorted(
                    (m.chembl_id for m in sample_unquoted),
                    key=lambda c: int(re.sub(r"\D", "", c)),
                ),
            },
        },
        "shares": shares,
        "continuous": continuous,
        "selected_chembl_ids": sorted(
            (m.chembl_id for m in sample), key=lambda c: int(re.sub(r"\D", "", c))
        ),
        "exclusions_written": len(exclusions),
        "exclusions_redacted": redacted,
    }

    write_candidates(pool)
    write_exclusions(exclusions)
    OUT_REPORT_JSON.parent.mkdir(parents=True, exist_ok=True)
    OUT_REPORT_JSON.write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    OUT_REPORT_MD.write_text(render_markdown(report), encoding="utf-8")
    log(
        "done",
        pool=len(pool),
        sample=len(sample),
        candidates=str(OUT_CANDIDATES.relative_to(ROOT)),
        report=str(OUT_REPORT_MD.relative_to(ROOT)),
    )
    return 0


def epmc_retrieval_dates() -> str:
    """Date range of the cached Europe PMC responses actually used (file modification times, UTC)."""
    files = list((CACHE / "epmc").glob("*.json.gz"))
    if not files:
        return "n/a"
    stamps = sorted(
        datetime.fromtimestamp(f.stat().st_mtime, timezone.utc).date().isoformat()
        for f in files
    )
    return stamps[0] if stamps[0] == stamps[-1] else f"{stamps[0]}…{stamps[-1]}"


if __name__ == "__main__":
    sys.exit(main())
