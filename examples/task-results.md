# Two worked task examples

These are fictional inputs and illustrative responses, not research or results
from a live business. Adapt the depth to the user's decision.

## Review a release without losing the approved experience

**Request:** “Review our printable planner for release. Keep the approved calm,
single-page interface. Do not deploy.”

**Supplied evidence:** The approved brief specifies one A4 planner, two controls
and no dashboard. Export tests pass for dimensions and pagination. The current
screen adds a sidebar, metrics and eight controls. Nobody has printed or assembled
the output. The sales draft promises reliable printing on every home printer.

**Useful result:**

| Requirement | Finding | Next check or correction |
|---|---|---|
| A4 export dimensions and pagination | Pass within the supplied automated test coverage | Keep the test output with the release record |
| Calm interface with two controls | Fails the approved brief | Restore the agreed interaction, then review the actual screen against the brief |
| Usable printed planner | Unverified | Print with declared settings, check margins and usability on representative equipment |
| Reliable on every home printer | Unsupported promise | Remove the universal claim; describe only tested conditions once results exist |

**Decision:** Hold release. The export tests support a limited functional claim;
they do not resolve experience drift or physical performance. Correct those
specific gaps and repeat the affected checks. No deployment was authorized.

This review needs findings and evidence. It does not need a new opportunity brief
or another seven-question analysis. If the user changes the intended experience,
record that decision before treating the new design as approved.

## Diagnose acquisition without inventing the cause

**Request:** “People try the tool but do not buy it. Find the next useful test.”

**Supplied evidence:** A fictional 14-day cohort contains 120 qualified visitors,
24 trial starts, six completed exports and one payment. Events are deduplicated
and connected to the same cohort. Completion is recorded only on successful
export. Five support messages report confusion about the export step, but those
messages are not linked to trial events. No usability observation exists yet.

**Useful result:**

- Trial start: 24/120, or 20% of qualified visitors.
- Completed export: 6/24, or 25% of trial starters.
- Payment: 1/6 among completers; too little evidence to assign the cause to price.
- The largest observed loss after trial start is before export completion.
  Support messages suggest confusion, but technical failure and poor fit remain
  competing explanations. They are not proof of the cause.

**Next test:** Observe a small, explicitly exploratory sample of recent trial
starters attempting their real export task. With consent, capture the point of
failure and match it to export/error events. Keep the current price and promise
unchanged while investigating this step.

**Decision rule:** If observed users cannot find the export action while the
underlying export succeeds, test a focused interface correction. If export fails,
reproduce and fix the technical error first. If users complete the task but reject
the result's value, investigate fit before changing price. Mixed observations
leave the diagnosis open; this sample does not estimate market-wide prevalence.

Use the operator's available research budget and schedule. With no event access,
return the measurement needed and an explicitly provisional hypothesis. Do not
invent rates, contact customers, change the approved offer or claim this example's
figures describe the user's business.
