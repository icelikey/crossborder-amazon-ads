# Approval Gates

## Gate A — Local read-only

Allowed: inspect files, calculate metrics, compare exports, draft a brief and create a change proposal. No external writes.

## Gate B — Human-approved proposal

The human confirms the exact marketplace, campaign/target, field, old value, new value, reason, owner and observation window. Codex may prepare the command or browser steps, but does not execute unless the next gate is explicit.

## Gate C — External mutation

Requires an authorized connector/browser session and explicit permission for the named mutation. Capture before/after evidence, timestamp, response or screenshot, and rollback instruction. A successful request is not proof of business impact.

## Gate D — Post-change review

After the agreed window, compare the same metrics and window definition, record the result, and either keep, roll back or mark the hypothesis unresolved.

If any gate is missing, classify the action as `BLOCKED_BY_MISSING_SOURCE` or `PROPOSAL_ONLY`.
