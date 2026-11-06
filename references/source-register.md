# Source register and provenance

The principal source is Peter Thiel and Blake Masters’s *Zero to One* (2014). The book is not included. The package contains secondary interpretive notes and page locators tied to a 160-page reference PDF; pagination may differ in other editions. Consult an authorized copy for exact wording and figures. Linked sources support attribution and further reading; their inclusion is not evidence that every link or claim has been reverified for this release.

## Tier 1 — primary text

1. **Thiel, Peter, with Blake Masters** (2014). *Zero to One: Notes on Startups, or How to Build the Future*. Crown Business. The reference pagination places publication details on PDF p. 3 and contents on p. 4. **Authority:** authoritative for what the book says; NOT empirical confirmation of its claims. **Used:** argument audit, seven questions, narrow markets, timing, value capture, culture, distribution, human-computer complementarity.

## Tier 2 — original lectures and first-person explanations

2. **Blake Masters** (2012). [Peter Thiel CS183 class notes index](https://blakemasters.tumblr.com/peter-thiels-cs183-startup). Stanford lectures as recorded and edited by student Blake Masters. Masters explicitly says errors/omissions are his. **Used:** verify origins and identify distinctions between course notes and edited book; do not call the notes a word-for-word Thiel transcript.
3. **Blake Masters** (4 May 2012). [Class 9: If You Build It, Will They Come?](https://blakemasters.tumblr.com/post/22405055017/peter-thiels-cs183-startup-class-9-notes-essay). **Used:** distribution channel economics, buyer/customer lifetime value vs acquisition cost, differing sales methods and PayPal growth; numbers are 2012 historical examples.
4. **Blake Masters** (11 May 2012). [Class 11: Secrets](https://blakemasters.tumblr.com/post/22866240816/peter-thiels-cs183-startup-class-11-notes). **Used:** secrets of people/nature, false consensus, conditional disclosure, market neglect; Thiel's ideas through note-taker's account.
5. **Blake Masters** (2012). [Class 4: The Last Mover Advantage](https://blakemasters.tumblr.com/post/21169325300/peter-thiels-cs183-startup-class-4-notes-essay). **Used:** first-market and durability emphasis.
6. **Peter Thiel** (January 2011). [Interview about René Girard, Imitatio](https://www.bishoprockcap.com/assets/library/peter-thiel/January%202011%20Peter%20Thiel%20on%20Ren%C3%A9%20Girard%20%28transcript%29). **Used:** independently grounds influence of mimetic rivalry, the avoidance of duplicate responsibilities, and contrarian market selection. The linked transcription labels imperfect confidence; check the original video for contentious quotations.

## Tier 3 — methods we add to make shipping and GTM possible

7. **Teresa Torres / Product Talk**. [Opportunity Solution Trees](https://www.producttalk.org/opportunity-solution-trees/). **Used:** organising outcomes, user opportunities, solution options, experiments. Not present as such in *Zero to One*.
8. **David J. Bland / Strategyzer** (4 August 2020). [Assumptions Mapping](https://www.strategyzer.com/library/how-assumptions-mapping-can-focus-your-teams-on-running-experiments-that-matter). **Used:** prioritising high-impact claims with little evidence.
9. **Strategyzer**. [Testing Business Ideas](https://www.strategyzer.com/library/testing-business-ideas-book) and [Critical Hypotheses](https://www.strategyzer.com/library/how-to-test-your-idea-start-with-the-most-critical-hypotheses). **Used:** demand/feasibility/viability and low-cost experiments. The original tests and evidence hierarchy should not be attributed to Thiel.
10. **Paul Graham** (July 2013). [Do Things That Don't Scale](https://paulgraham.com/ds.html). **Used:** first-user recruitment, manual fulfilment, doing work on customers' behalf to discover what truly needs automating.

## Tier 4 — agent skill format and execution guidance

11. **Agent Skills project**. [Agent Skill format specification](https://github.com/agentskills/agentskills/blob/main/docs/specification.mdx). **Used:** YAML frontmatter, folder name, `SKILL.md`, relative references and progressive loading.
12. **OpenAI Developers**. [Skills API guide](https://developers.openai.com/api/docs/guides/tools-skills). **Used:** portable skill bundle with reference material and ZIP upload format; actual installation depends on client/product.
13. **OpenAI Codex**. [Skill creator guidance](https://github.com/openai/codex/blob/main/codex-rs/skills/src/assets/samples/skill-creator/SKILL.md). **Used:** concise instructions, selective reference loading, no gratuitous scaffolding or fixed rituals where flexible decisions are preferable.

## Source claims to deliberately flag

- **2014 metrics and values** (Google market share, Twitter/LinkedIn valuations, cost of acquisition, Tesla sales): historical examples; never use as present figures.
- **Monopoly welfare claims:** a viewpoint, not blanket empirical proof or legal advice.
- **Founder personality claims:** illustrations, not valid hiring assessments.
- **Human-versus-machine prediction:** compare against contemporary model testing before operationalisation.
- **Success stories:** selected retrospective illustrations and subject to survivorship bias.
- **Power law:** concentration of venture outcomes does not imply the operator should gamble personal finances.
- **GTM:** customer interviews, tracking, launch checklists and profitability gates are supplementary 021 methods.

## How to cite a 021 deliverable

- Book checked directly: `Thiel & Masters (2014), Zero to One`, with the edition and a precise page verified in that copy.
- Only included notes available: `021 book notes, interpreting Thiel & Masters (2014)`; identify the note file and treat its PDF page locator as unverified against the original.
- Earlier lecture: `Masters (2012), CS183 Class 9 Notes, May 4, URL`.
- Independent methodology: `Bland (2020), Assumptions Mapping, URL`.
- Studio norm or invention: `021 methodology — design rule`, not `Thiel says`.

Do not assert an original quote unless it has been checked against the PDF or original interview, and respect quotation/copyright limits.

## v0.2 — Context/intention and skills architecture

14. **Agent Skills open specification**. [Format specification](https://agentskills.io/specification). **Used:** required frontmatter, matching skill folder name and optional reference assets; current recommendation for progressive loading. Its suggested file lengths are **guidance**, not a substitute for complete project understanding.
15. **Anthropic engineering**. [Equipping agents for the real world with Agent Skills](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills). **Used:** progressive disclosure, agent-specific tools and contextual references; no guarantee of performance on our tasks.
16. **021 design inference**. `references/context-and-intention.md` and `references/agent-context-protocol.md`. **Used:** purpose preservation, change-control, continuity and fidelity checks. These are our proposed operating methodology, **not attributed to Thiel or Anthropic**.

