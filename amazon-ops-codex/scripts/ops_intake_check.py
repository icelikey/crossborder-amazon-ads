#!/usr/bin/env python3
"""Validate an Amazon Ops intake file without contacting Amazon or mutating an account."""
from __future__ import annotations
import argparse, json
from pathlib import Path

REQUIRED = [
    "run_id", "account_alias", "marketplace", "currency", "timezone",
    "date_range", "business_goal", "report_paths", "authorized_actions", "owner",
]

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", required=True, help="Path to intake JSON")
    args = ap.parse_args()
    path = Path(args.input)
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        print(json.dumps({"ok": False, "error": f"cannot_read_json: {exc}"}, ensure_ascii=False))
        return 2
    missing = [k for k in REQUIRED if k not in data or data[k] in (None, "", [], {})]
    unknown_mode = data.get("authorized_actions") not in {"read_only", "proposal_only"} and not isinstance(data.get("authorized_actions"), list)
    result = {
        "ok": not missing and not unknown_mode,
        "missing": missing,
        "authorized_actions_valid": not unknown_mode,
        "account_alias": data.get("account_alias"),
        "marketplace": data.get("marketplace"),
        "date_range": data.get("date_range"),
        "report_count": len(data.get("report_paths", [])) if isinstance(data.get("report_paths"), list) else None,
        "message": "ready_for_read_only_review" if not missing and not unknown_mode else "mark_missing_fields_to_confirm",
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["ok"] else 1

if __name__ == "__main__":
    raise SystemExit(main())
