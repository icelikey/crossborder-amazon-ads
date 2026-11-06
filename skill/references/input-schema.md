# Input schema

The minimum review context is:

```json
{
  "marketplace": "US",
  "currency": "USD",
  "account_id": "redacted-or-internal-id",
  "date_start": "YYYY-MM-DD",
  "date_end": "YYYY-MM-DD",
  "attribution_window": "reported-window-or-unknown",
  "objective": "profit|launch|rank|defense|awareness|unknown",
  "target_acos": null,
  "report_path": "local/path.csv",
  "inventory_days": null,
  "price_or_coupon_change": null,
  "threshold_overrides": {}
}
```

Report rows should expose, where available: campaign, ad group, portfolio, targeting, match type, customer search term, product/ASIN, impressions, clicks, spend, sales, orders, CPC, CTR, CVR, ACOS, ROAS, budget, bid, placement, and status. Column names may be mapped by the helper; preserve the original headers in the evidence record.

Required for arithmetic: spend plus at least one of clicks, impressions, sales, or orders. Required for a bid/budget recommendation: spend, sales or orders, and a stated objective or target ACOS. Required for negative-targeting recommendations: query/targeting plus spend/clicks and product-fit context. Required for seasonal checks: event dates, inventory or replenishment signal, and marketplace.

Unknowns must be represented as `待确认` with a question, for example: `target_acos: 待确认（请提供目标ACOS或毛利约束）`.
