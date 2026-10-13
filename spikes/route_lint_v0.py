#!/usr/bin/env python3
"""SPIKE (stage 1): prove route-lint v0 is feasible — schema check + RL1 structures + RL2 balance + RL3 provenance + RL4 graph.

Not production code: it will be rewritten into backend/app/validation with tests (feature 001).
    uv run --no-project --python 3.12 --with rdkit --with jsonschema spikes/route_lint_v0.py <route.json>... [--json]
"""

from __future__ import annotations

import json
import sys
from collections import Counter
from importlib.metadata import version
from pathlib import Path

import jsonschema
import rdkit
from rdkit import Chem, RDLogger

RDLogger.DisableLog("rdApp.*")
ROOT = Path(__file__).resolve().parent.parent
SCHEMA = json.loads((ROOT / "schemas/route/v0.1/route.schema.json").read_text(encoding="utf-8"))
CHECK_VERSION = "0.1-spike"
SMALL_BYPRODUCTS = {"H2O": Counter({"H": 2, "O": 1}), "HCl": Counter({"H": 1, "Cl": 1})}


def element_counts(mol: Chem.Mol) -> tuple[Counter, int]:
    mol = Chem.AddHs(mol)
    return Counter(a.GetSymbol() for a in mol.GetAtoms()), sum(a.GetFormalCharge() for a in mol.GetAtoms())


def diag(code: str, level: str, msg: str) -> dict:
    return {"check_id": code, "level": level, "message": msg}


def lint(doc: dict) -> dict:
    errors = sorted(jsonschema.Draft202012Validator(SCHEMA).iter_errors(doc), key=lambda e: list(e.path))
    if errors:
        return {"route_id": doc.get("route", {}).get("id"), "schema_valid": False,
                "diagnostics": [diag("RL001", "error", f"{'/'.join(map(str, e.path)) or '<root>'}: {e.message}") for e in errors]}

    route_diags: list[dict] = []
    mols: dict[str, tuple[Counter, int]] = {}
    for s in doc["substances"]:  # RL1xx: structures
        mol = Chem.MolFromSmiles(s["smiles"])
        if mol is None:
            route_diags.append(diag("RL101", "error", f"{s['id']}: SMILES does not parse/sanitize"))
            continue
        mols[s["id"]] = element_counts(mol)
        if s.get("inchikey") and s["inchikey"] != Chem.MolToInchiKey(mol):
            route_diags.append(diag("RL102", "error", f"{s['id']}: declared InChIKey != computed {Chem.MolToInchiKey(mol)}"))

    known = {s["id"] for s in doc["substances"]}
    produced = set()
    steps = []
    for st in doc["steps"]:
        d: list[dict] = []
        ids = [p["substance_id"] for p in st["inputs"] + st["outputs"]]
        for sid in ids:  # RL401: references
            if sid not in known:
                d.append(diag("RL401", "error", f"unknown substance '{sid}'"))
        produced |= {p["substance_id"] for p in st["outputs"]}

        if all(sid in mols for sid in ids):  # RL2xx: two-level balance (literature reactions are mostly unbalanced)
            left, right, ql, qr = Counter(), Counter(), 0, 0
            for p in st["inputs"]:
                c, q = mols[p["substance_id"]]
                left.update({k: v * p["coefficient"] for k, v in c.items()}); ql += q * p["coefficient"]
            for p in st["outputs"]:
                c, q = mols[p["substance_id"]]
                right.update({k: v * p["coefficient"] for k, v in c.items()}); qr += q * p["coefficient"]
            missing, extra = left - right, right - left
            from_nowhere = Counter({k: v for k, v in extra.items() if k != "H"})
            if from_nowhere:  # level 1 (blocking): product heavy atoms must come from the declared reactants
                d.append(diag("RL203", "error", f"product heavy atoms missing from reactants: {dict(from_nowhere)}"))
            elif missing or extra:  # level 2 (strict): report, do not block
                hint = next((f"; hint: maybe undeclared byproduct {n}" for n, f in SMALL_BYPRODUCTS.items() if missing == f and not extra), "")
                d.append(diag("RL201", "warning", f"not strictly balanced: products lack {dict(missing)}, extra {dict(extra)}{hint}"))
            if ql != qr:
                d.append(diag("RL202", "warning", f"charge not balanced: {ql} → {qr}"))
        elif not any(x["check_id"] == "RL401" for x in d):
            d.append(diag("RL204", "error", "balance not computable: a participant has an invalid structure"))

        real_sources = [p for p in st["provenance"] if p["kind"] != "model"]  # RL301: provenance caps the status
        if not st["provenance"]:
            d.append(diag("RL301", "warning", "no provenance at all: status capped at hypothesis"))
        elif not real_sources:
            d.append(diag("RL302", "info", "only model provenance: status capped at hypothesis"))

        status = "failed" if any(x["level"] == "error" for x in d) else ("computed" if real_sources else "hypothesis")
        steps.append({"step_id": st["id"], "status": status, "diagnostics": d})

    if doc["route"]["target_id"] not in produced:  # RL402: graph reaches the target
        route_diags.append(diag("RL402", "error", "no step produces the target"))

    valid = sum(s["status"] != "failed" for s in steps)
    return {"route_id": doc["route"]["id"], "schema_valid": True, "diagnostics": route_diags, "steps": steps,
            "summary": {"valid_steps": valid, "total_steps": len(steps)},
            "tool_versions": {"route-lint": CHECK_VERSION, "rdkit": rdkit.__version__, "jsonschema": version("jsonschema")}}


def render(path: str, rep: dict) -> str:
    out = [f"{path}"]
    if not rep["schema_valid"]:
        out.append("  ✗ schema invalid")
        out += [f"    {d['check_id']} {d['message']}" for d in rep["diagnostics"]]
        return "\n".join(out)
    s = rep["summary"]
    out[0] += f": {s['total_steps']} steps · valid {s['valid_steps']}/{s['total_steps']}"
    out += [f"  route  {d['check_id']} {d['message']}" for d in rep["diagnostics"]]
    mark = {"computed": "✓", "hypothesis": "?", "failed": "✗", "literature": "✓"}
    for st in rep["steps"]:
        out.append(f"  {st['step_id']:<4} {mark[st['status']]} {st['status']}")
        out += [f"         {d['check_id']} {d['message']}" for d in st["diagnostics"]]
    return "\n".join(out)


if __name__ == "__main__":
    as_json = "--json" in sys.argv
    reports = {p: lint(json.loads(Path(p).read_text(encoding="utf-8"))) for p in sys.argv[1:] if p != "--json"}
    print(json.dumps(reports, ensure_ascii=False, indent=2) if as_json else "\n\n".join(render(p, r) for p, r in reports.items()))
