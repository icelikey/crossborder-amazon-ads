# Decision Log Contract

Use one row per decision or experiment.

```text
run_id:
account_alias:
marketplace:
currency:
timezone:
source_window:
source_paths:

fact:
evidence_grade: A | B | C | D
assumption_or_gap:
hypothesis:
proposed_action:
action_class: READ_ONLY | PROPOSAL_ONLY | EXECUTE_AFTER_APPROVAL | BLOCKED_BY_MISSING_SOURCE
owner:
deadline:
stop_rule:
validation_metric:
approval_state:
rollback_plan:
result:
```

Evidence grades:

- `A`: directly observed in a complete, identified export or confirmed live response;
- `B`: supported by multiple exports or a reproducible calculation;
- `C`: method signal, sample, or partial export;
- `D`: hypothesis, example, or unverified claim.
