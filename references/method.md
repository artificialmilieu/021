# 021 method — Observe → Opportunity → Outcome → Evidence

Use with `assets/opportunity-brief.md` and `assets/experiment-log.md`. The **book's** strategic insights are documented in `references/book-audit.md`; the workflow below is **021's own implementation method**, supplemented by modern customer-discovery and experiment practices.

## Stage 0. Observe and frame

A promising source record describes a specific actor encountering a specific problem while attempting a specific job. Collect data from relevant discussion threads, customer support tickets, manual workarounds, search patterns, product reviews and interviews. Preserve dates, author/source and exact evidence location. Never treat frequency of mentions as quantified market size without appropriate sampling. An agent can collect forum observations but **cannot generate actual customer behaviour**.

**First output** (in ordinary language): "[Group] is trying to [job]; today [workaround], causing [specific cost/friction]. Evidence: [sources]. Unknown: [assumptions]."

## Stage 1. The opportunity and the secret

Ask five questions:

1. What important belief do incumbents or users hold about this job that might be wrong?
2. What evidence supports the alternative (not just an opinion)?
3. Who experiences the friction intensely and repeatedly?
4. Why isn't an existing substitute sufficient? Count "do nothing" and "hire a human" as alternatives.
5. If we solve it, what concrete outcome changes for the user?

**A secret is not a hot take.** It must affect what is built, for whom, or how it is distributed, and yield a disconfirmable prediction.

## Stage 2. Reverse-engineer the result

Define final successful customer state **without a product noun**. Work backwards through preconditions, required inputs, transformations, verification, and handoffs. Produce an outcome tree such as:

```text
USER OUTCOME: usable printed booklet
├── printed geometry and pagination are accurate
├── user can supply content without specialist tools
├── printer instructions match ordinary home equipment
├── output meets defined physical tolerance
└── recipient can assemble and use the booklet
```

When the mechanism is still open, compare alternatives such as manual service, template, browser tool, software/API, physical product, guided experience. Compare on outcome quality, time-to-prototype, variable cost, support burden, necessary data, risk and first-channel access. Avoid selecting AI just because it is available.

Define the **beachhead** by real common need, access and purchasing behaviour, not arbitrary demographic precision. For each proposed channel, identify an initial group of reachable prospects. Choose its size to suit the experiment; a count alone does not establish demand.

## Stage 3. Risk-first validation

List assumptions across:

- **Desirability:** Does the problem matter, and will users change behaviour?
- **Feasibility:** Can the promised outcome be delivered at required quality and constraints?
- **Viability:** Is there a realistic paying buyer, price, cost structure and contribution?
- **Distribution:** Can the target segment be reached and converted affordably?
- **Operational/survivability:** Can the venture legally, safely and reliably deliver over time?

Classify each by **impact if wrong** and **strength of evidence**, then test high-impact, weak-evidence assumptions first. Do not let a low-risk test generate false comfort while an existential unknown remains unresolved.

**Experiment specification:** Hypothesis | why it matters | procedure | target participants | observable event | precommitted success/fail/ambiguous rule | cost cap | end date | owner | source of results.

**Strength of evidence** is contextual. Ideas and agent-generated simulations are assumptions. Interviews and reported behaviour are useful but imperfect. Observed task completion and real paid demand can be stronger, but may still have sampling, price or novelty effects.

## Stage 4. Readiness gates

For a product to advance beyond exploration, inspect:

- **Value:** A buyer/user outcome, not just a solution description.
- **Substitutes:** The real alternatives and why one segment may prefer this.
- **Engineering:** Reproducible proof for claims critical to delivery.
- **Timing:** Why the approach is now practical and worth attempting.
- **Channel:** At least one actionable first customer acquisition method.
- **Price and costs:** Testable price hypothesis and estimated gross contribution.
- **Durability:** Reasons to return, trust or recommend; maintenance obligations.
- **Risk:** Compliance and safety constraints appropriate to domain.

Use the **original seven questions** in `SKILL.md` as an additional strategic review; don't replace them with these operational readiness checks.

## Common false positives

| False positive | Better evidence |
|---|---|
| People say 'I'd use this' | Actually try or pay under realistic conditions |
| Competitors have many users | Specific underserved customer segment and switching triggers |
| AI can generate a demo | End-to-end repeatable output verified against acceptance criteria |
| No direct competitors | Real substitutes and user workaround inspection |
| Landing page gets visitors | Qualified visitors take the intended conversion action |
| Product is '10x better' | Relevant customer outcome materially improves on a defined metric |
| One paying customer | Learn acquisition source, repeatability and economics |
| Model can act autonomously | Measured long-running success and independent verification |

## Make the next commitment explicit

When evidence affects a consequential commitment, state whether to advance, revise,
hold or stop, and why. Use `assets/decision-memo.md` only when the decision needs a
durable record; otherwise update the existing ledger or report the result briefly.
Link an existing opportunity review instead of repeating its seven questions.
A small authorized improvement does not require another investment decision.
A minimal prototype is permitted when building is the cheapest discriminating test.
Judge an experiment by what it resolves, not by the volume of activity.

## Example applications

- **Research-to-service:** Diagnose recurring complex document problems; manually provide a result to five real prospects; validate outcomes/pricing; formalise the repeatable steps; automate selectively.
- **Physical product:** Build a full-sized working object and test assembly, tolerances and instructions, not only a 3D mockup.
- **Software:** Write measurable requirements, run a bounded coding agent, reproduce tests and instrument activation before public launch.
- **Publication or experience:** Define the reader/participant transformation (learning, decision, action, enjoyment); observe repeated engagement or explicit payment rather than raw content output.

## Stage-specific source discipline

Use original book page references for ideas (see page audit) and label the new workflow 021. External methodological sources: Torres on opportunity-solution trees; Strategyzer on assumptions and experiments; Graham on manual early customer acquisition. The source register gives URLs and attribution. These authors offer complementary frameworks, not verification of Thiel's broad market claims.


## Context and intention checks by stage (021 v0.2)

- **Observe:** record who originally requested the project, their stated purpose, relevant history and explicitly rejected directions. Do not collapse a customer's job and the operator's design intention into a single sentence if both affect the outcome.
- **Opportunity:** link the proposed 'secret' to the actual job and consequences. A contrarian opinion that changes neither beneficiary, mechanism nor delivery is not enough.
- **Design:** compare candidate solutions against the desired outcome **and** qualitative experience, constraints and rationale from the `intention-brief`, not just technical feasibility.
- **Validate:** include a test for important qualitative constraints (physical assembly, actual readability, distinctiveness, customer trust), assigning qualified human review where tests cannot be automated.
- **Build:** attach the intention baseline and negative constraints to `product-spec.md` and every relevant delegated task.
- **Launch:** check promise fidelity using `assets/launch-intention-check.md` before external announcements; real product availability and revenue are separately verifiable events.
- **Learn:** proposed pivots that change beneficiary, purpose or core experience require `assets/intent-change.md` and an approved decision. Keep a rationale and baseline history so agents in future sessions can recover the original intention.

For details see `references/context-and-intention.md`. This is a new 021 operating extension, not original *Zero to One* text.
