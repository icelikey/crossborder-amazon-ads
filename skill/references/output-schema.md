# Output schema

Return JSON when requested:

```json
{
  "review": {
    "mode": "structure|budget_bid|negative_search_terms|report_review|seasonal|all",
    "marketplace": "US",
    "currency": "USD",
    "date_range": {"start": "YYYY-MM-DD", "end": "YYYY-MM-DD"},
    "evidence_grade": "A|B|C|D",
    "source_trace": ["path or export id"],
    "data_quality": {"status": "pass|partial|blocked", "findings": []}
  },
  "facts": [],
  "rule_hits": [],
  "recommendations": [
    {
      "priority": "P0|P1|P2",
      "action": "",
      "scope": "campaign/ad_group/target/query/account",
      "reason": "",
      "confidence": "high|medium|low",
      "status": "可直接执行|需要人工确认|不可判断",
      "validation_metric": "",
      "validation_window": "",
      "rollback": ""
    }
  ],
  "unknowns": [],
  "next_questions": []
}
```

Every recommendation must include a source trace, confidence, validation metric, and rollback. If a field cannot be filled, use `待确认`, not a guessed value.
