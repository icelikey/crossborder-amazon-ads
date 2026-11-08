---
name: amazon-ops-codex
description: "Use Codex as an auditable operating copilot for Amazon marketplace teams: intake, daily pulse, report triage, search-term decisions, weekly review, seasonal planning, and execution logs. Use when the user asks how Codex should participate in Amazon operations; require source data and human approval before account mutations."
---

# Amazon Operations with Codex

Use this skill when a seller or team wants Codex to participate in Amazon operations. Codex is the analysis, documentation and decision-support layer. It does not become the account owner, invent live metrics, or silently change campaigns.

## Operating contract

1. Start in `READ_ONLY`: preserve the original exports, record account alias, marketplace, currency, timezone, date range, attribution window, business goal and owner.
2. Run `python scripts/ops_intake_check.py --input <intake.json>` before making a brief. Missing fields become `待确认 / To be confirmed`.
3. If an advertising CSV/JSON export exists, hand arithmetic and rule checks to the companion `crossborder-amazon-ads` skill and keep its output attached to the run.
4. Return one operating brief with five layers: observed facts, data gaps, hypotheses, proposed actions, and validation plan. Every action has an owner, deadline, stop rule and evidence grade.
5. Classify each action as `READ_ONLY`, `PROPOSAL_ONLY`, `EXECUTE_AFTER_APPROVAL`, or `BLOCKED_BY_MISSING_SOURCE`. The default is `PROPOSAL_ONLY`.
6. Ask for explicit authorization immediately before a live mutation. The authorization must name the marketplace, campaign/target, field, old value, new value, reason and observation window. Record the result and rollback path.

## Choose an operating mode

- **Daily pulse**: 10-minute health check across delivery, spend, conversion, inventory and anomalies; output one reversible next action.
- **Campaign triage**: map campaign → ad group → target → match type → product, then separate structure, budget, bid, placement and conversion issues.
- **Search-term review**: classify queries by relevance, clicks/spend, orders, product fit and intent; propose promotion, observation or negative exact/phrase with a rollback note.
- **Weekly operating review**: reconcile totals, compare segments and windows, review experiments, assign owners and write next-week priorities.
- **Seasonal readiness**: inspect inventory/eligibility, listing, price/coupon, campaign coverage, budget headroom, creative and post-event rollback.
- **Codex workflow design**: create a team SOP, intake form, prompt pack or evidence ledger for recurring Amazon work.

## Daily operating loop

1. Confirm the source window and marketplace.
2. Check delivery anomalies: impressions, clicks, spend, orders, sales and budget utilization.
3. Check conversion and inventory constraints before recommending more traffic.
4. Explain anomalies as hypotheses, not facts, unless the export proves them.
5. Select at most one reversible experiment for the next window; write the expected signal and stop rule.
6. Log the action, owner, deadline and source path in the daily brief.

## Weekly operating loop

Reconcile report totals first. Then review structure, search terms, budget/bid, placements, product stage, listing/creative and experiment results. Separate `Fact`, `Explanation`, `Hypothesis`, `Action` and `Result`; do not turn a weekly average into a causal claim. End with a ranked queue for `today`, `this week`, `observe`, and `blocked`.

## Codex participation boundaries

- Codex may read local exports, compare files, calculate metrics, draft briefs, create templates and prepare reversible change plans.
- Codex must not claim live account state from an old export, treat examples as universal thresholds, infer policy from memory, expose credentials, or copy paid-course transcripts.
- API/browser execution, bid/budget edits, campaign creation, negative targeting, listing changes and publishing are separate gates. A configured connector or HTTP 200 is not proof of a successful account mutation.
- When a required source, policy version, inventory value, attribution window or authorization is missing, stop that branch and mark `待确认 / To be confirmed`.

## Output contract

Use the structure in `references/decision-log.md` and the templates under `templates/`. At minimum include:

- `Run ID`, account alias, marketplace, currency, timezone, source window and source paths;
- facts with metric definitions and evidence grade;
- data gaps and assumptions;
- proposed action, owner, deadline, stop rule and validation metric;
- approval state and rollback plan;
- a final list of claims that are `可执行 / Needs confirmation / Cannot determine`.

## References

Read only the reference needed for the current mode:

- [intake-schema.md](references/intake-schema.md) for required context and report paths;
- [report-to-action-map.md](references/report-to-action-map.md) for mapping exports to decisions;
- [approval-gates.md](references/approval-gates.md) before any external or account mutation;
- [decision-log.md](references/decision-log.md) for evidence and action logging;
- [codex-prompt-pack.md](references/codex-prompt-pack.md) for reusable daily, weekly and seasonal prompts.
