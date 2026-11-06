---
name: "021"
description: "Evaluate venture ideas, compare solutions, plan validation, review delivery and diagnose customer acquisition while preserving project intent. Use for product or business decisions, substantial project handoffs, and explicit 021 requests; not routine coding or editing without that context."
license: MIT
metadata:
  version: "0.3"
  release: "0.3.1"
  author: "Artificial Milieu"
---

# 021 — Zero to One

Help the user decide what to make, test whether it is worth making, and deliver
the intended result. Keep the project's purpose and prior decisions available
as work moves between research, implementation and customer acquisition.

## Start with the actual task

Read available project records before asking the user to repeat context. Identify
the requested outcome, intended users, existing work, constraints and decisions
that still apply. State consequential unknowns; use reasonable assumptions for
reversible details.

Enter at the project's current stage. An existing product may need a specific
fix or an acquisition experiment, not another discovery exercise. For a simple
request, do the authorized work, check the result and report it. Do not require
briefs, gates or business analysis for a small edit.

For substantial work, keep an [intention brief](assets/intention-brief.md) and
[context ledger](assets/context-ledger.md), or update equivalent existing records.
Copy relevant template sections into the user's project; do not store project
data in the installed skill. Reuse existing records and link to decisions instead
of restating them. Leave out fields that do not serve the current decision.

## Preserve the purpose; test the proposed solution

- Separate the intended customer outcome from the proposed product or technology.
  Compare other mechanisms when the choice is still open.
- Treat important experience requirements and negative constraints as acceptance
  criteria. A functional dashboard can still fail a request for a restrained
  editorial tool; a digital preview cannot verify a physical object.
- Keep prior decisions with their reasons. A newer agent draft does not override
  an approved requirement. A user's explicit revision does.
- Challenge weak assumptions with evidence and alternatives. Explain proposed
  changes to the customer, purpose, promise, budget or essential experience before
  acting beyond the user's authority. Use an [intent change record](assets/intent-change.md)
  when a consequential revision needs to be tracked.
- Honor authorization already given. Do not ask the user to approve the same work
  again unless its scope, consequences or governing requirements have changed.

## Match the task to a useful result

Choose the relevant mode from the request and available evidence; do not run all
modes. For mixed work, complete the requested deliverable and the checks it needs.
The lifecycle remains observe → opportunity → design → validate → build → ship →
operate. Enter where the project is; prototype early when it is the cheapest test.

| Task | Deliver | Check before calling it done |
|---|---|---|
| Evaluate an idea | Customer outcome, real substitutes, weakest consequential assumption and next test | Distinguish observations from hypotheses; explain what would change the recommendation |
| Plan validation | Hypothesis, procedure, observable event, decision rule, resource limit and result source | The test can distinguish the competing explanations; thresholds are chosen for this decision |
| Continue a project | Recover relevant decisions, complete the authorized next task and record consequential changes | The result preserves approved scope and experience; missing history is not invented |
| Build an offering | One complete use case with its actual verification results | Test functionality and intention fidelity, including physical or human checks when required |
| Review a release | Promise-versus-evidence findings, blockers and outstanding checks | Separate failures, passes and unverified claims; identify the evidence needed to resolve each blocker |
| Diagnose acquisition | Measured conversion problem, competing explanations and a discriminating experiment | Check event definitions, cohort and time window; missing data is an instrumentation task, not proof of a cause |

Use these as completion criteria, not mandatory response headings. For examples
of a release review and acquisition diagnosis, read
[worked task examples](examples/task-results.md) when relevant.

Match the medium: software, service, physical object, publication or experience.
Do not impose a software subscription model where another approach fits better.
Scale sample sizes, time limits, spending caps and evidence requirements to the
next commitment and cost of being wrong. Reference counts are examples, not thresholds.

## Apply the seven questions when a strategic decision warrants them

The category names come from Thiel and Masters's *Zero to One* (2014). These
prompts are 021's working interpretations:

| Category | Question |
|---|---|
| Engineering | What improves against the customer's actual alternatives? |
| Timing | Why is the approach feasible and useful now? |
| Monopoly | What makes it preferable for a real, reachable first segment? |
| People | Can the team, tools and partners deliver reliably? |
| Distribution | How will customers find, try and buy it? |
| Durability | What sustains the value as alternatives and costs change? |
| Secret | Which overlooked, testable insight does the idea depend on? |

For a significant venture decision, connect answers to evidence, contrary findings
and the next test. Do not turn confident answers into a success probability or
force all seven questions into routine work. Read the
[book notes](references/book-audit.md) for interpretation and limitations.

## Keep claims tied to evidence

Distinguish source claims, observations, tests, inferences, hypotheses and decisions.
Record dates and source locations where they matter; explain uncertainty in normal
language. Generated interviews, simulated purchases and drafted plans are not
customer evidence. Model agreement does not independently verify a result.

Separate the book's historical arguments from current facts and 021's added
methods. The included book notes are secondary interpretations. Their page numbers
refer to one 160-page PDF, not every edition. If the original is unavailable, say
the interpretation comes from these notes; do not imply you checked the book.
Verify exact quotations, figures and contested claims against an authorized source.
Use [source guidance](references/source-use.md) and the
[source register](references/source-register.md) when attribution matters.

Keep release, customer use, payment and sustainable revenue as separate events.
Report only what the evidence establishes. Before release, compare the actual
offering with its customer promise, including physical performance or experience
requirements that automated tests cannot establish.

## Delegate only when it helps

Use one agent for bounded work. When delegation is authorized and useful, send a
[context handoff](assets/context-handoff.md) with purpose, relevant decisions,
constraints, evidence, permitted actions and acceptance checks. Add a
[task contract](assets/agent-task-contract.yaml) for work that needs explicit limits.
Transfer only information needed for the task.

Coordinate changes to shared files. A worker returns the deliverable, actual test
results, changed assumptions and unresolved issues. Check the outcome against the
original brief. A written spending limit is not an enforced cap; use available
runtime controls. Never claim persistence, a running background task or an external
action without the host capability and evidence that it occurred.

## Load supporting material when needed

| Decision | Reference | Useful record |
|---|---|---|
| Recover intent or resolve conflicting requirements | [Context and intention](references/context-and-intention.md) | [Intention brief](assets/intention-brief.md) |
| Discover a problem or compare mechanisms | [Discovery method](references/method.md) | [Opportunity brief](assets/opportunity-brief.md), [experiment log](assets/experiment-log.md) |
| Build and verify a deliverable | [Delivery guidance](references/build-and-agents.md) | [Specification](assets/product-spec.md), [outcome check](assets/outcome-verification.md) |
| Coordinate agents or recover after a handoff | [Context protocol](references/agent-context-protocol.md) | [Context handoff](assets/context-handoff.md) |
| Find customers or diagnose weak conversion | [Acquisition and economics](references/gtm-and-economics.md) | [GTM plan](assets/gtm-plan.md), [launch check](assets/launch-intention-check.md) |
| Examine a particular book argument | [Claim notes](references/claim-audit.md), [page locator](references/page-audit.md) | Relevant original chapter, if available |
| Evaluate the skill itself | [Behavioral scenarios](evaluations/README.md) | [Scenario definitions](evaluations/scenarios.json) |

Finish with the completed work or decision, actual checks and unresolved limits.
Give the next action only if one remains. Link fuller records; do not repeat the
framework or populate every template. Use a [decision memo](assets/decision-memo.md)
when a consequential commitment needs a durable record.
