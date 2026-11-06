# 021 — How to use original sources and research references

This file makes reference usage an **operating requirement** rather than an implied convenience. The goal is faithful interpretation and good decisions, not ornamental citations.

## 1. Select references by claim and decision

For each important decision or claim, ask:

1. Is this about **what the original book says**, **what happened in a particular company**, **what is currently true about the market**, or **our own proposed operating method**?
2. Which source is authoritative for that question?
3. Does the source genuinely support the conclusion, or only part of it?
4. Is its date, sample, context and scope suitable for today's decision?
5. What contrary evidence or interpretive limitation must travel with it?

Don't cite `claim-audit.md` as if it were the original book. It is an **interpretive audit** with physical-page locators. If a claim depends on exact wording, a figure or numerical example, inspect that page of the reader’s authorized copy when provided.

## 2. Reference loading matrix

| Task | Required source basis | Output consequence |
|---|---|---|
| Thiel concept summary | Original book page or explicit note that interpretation used the secondary book audit | Accurate attribution plus page reference |
| Seven-question venture screen | Book p. 114, plus project-specific evidence | Clearly distinguish author's categories from 021 fields |
| Market size / demand | Recent sources, customer data or real observations | Do not infer market size from anecdotal online posts |
| Technical requirements | Standards, product docs, reproducible fixtures, actual tests | Exact acceptance requirements and evidence |
| Product / interaction design | Current operator intention, precedent, user testing, domain rules | Preserve qualitative and negative constraints |
| GTM / price | Observed customer channels, tests and economics | Label hypotheses as unproven |
| Agent behaviour | Runtime docs, permissions, traces, test outcomes | No autonomous execution or capability claims without proof |
| Historical academic method | Primary method source (Torres / Strategyzer / Graham as appropriate) | Clearly mark as 021 addition, not Thiel instruction |

## 3. What to record

Each decision-critical evidence item should include:

```yaml
id: E-001
claim: ""
kind: "source_claim | observed | verified_test | inference | hypothesis | decision | unknown"
source_title: ""
source_author_or_owner: ""
source_date: ""
retrieved_or_observed_at: ""
location: "URL | physical PDF page | log | test file | receipt"
exact_support: "What this source actually establishes"
limitations: ""
contrary_evidence: []
used_to_decide: ""
```

Keep enough context that another agent can **verify** the claim, not merely restate it. Use links to originals; do not indiscriminately reproduce copyrighted passages.

## 4. Resolving source conflicts

- Preserve both claims with dates and scope before reconciling them.
- Do not resolve a conflict by preferring the more confident prose.
- Prefer primary, task-specific, current evidence for current questions, but do not disregard older sources when explaining an author's historical position.
- If available evidence cannot settle the issue, mark it unresolved and identify the cheapest credible test.
- Keep personal or project decisions separate from outside facts: external evidence may challenge the decision but does not silently revoke it.

## 5. Examples

**Incorrect:** "Thiel says that five customer interviews prove product-market fit." No such rule appears in *Zero to One*.

**Correct:** "Thiel emphasises starting from a small market (Thiel & Masters, 2014, reference PDF pp. 43–44). We propose five exploratory conversations as an initial 021 discovery activity; this would not itself establish product-market fit."

**Incorrect:** "Thiel says agents should run in parallel." The 2014 book did not offer a modern multi-agent orchestration architecture.

**Correct:** "021 proposes independent agent research branches as an implementation pattern, subject to current agent reliability and cost evidence."

**Incorrect:** "This launched service made £800." Unless an actual transaction and delivery record exist, this is a forecast or fabricated fact.

**Correct:** "The £800 figure is a scenario assumption; actual revenue is presently unverified."
