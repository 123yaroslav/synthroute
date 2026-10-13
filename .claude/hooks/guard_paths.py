#!/usr/bin/env python3
"""PreToolUse hook for Edit|Write|NotebookEdit: block writes to protected paths.

Exit code 2 blocks the tool call; stderr is shown to Claude with the rule ID to follow.
"""

from __future__ import annotations

import json
import os
import sys
from fnmatch import fnmatch
from pathlib import Path

# (glob relative to project root, reason with rule ID)
PROTECTED = [
    ("data/raw/**", "DATA-002: сырые данные не правятся; производные получаются скриптами"),
    ("eval/benchmark/test/**", "EVAL-002: тест-сплит заморожен; изменение возможно только через ADR и руками человека"),
    ("docs/rules/REGISTRY.md", "реестр генерируется: запустите `make rules`"),
]
SECRET_REASON = "CORE-004: секреты хранятся только у человека; шаблон находится в .env.example"


def is_secret_file(rel: str) -> bool:
    name = rel.rsplit("/", 1)[-1]
    return name != ".env.example" and (name == ".env" or name.startswith(".env."))


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except json.JSONDecodeError:
        return 0
    tool_input = payload.get("tool_input") or {}
    raw = tool_input.get("file_path") or tool_input.get("notebook_path")
    if not raw:
        return 0

    root = Path(os.environ.get("CLAUDE_PROJECT_DIR") or payload.get("cwd") or ".").resolve()
    try:
        rel = Path(raw).resolve().relative_to(root).as_posix()
    except ValueError:
        return 0  # outside the project: not our concern

    if is_secret_file(rel):
        print(f"Заблокировано правилом репозитория ({rel}). {SECRET_REASON}", file=sys.stderr)
        return 2
    for pattern, reason in PROTECTED:
        if fnmatch(rel, pattern):
            print(f"Заблокировано правилом репозитория ({rel}). {reason}", file=sys.stderr)
            return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
