#!/usr/bin/env python3
"""Read this project's actual free-tier quotas from the API itself.

The public rate-limit page no longer lists per-model numbers, but a 429 response carries
google.rpc.QuotaFailure violations (quotaId, quotaValue) and RetryInfo. One cheap request per model is enough.

    uv run --env-file .env --no-project --python 3.12 --with google-genai scripts/check_quota.py \
        --models gemini-3.5-flash gemini-3.1-pro-preview gemini-3.5-flash-lite

Writes docs/reports/assets/quota-probe.json. The API key is never printed or written.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

from google import genai
from google.genai import errors, types

ROOT = Path(__file__).resolve().parent.parent
OUT_FILE = ROOT / "docs" / "reports" / "assets" / "quota-probe.json"


def redact(text: str) -> str:
    key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY") or ""
    return text.replace(key, "***") if key else text


def details_of(exc: errors.APIError) -> list[dict]:
    d = getattr(exc, "details", None)
    if isinstance(d, dict):
        return d.get("error", {}).get("details", []) or []
    return []


def probe(client: genai.Client, model: str) -> dict:
    row: dict = {"model": model}
    try:
        resp = client.models.generate_content(model=model, contents="hi")
        row.update(ok=True, model_version=getattr(resp, "model_version", None),
                   note="quota not exhausted: limits are not disclosed on a successful call")
        return row
    except errors.APIError as exc:
        row.update(ok=False, code=getattr(exc, "code", None))
        quotas, retry = [], None
        for d in details_of(exc):
            kind = d.get("@type", "")
            if kind.endswith("QuotaFailure"):
                for v in d.get("violations", []):
                    quotas.append({
                        "quota_id": v.get("quotaId"),
                        "quota_value": v.get("quotaValue"),  # absent means the limit is 0 for this tier
                        "metric": v.get("quotaMetric"),
                        "model_dimension": (v.get("quotaDimensions") or {}).get("model"),
                    })
            elif kind.endswith("RetryInfo"):
                retry = d.get("retryDelay")
        row["quotas"] = quotas
        row["retry_delay"] = retry
        if retry and retry.endswith("s"):
            row["retry_delay_hours"] = round(float(retry[:-1]) / 3600, 1)
        if not quotas:
            row["raw"] = redact(str(exc))[:400]
        return row


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--models", nargs="+", required=True)
    args = ap.parse_args()
    if not (os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")):
        print("GEMINI_API_KEY is not set: run via `uv run --env-file .env ...`", file=sys.stderr)
        return 1

    client = genai.Client(http_options=types.HttpOptions(timeout=45_000, retry_options=types.HttpRetryOptions(attempts=1)))
    rows = [probe(client, m) for m in args.models]
    for r in rows:
        if r["ok"]:
            print(f"{r['model']:<28} ok (quota not exhausted)")
        else:
            for q in r.get("quotas", []):
                print(f"{r['model']:<28} {q['quota_id']}: {q['quota_value'] or '— (0 на этом тире)'}"
                      f"  [{q['model_dimension']}]")
            print(f"{'':<28} retry after {r.get('retry_delay_hours', '?')} h")

    OUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUT_FILE.write_text(json.dumps({
        "checked_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "note": "Quota values are reported by the API only when the quota is exhausted (HTTP 429).",
        "results": rows,
    }, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"log → {OUT_FILE.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
