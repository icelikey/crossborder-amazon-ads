---
name: crossborder-amazon-ads
description: "Diagnose and improve Amazon Ads for cross-border sellers using auditable inputs, configurable rules, and clear next actions. Use for Sponsored Products, Sponsored Brands, Sponsored Display, search-term reports, budget/bid decisions, negative targeting, and seasonal readiness; do not use it to claim account performance without source data."
---

# Cross-border Amazon Ads

Use this skill when a seller needs a repeatable advertising review or a practical operating checklist. Keep the account, marketplace, currency, attribution window, date range, and source report attached to every conclusion.

## Operating contract

1. Capture the intake fields in `references/input-schema.md`. If a required field is absent, label it `待确认` and continue only with diagnostics that do not depend on it.
2. Load `references/evidence-and-rules.md` for metric definitions, evidence grades, configurable thresholds, and the five supported modes.
3. Run the deterministic helper when a CSV/JSON export is available:
   `python scripts/ads_audit.py --input <report.csv> --mode all --output <report.json>`
4. Return a concise decision report with: observed facts, assumptions, rule hits, recommended action, owner, deadline, and validation metric. Never silently fill missing spend, sales, orders, clicks, impressions, or currency.
5. Separate `可直接执行` (reversible account edits after human review), `需要人工确认`, and `不可判断`. Do not change bids, budgets, targeting, or campaigns directly unless the user explicitly authorizes the specific mutation.

## Supported modes

- `structure`: map campaign → ad group → targeting → match type → product, then detect overlap, orphan targets, mixed objectives, and missing brand/product separation.
- `budget_bid`: diagnose delivery and efficiency using spend, sales, orders, clicks, impressions, CPC, CTR, CVR, ACOS, ROAS, and budget utilization; propose a bounded adjustment and a test window.
- `negative_search_terms`: classify query rows by intent, conversion evidence, spend waste, and product fit; propose negative exact/phrase with rationale and a rollback note.
- `report_review`: reconcile report totals, inspect segments and date windows, identify data quality gaps, and produce a prioritized issue list.
- `seasonal`: check inventory, lead time, price/coupon, listing readiness, campaign coverage, budget headroom, creative, and post-event rollback plan. Mark marketplace-specific policy or date assumptions `待确认`.

## Decision discipline

- A formula is not proof of causality. Use `规则命中` for arithmetic and `待验证假设` for explanations such as ranking lift or cannibalization.
- Thresholds are starting points, not universal truths. Keep them in the input or report and state the sample-size requirement.
- Treat an empty or partial export as a data-quality finding; never produce a confident "increase" or "decrease" recommendation from one metric alone.
- Do not reproduce course transcripts or paid-content wording. Distill only reusable procedures and short summaries from authorized material.

## References

- Read [references/input-schema.md](references/input-schema.md) before accepting data.
- Read [references/evidence-and-rules.md](references/evidence-and-rules.md) for formulas, thresholds, and the five modes.
- Read [references/output-schema.md](references/output-schema.md) when producing JSON or integrating into another tool.
- Read [references/course-boundary.md](references/course-boundary.md) when the request refers to the two source course folders.
