# Evidence and rules

## Evidence grades

- `A`: exported row-level report with marketplace, currency, date range, and source path; arithmetic is reproducible.
- `B`: aggregated report with clear date range and definitions, but no row-level trace.
- `C`: screenshot, narrative, or course case without denominator; use for hypotheses only.
- `D`: title, memory, or unsupported claim; do not use for account decisions.

Always state the grade next to a recommendation. A grade C or D source cannot establish a market-ready result.

## Stable formulas

When denominators are non-zero:

- `CTR = clicks / impressions`
- `CPC = spend / clicks`
- `CVR = orders / clicks`
- `ACOS = spend / sales`
- `ROAS = sales / spend`
- `budget_utilization = spend / budget`

Use reported values when they disagree with calculated values, but flag the discrepancy and preserve both.

## Configurable starting rules

The helper uses conservative defaults that should be overridden for the account:

1. `budget_utilization >= 0.90` and efficiency is at or better than target: candidate for a small budget increase (default `+10%`, cap `+20%`).
2. `budget_utilization < 0.50` with low delivery: inspect eligibility, bid, targeting volume, and inventory before cutting budget.
3. Spend with zero orders: do not automatically negate; inspect clicks, intent, listing fit, and sample size. Default review flags: `clicks >= 8` or `spend >= 2x target CPA`.
4. Query with orders and product fit: candidate for harvesting into a controlled exact or phrase target, after deduplication and attribution-window check.
5. Query with spend/clicks and clear mismatch: candidate for negative exact or phrase. Preserve the query and reason.
6. Bid changes must be bounded, reversible, and tied to a validation window. Default proposal is `±10%`, never an automatic write.

These are triage rules, not guarantees. Add sample-size, margin, inventory, and marketplace policy checks before execution.

## Mode procedure

### Structure

Inventory the hierarchy and label each campaign by objective, product, match type, placement, and lifecycle stage. Flag mixed objectives, duplicate targets across campaigns, missing negatives between discovery and harvesting layers, orphan ad groups, and campaigns with no eligible product. Output a map plus the smallest next correction.

### Budget and bid

Reconcile spend, sales, orders, budget, and target ACOS. Diagnose delivery before efficiency: eligibility → inventory → impressions → clicks → conversion. Propose one bounded change, a holdout or comparison period, a stop condition, and the metric to check.

### Negative search terms

Group by exact query, normalize case/spacing, keep marketplace language intact, and review product fit. Prefer negative exact when one query is wrong but the phrase may be useful; prefer negative phrase only when the whole phrase family is unsuitable. Record evidence and rollback.

### Report review

Check date range, attribution window, currency, duplicate rows, missing columns, zero denominators, and report total reconciliation. Rank issues by impact × confidence × reversibility. Do not infer organic lift or incremental sales from an ad report alone.

### Seasonal readiness

Run a pre-event and post-event checklist. Confirm inventory runway, replenishment lead time, price/coupon, listing/creative, campaign status, budget headroom, placement strategy, search-term harvesting, and rollback. Dates, policy, and eligibility are marketplace-specific and must be verified from current official sources before execution.
