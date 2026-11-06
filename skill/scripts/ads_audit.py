#!/usr/bin/env python3
"""Deterministic, local-first Amazon Ads triage helper.

It reads CSV or JSON rows, calculates safe metrics, and emits a review report.
It never calls Amazon APIs and never mutates an account.
"""
from __future__ import annotations

import argparse
import csv
import json
import math
from pathlib import Path
from typing import Any, Dict, Iterable, List


ALIASES = {
    "campaign": ["campaign", "campaign_name"],
    "ad_group": ["ad_group", "ad_group_name"],
    "query": ["customer_search_term", "search_term", "targeting", "keyword"],
    "impressions": ["impressions", "impression"],
    "clicks": ["clicks", "click"],
    "spend": ["spend", "cost", "ad_spend"],
    "sales": ["sales", "7_day_total_sales", "attributed_sales_7d", "attributed_sales"],
    "orders": ["orders", "7_day_total_orders", "attributed_conversions_7d", "attributed_orders"],
    "budget": ["budget", "daily_budget"],
    "bid": ["bid", "default_bid"],
}


def as_number(value: Any) -> float | None:
    if value is None or str(value).strip() == "":
        return None
    text = str(value).strip().replace(",", "").replace("$", "")
    try:
        result = float(text)
        return result if math.isfinite(result) else None
    except ValueError:
        return None


def canonical(row: Dict[str, Any]) -> Dict[str, Any]:
    lower = {str(k).strip().lower(): v for k, v in row.items()}
    out: Dict[str, Any] = dict(row)
    for key, aliases in ALIASES.items():
        for alias in aliases:
            if alias in lower:
                out[key] = lower[alias]
                break
    for key in ("impressions", "clicks", "spend", "sales", "orders", "budget", "bid"):
        out[key] = as_number(out.get(key))
    return out


def read_rows(path: Path) -> List[Dict[str, Any]]:
    if path.suffix.lower() == ".json":
        data = json.loads(path.read_text(encoding="utf-8"))
        if isinstance(data, dict):
            data = data.get("rows", [])
        if not isinstance(data, list):
            raise ValueError("JSON must be an array or an object with a rows array")
        return [canonical(row) for row in data if isinstance(row, dict)]
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return [canonical(row) for row in csv.DictReader(handle)]


def ratio(num: float | None, den: float | None) -> float | None:
    return None if num is None or den in (None, 0) else num / den


def metrics(row: Dict[str, Any]) -> Dict[str, float | None]:
    return {
        "ctr": ratio(row.get("clicks"), row.get("impressions")),
        "cpc": ratio(row.get("spend"), row.get("clicks")),
        "cvr": ratio(row.get("orders"), row.get("clicks")),
        "acos": ratio(row.get("spend"), row.get("sales")),
        "roas": ratio(row.get("sales"), row.get("spend")),
        "budget_utilization": ratio(row.get("spend"), row.get("budget")),
    }


def review(rows: Iterable[Dict[str, Any]], target_acos: float | None = None) -> Dict[str, Any]:
    facts: List[Dict[str, Any]] = []
    rule_hits: List[Dict[str, Any]] = []
    unknowns: List[str] = []
    for index, row in enumerate(rows, start=1):
        m = metrics(row)
        identity = row.get("query") or row.get("campaign") or f"row-{index}"
        facts.append({"row": index, "identity": identity, "metrics": m})
        if row.get("spend") is None:
            unknowns.append(f"row {index}: spend 待确认")
            continue
        if target_acos is None:
            unknowns.append("target_acos 待确认（未执行效率方向判断）")
        util = m["budget_utilization"]
        if util is not None and util >= 0.90 and target_acos is not None and m["acos"] is not None and m["acos"] <= target_acos:
            rule_hits.append({"row": index, "rule": "budget_near_cap_and_at_target", "action": "candidate_budget_increase_10_percent", "status": "需要人工确认"})
        clicks = row.get("clicks") or 0
        orders = row.get("orders") or 0
        # ACOS is a ratio, so it is not valid to compare it with spend as a
        # dollar threshold. Use an explicit click sample-size trigger here;
        # the agent should request target CPA/margin before adding a spend rule.
        if orders == 0 and clicks >= 8:
            rule_hits.append({"row": index, "rule": "spend_without_orders_review", "action": "inspect_query_fit_before_negative", "status": "需要人工确认"})
        query = str(row.get("query") or "").strip()
        if query and orders > 0:
            rule_hits.append({"row": index, "rule": "converting_query_harvest_candidate", "action": "candidate_exact_or_phrase_harvest", "status": "需要人工确认"})
    status = "pass" if facts and not unknowns else ("partial" if facts else "blocked")
    return {"facts": facts, "rule_hits": rule_hits, "unknowns": sorted(set(unknowns)), "data_quality": {"status": status, "row_count": len(facts)}}


def main() -> int:
    parser = argparse.ArgumentParser(description="Local Amazon Ads triage; no API calls or account mutations")
    parser.add_argument("--input", required=True, help="CSV or JSON report")
    parser.add_argument("--mode", default="all", choices=["all", "structure", "budget_bid", "negative_search_terms", "report_review", "seasonal"])
    parser.add_argument("--target-acos", type=float, default=None, help="Decimal, e.g. 0.30")
    parser.add_argument("--output", required=True, help="JSON output path")
    args = parser.parse_args()
    rows = read_rows(Path(args.input))
    result = review(rows, args.target_acos)
    result["review"] = {"mode": args.mode, "source_path": str(Path(args.input).resolve()), "target_acos": args.target_acos}
    Path(args.output).write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({"status": "ok", "rows": len(rows), "output": str(Path(args.output).resolve())}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
