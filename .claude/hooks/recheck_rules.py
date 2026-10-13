#!/usr/bin/env python3
"""PostToolUse hook for Edit|Write: after a rules file changes, validate rules and refresh the registry.

On failure exits 2 so Claude sees the validation errors and fixes them right away.
"""

from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path

WATCHED_PREFIXES = (".claude/rules/", "AGENTS.md", "docs/rules/RETIRED.md")


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except json.JSONDecodeError:
        return 0
    raw = (payload.get("tool_input") or {}).get("file_path")
    if not raw:
        return 0

    root = Path(os.environ.get("CLAUDE_PROJECT_DIR") or payload.get("cwd") or ".").resolve()
    try:
        rel = Path(raw).resolve().relative_to(root).as_posix()
    except ValueError:
        return 0
    if not rel.startswith(WATCHED_PREFIXES):
        return 0

    result = subprocess.run(
        [sys.executable, str(root / "scripts" / "check_rules.py"), "--write"],
        capture_output=True,
        text=True,
        cwd=root,
    )
    if result.returncode != 0:
        print(result.stderr or result.stdout, file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
