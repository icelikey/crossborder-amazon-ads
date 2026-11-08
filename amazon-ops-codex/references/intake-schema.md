# Amazon Ops Intake Schema

Use this schema before interpreting an export. JSON is preferred; Markdown is acceptable when every field is present.

| Field | Required | Meaning |
|---|---:|---|
| `run_id` | yes | Stable ID for the review run |
| `account_alias` | yes | Non-sensitive account label; never store credentials |
| `marketplace` | yes | Example: US, UK, DE; do not infer from currency |
| `currency` | yes | Reporting currency |
| `timezone` | yes | Reporting and deadline timezone |
| `date_range` | yes | Start/end dates for every report |
| `attribution_window` | preferred | Attribution rule or `待确认` |
| `business_goal` | yes | Explore, validate, scale, defend, or another explicit goal |
| `inventory_status` | preferred | Available units, inbound risk or `待确认` |
| `report_paths` | yes | Local CSV/JSON paths and report types |
| `authorized_actions` | yes | `read_only`, `proposal_only`, or named mutation permission |
| `owner` | yes | Human responsible for review and approval |
| `constraints` | preferred | Margin, budget ceiling, policy, launch date or other limits |

If a required field is missing, continue only with unaffected diagnostics and label the missing field `待确认 / To be confirmed`.
