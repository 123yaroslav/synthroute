#!/usr/bin/env python3
"""Validate repository rules in .claude/rules and keep docs/rules/REGISTRY.md in sync.

Usage:
    python3 scripts/check_rules.py           # validate and print a summary
    python3 scripts/check_rules.py --write   # validate and regenerate the registry
    python3 scripts/check_rules.py --check   # validate and fail if the registry is stale (CI)

Rule anatomy is documented in docs/rules/README.md. Stdlib only, Python 3.10+.
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RULES_DIR = ROOT / ".claude" / "rules"
INDEX_FILE = ROOT / "AGENTS.md"
REGISTRY_FILE = ROOT / "docs" / "rules" / "REGISTRY.md"
RETIRED_FILE = ROOT / "docs" / "rules" / "RETIRED.md"

CHECK_TAGS = {"auto:ci", "auto:hook", "auto:test", "auto:schema", "review", "agent"}
ALLOWED_FRONTMATTER_KEYS = {"paths"}

TITLE_RE = re.compile(r"^# ([A-Z]+) — (.+)$")
RULE_RE = re.compile(r"^### ([A-Z]+)-(\d{3}) · (MUST|SHOULD|MAY) · (.+)$")
FIELD_RE = re.compile(r"^- \*\*(Почему|Проверка|Исключения):\*\*\s*(.*)$")
RETIRED_RE = re.compile(r"^- ([A-Z]+-\d{3}) — ")
TODO_MARK = "[todo]"


@dataclass
class Rule:
    rule_id: str
    level: str
    title: str
    file: Path
    line: int
    fields: dict[str, str] = field(default_factory=dict)

    @property
    def check_tags(self) -> list[str]:
        head = self.fields.get("Проверка", "").replace(TODO_MARK, "")
        head = re.split(r"\s+—\s+", head, maxsplit=1)[0]
        return [t.strip() for t in head.split("+") if t.strip()]

    @property
    def is_todo(self) -> bool:
        return TODO_MARK in self.fields.get("Проверка", "")

    @property
    def is_automated(self) -> bool:
        return any(t.startswith("auto:") for t in self.check_tags) and not self.is_todo


@dataclass
class RuleFile:
    path: Path
    prefix: str = ""
    title: str = ""
    paths: list[str] = field(default_factory=list)
    rules: list[Rule] = field(default_factory=list)

    @property
    def rel(self) -> str:
        return self.path.relative_to(ROOT).as_posix()

    @property
    def scope(self) -> str:
        return ", ".join(f"`{p}`" for p in self.paths) if self.paths else "всегда"


def split_frontmatter(text: str) -> tuple[str | None, str, int]:
    """Return (frontmatter, body, body_start_line)."""
    if not text.startswith("---\n"):
        return None, text, 1
    end = text.find("\n---\n", 4)
    if end == -1:
        return None, text, 1
    fm = text[4:end]
    return fm, text[end + 5 :], fm.count("\n") + 3


def parse_frontmatter(fm: str, rf: RuleFile, errors: list[str]) -> None:
    current_key = None
    for raw in fm.splitlines():
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        key_match = re.match(r"^([A-Za-z_][\w-]*):\s*(.*)$", raw)
        if key_match:
            current_key, value = key_match.group(1), key_match.group(2).strip()
            if current_key not in ALLOWED_FRONTMATTER_KEYS:
                errors.append(f"{rf.rel}: frontmatter key '{current_key}' is ignored by Claude Code; only 'paths' is allowed")
            elif value:
                rf.paths.extend(p.strip().strip("\"'") for p in value.split(",") if p.strip())
            continue
        item = re.match(r"^\s+-\s+(.+)$", raw)
        if item and current_key == "paths":
            rf.paths.append(item.group(1).split(" #")[0].strip().strip("\"'"))
    if fm and not rf.paths:
        errors.append(f"{rf.rel}: frontmatter present but 'paths' is empty")


def parse_file(path: Path, errors: list[str]) -> RuleFile:
    rf = RuleFile(path=path)
    fm, body, offset = split_frontmatter(path.read_text(encoding="utf-8"))
    if fm is not None:
        parse_frontmatter(fm, rf, errors)

    current: Rule | None = None
    for i, line in enumerate(body.splitlines()):
        lineno = offset + i
        if not rf.prefix and (m := TITLE_RE.match(line)):
            rf.prefix, rf.title = m.group(1), m.group(2).strip()
        elif m := RULE_RE.match(line):
            prefix, num, level, title = m.groups()
            current = Rule(f"{prefix}-{num}", level, title.strip(), path, lineno)
            rf.rules.append(current)
        elif line.startswith("#"):
            current = None
        elif current and (m := FIELD_RE.match(line)):
            current.fields[m.group(1)] = m.group(2).strip()

    if not rf.prefix:
        errors.append(f"{rf.rel}: missing H1 title in the form '# PREFIX — Title'")
    if not rf.rules:
        errors.append(f"{rf.rel}: no rules found (expected '### PREFIX-NNN · LEVEL · Title')")
    return rf


def validate(files: list[RuleFile], errors: list[str]) -> None:
    seen_ids: dict[str, Rule] = {}
    seen_prefixes: dict[str, RuleFile] = {}
    retired = set()
    if RETIRED_FILE.exists():
        retired = {m.group(1) for ln in RETIRED_FILE.read_text(encoding="utf-8").splitlines() if (m := RETIRED_RE.match(ln))}
    index_text = INDEX_FILE.read_text(encoding="utf-8") if INDEX_FILE.exists() else ""

    for rf in files:
        if rf.prefix in seen_prefixes:
            errors.append(f"{rf.rel}: prefix {rf.prefix} already used in {seen_prefixes[rf.prefix].rel}")
        seen_prefixes[rf.prefix] = rf
        if rf.rel not in index_text:
            errors.append(f"{rf.rel}: not listed in the rules index of {INDEX_FILE.name}")

        for rule in rf.rules:
            where = f"{rf.rel}:{rule.line} {rule.rule_id}"
            if rf.prefix and not rule.rule_id.startswith(rf.prefix + "-"):
                errors.append(f"{where}: ID prefix does not match file prefix {rf.prefix}")
            if rule.rule_id in seen_ids:
                errors.append(f"{where}: duplicate ID (first at {seen_ids[rule.rule_id].file.relative_to(ROOT)})")
            seen_ids[rule.rule_id] = rule
            if rule.rule_id in retired:
                errors.append(f"{where}: ID is retired and must not be reused")
            for required in ("Почему", "Проверка"):
                if not rule.fields.get(required):
                    errors.append(f"{where}: missing '- **{required}:** …'")
            unknown = [t for t in rule.check_tags if t not in CHECK_TAGS]
            if unknown:
                errors.append(f"{where}: unknown check tag(s) {unknown}; allowed: {sorted(CHECK_TAGS)}")
            if rule.is_todo and not any(t.startswith("auto:") for t in rule.check_tags):
                errors.append(f"{where}: [todo] makes sense only for auto:* checks")


def render_registry(files: list[RuleFile]) -> str:
    rules = [r for rf in files for r in rf.rules]
    by_level = {lvl: sum(r.level == lvl for r in rules) for lvl in ("MUST", "SHOULD", "MAY")}
    automated = sum(r.is_automated for r in rules)
    todo = sum(r.is_todo for r in rules)
    pct = round(100 * automated / len(rules)) if rules else 0

    out = [
        "# Реестр правил",
        "",
        "> Генерируется `python3 scripts/check_rules.py --write`. Не редактировать вручную.",
        "",
        f"**Всего:** {len(rules)} · MUST {by_level['MUST']} · SHOULD {by_level['SHOULD']} · MAY {by_level['MAY']}  ",
        f"**Автоматизировано:** {automated}/{len(rules)} ({pct}%) · **Долг автоматизации** (`[todo]`): {todo}",
        "",
    ]
    for rf in files:
        out += [f"## {rf.prefix} — {rf.title}", "", f"Файл: `{rf.rel}` · Загрузка: {rf.scope}", ""]
        out += ["| ID | Уровень | Правило | Проверка |", "|---|---|---|---|"]
        for r in rf.rules:
            check = " + ".join(f"`{t}`" for t in r.check_tags) + (" ⏳" if r.is_todo else "")
            title = r.title.replace("|", r"\|")
            out.append(f"| {r.rule_id} | {r.level} | {title} | {check} |")
        out.append("")
    out += ["⏳ — автоматизация заявлена, но ещё не реализована.", ""]
    return "\n".join(out)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--write", action="store_true", help="regenerate docs/rules/REGISTRY.md")
    mode.add_argument("--check", action="store_true", help="fail if REGISTRY.md is stale")
    args = parser.parse_args()

    errors: list[str] = []
    paths = sorted(RULES_DIR.rglob("*.md"), key=lambda p: (p.name != "00-core.md", p.as_posix()))
    files = [parse_file(p, errors) for p in paths]
    validate(files, errors)

    if errors:
        print(f"✗ rules: {len(errors)} problem(s)", file=sys.stderr)
        for e in errors:
            print(f"  - {e}", file=sys.stderr)
        return 1

    registry = render_registry(files)
    if args.write:
        REGISTRY_FILE.parent.mkdir(parents=True, exist_ok=True)
        REGISTRY_FILE.write_text(registry, encoding="utf-8")
    elif args.check:
        current = REGISTRY_FILE.read_text(encoding="utf-8") if REGISTRY_FILE.exists() else ""
        if current != registry:
            print("✗ rules: docs/rules/REGISTRY.md is stale — run `make rules`", file=sys.stderr)
            return 1

    summary = next(ln for ln in registry.splitlines() if ln.startswith("**Автоматизировано"))
    total = sum(len(rf.rules) for rf in files)
    print(f"✓ rules: {total} rules in {len(files)} files · {summary.replace('**', '')}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
