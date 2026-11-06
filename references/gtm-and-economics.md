# 021 GTM and revenue operations

The original book treats distribution as strategic and frequently overlooked (reference PDF pp. 95–103), while its 2012 lecture notes also discuss customer acquisition math and channel economics. This file is 021's **added operational method**, not a verbatim Thiel GTM playbook.

## Rule: distribution hypothesis before expensive build

For a substantial build commitment, address the relevant items below. Adapt example prospect counts to the decision; they are not statistical thresholds:

**Buyer** — Who authorises payment? User and buyer may differ. **Job** — Why will they care now? **Trigger** — What event makes them search for help? **Substitute** — What do they do without us? **Promise** — What specific result can we honestly deliver? **First channel** — Where are the first 10–25 qualified buyers? **Conversion step** — What action do we ask them to take? **Price hypothesis** — How much and why? **Friction** — What prevents initial trial or purchase?

An example: "Independent designers who just exported generative artwork from a model and have a print deadline. Trigger: print-shop file rejection. First channel: direct contact with relevant print communities and pilot participants. Conversion: paid verification + fix, with clear scope. Verify demand and costs before claiming product-market fit."

## The first customer path

1. **Identify a beachhead:** real narrow cohort with urgent repeated job and reachable distribution.
2. **Make an offer:** one buyer, one result, clear scope, realistic price and deliverable.
3. **Recruit manually:** contact appropriate prospects individually and transparently; no spam or impersonation by agents. Ask permission for interviews and beta trials.
4. **Convert first use:** reduce unnecessary onboarding, verify the job completed, keep a record of failures.
5. **Deliver and observe:** collect actual time-to-result, completion, support requests, refunds and willingness to return.
6. **Ask for payment appropriately:** a transaction is evidence about that buyer at that price, not universal demand.
7. **Retain / refer / expand:** improve value, monitor repeated purchasing or use, then test adjacent segments.

## Funnel and operational instrumenting

Track events suited to the venture medium:

```text
qualified_prospect
  → contacted/visitor
  → meaningful_engagement
  → first_attempt / trial
  → successful_outcome (activation)
  → purchase or contract
  → successful_fulfilment
  → repeat_use / renewal / referral
```

For a one-off product, `purchase` may precede fulfilment and activation. For services, `qualified_prospect → discovery → quote → agreement → delivery → rehire`. For a publication, email signup is not automatically revenue. Define each event and data source before measuring a rate; don't infer denominators or invent conversion numbers.

## Channel strategy by price and behaviour

| Offer | Candidate first channels | Crucial constraint |
|---|---|---|
| Low-price consumer digital product | Search intent, owned audience, relevant communities, cross-promotion | Paid ads may exceed order contribution |
| Productised B2B service | Direct personal outreach, referrals, relevant professional communities | Founder time in conversations and fulfilment |
| Mid/high-ticket business workflow | Demonstrations, case evidence, direct sales, founder-led pilots | Long purchasing cycles and trust |
| Subscription software | Niche content, integrations, targeted outreach, product-led trials | Retention, activation, support, churn |
| Physical object | Targeted creative audience, demos, retail partnerships where economical | Materials, shipping, returns and fulfilment |
| Publication or experience | Editorial distribution, events, partnerships, communities | Engagement alone may not generate buyers |

Choose one principal channel hypothesis before spreading effort across several. Test other channels when the first fails or reveals clear constraints. The original book's distribution power law is a provocation, not proof that exactly one channel always succeeds.

## Pricing and unit economics

For an individual order:

`Contribution per order = Net collected revenue - variable delivery costs - transaction/fulfilment costs - attributable acquisition cost`.

For subscriptions: inspect monthly gross contribution, renewal, churn, support hours and acquisition spend; **LTV is uncertain early**. For services: record direct labour (including your own hours), subcontractors, tools, revision cycles and post-delivery support. For an AI agent-heavy product: log model/tool spending across retries and the time required to verify outputs.

For studio portfolio: count shared cost once. Track **revenue, variable costs, CAC (where measurable), verified outcomes, founder review hours, refunds, ongoing support and setup time**. Do not produce profitability claims by excluding owner labour and operating obligations without saying so.

Use no default magic ratios (e.g. 3:1 LTV:CAC) as gates across all venture categories. It is acceptable to use modelled assumptions, but label them, show sensitivity and update with observed data.

## GTM plan checklist

- Clear offer and customer outcome with limits and honest proof.
- Defined first customer cohort and reachable contact plan.
- Price, payment mechanism and terms; locally appropriate legal/tax review where needed.
- Working landing/checkout/booking/request path.
- Onboarding/usage instructions and support escalation.
- Measured conversion events and privacy-respecting analytics.
- Capacity to deliver, refunds and post-sale support.
- Evidence of shipping (URL, test, receipt, deployed version as appropriate).
- Follow-up schedule for real customers, review of failure modes.
- Stage-based review: launch, activation, first sale, repeat use, financial viability.

## What to do when something fails

First check how the relevant events were recorded: the cohort, time window,
denominators and whether events can be connected to the same people. A large
drop-off identifies where to investigate; it does not establish why it happened.
Separate observed events from explanations, then choose a test that could change
the diagnosis. If events are missing, define the measurement before claiming a
conversion rate. Compare with the [worked diagnosis](../examples/task-results.md).

| Observed bottleneck | Next action |
|---|---|
| No qualified traffic | Recheck reachable market, search intent, channel and positioning; don't rebuild product yet |
| Engagement but no trials | Examine unclear promise, friction and credibility |
| Trial without activation | Fix the outcome workflow, onboarding, correctness and support |
| Activation without purchase | Investigate buyer, price, budget authority and alternatives |
| Sales with low contribution | Reduce fulfilment costs, revise pricing/scope or stop uneconomic delivery |
| Purchase without return | Check whether the job is intrinsically infrequent; measure referrals/satisfaction appropriately |
| Agents produce lots of content but no customers | Redirect to qualified distribution experiments; stop measuring output volume |

## Book-to-GTM trace

- **PDF pp. 18, 43–44, 100–102:** PayPal's pivot, niche selection, eBay PowerSellers and virality are historical cases. Incentive spending is not a default growth prescription.
- **PDF pp. 95–103:** Sales and channel strategy are necessary, not optional; sales method follows deal economics.
- **PDF pp. 120, 124–125:** Better Place as distribution failure and Tesla's direct-sales strategy are contrasted; retrospective examples are not universal causal proofs.
- **2012 CS183 Class 9 lecture notes:** Adds acquisition mathematics, first-channel distinctions and further narrative context; lecture notes are Blake Masters's interpretation, not the same text as the book.

## Complementary sources

Paul Graham, *Do Things That Don't Scale* (2013), recommends manual first-user recruitment and unusually attentive delivery. Strategyzer's *Testing Business Ideas* approach prioritises assumptions with weak evidence and large consequences. Cite each distinctly. See `references/source-register.md`.


## Promise-to-delivery consistency (021 v0.2)

GTM is an extension of product intention, not a stage where an autonomous agent may invent a new user, value proposition or unrestricted promise to improve conversion. Before publishing or directly sending sales materials, reconcile each substantive claim against real capability and the approved intention baseline using `assets/launch-intention-check.md`. A customer promise change that affects the business model or outcome is a material intent revision requiring operator approval. Record product shipped, offer discoverable, buyer contacted, user activated, payment received and repeat value as distinct events with original evidence.

If a conversion experiment suggests a new segment, investigate it as a hypothesis, rather than immediately rewriting the venture purpose. If the operator approves the change, preserve the previous rationale in the context ledger and update specifications, customer terms, acceptance criteria and agent packets together.
