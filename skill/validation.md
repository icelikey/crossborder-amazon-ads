# Validation record

Date: 2026-11-06 (Asia/Shanghai)

Commands run:

```powershell
$env:PYTHONUTF8='1'
python C:/Users/admin/.codex/skills/.system/skill-creator/scripts/quick_validate.py H:/直播人/crossborder-amazon-ads-skill/crossborder-amazon-ads
python H:/直播人/crossborder-amazon-ads-skill/crossborder-amazon-ads/scripts/ads_audit.py `
  --input H:/直播人/crossborder-amazon-ads-skill/crossborder-amazon-ads/assets/sample-report.csv `
  --mode all --target-acos 0.30 `
  --output H:/直播人/crossborder-amazon-ads-skill/crossborder-amazon-ads/assets/sample-review.json
```

Observed result:

- `quick_validate.py`: `Skill is valid!`
- `ads_audit.py`: exited 0, read 2 rows, wrote `assets/sample-review.json`.
- The sample produced a budget-near-cap candidate, a converting-query harvest candidate, and a zero-order query review. All are marked `需要人工确认`; no account API or mutation is used.

Known limits:

- The helper is a local triage tool, not an Amazon Ads API client.
- It cannot establish attribution, incrementality, policy eligibility, margin, inventory, or current UI behavior.
- The course folders were not transcribed; title-only or unverified course claims remain `待确认`/low evidence until a human reviews the authorized source and attaches a trace.
