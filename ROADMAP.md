# Roadmap (revised)

> **Working title: Psychology Task Catalog** (public name to be decided).
> Reframed: not a directory of where tasks are implemented, but an **auditable
> map of the field's measurement claims** — for each cognitive construct, the
> competing ways it is operationalised, how well each one is known to work, and
> a machine-checkable definition of what it means to instantiate the paradigm
> correctly.

**North star — honesty about validation is the product.** An unreviewed claim
is always shown as unreviewed, never dressed up as settled. Human expert
validation is the moat: LLM-assisted generation commoditises *building* tasks
and even *drafting* specs, so the one thing a model cannot self-certify — a
human having checked a claim, and the record carrying that fact — is where the
defensible value lives. `sourced` is honest and already useful;
`expert-annotated` is the differentiator. Every decision below serves this.

This document sets out the **intentions and direction** of the project after a
strategic reframing. It is written for readers assessing how useful the
resource is to the research community. It is deliberately more opinionated than
its predecessor: the central decision behind it is that a neutral inventory is
low-value, and the value lives in judgments about measurement.

## What changed from v1, in one paragraph

The first roadmap optimised for **discoverability of implementations** — "which
Flanker tasks exist, which run in a browser, which are free." That bottleneck is
eroding from two sides at once: AI-assisted generation now produces a working
task from a plain-language description in minutes, and the taxonomy/ontology
layer is already occupied by the Cognitive Atlas and the Cognitive Paradigm
Ontology. v1's Phase 4 ("methodological depth," flagged as *exploratory, not a
commitment*) is in fact the moat; v1's Phases 1–3 are the commoditised floor.
This revision **inverts that priority**, changes the unit of curation from the
*implementation* to the *paradigm specification*, **splits the neutrality
principle**, and adds an **executable-test track** so that "this implementation
correctly instantiates the paradigm" becomes a claim a machine can check rather
than a claim a link can only assert.

## Mission

A paradigm is individuated not by its stimuli, platform, or code but by the
**inference it licenses** — the contrast it sets up and the bridge from that
contrast to a latent process. The catalog's job is to make that inferential
structure explicit, comparable, and trustworthy across the field: to let a
researcher or a reviewer see a construct, its rival operationalisations, the
evidence on whether each one measures what it claims, and where the inference is
contested — without rehosting anyone's code, stimuli, or data.

The descriptive layer (what exists, on what platform, at what cost, whether the
link loads) is the **floor**. The specification and measurement-audit layers are
the **building**.

## Principles (revised)

1. **The unit of curation is the paradigm specification, not the
   implementation.** The spec is: the construct(s) operationalised, the defining
   contrast, the design parameters that materially change the result, the known
   variants and how they differ, and the stimulus sets the paradigm depends on.
   Implementations attach to a spec as *reference instances*, annotated for how
   well they conform to it.
2. **Validation is a state, not a gate.** Every claim carries a validation
   level. Nothing is blocked waiting for the top level. Expert review *raises*
   the level; it never unblocks publication. (See the advisory model below — this
   is the structural reason psychologists can advise without becoming a time or
   funding bottleneck.)
3. **Split neutrality.** Neutral on **platforms** — open-source and commercial
   tools listed on equal terms, no crowning of jsPsych over Gorilla. Opinionated
   and sourced on **measurement quality** — refusing to say which
   operationalisations are valid is refusing to do the one thing that helps.
   v1 bundled both under one neutrality banner, which would have neutered the
   valuable half.
4. **Evidence-weighted, never falsely neutral or falsely consensual.** Where the
   literature disagrees, surface the disagreement with edges weighted by
   evidence — not "all views equal," not a manufactured consensus. **Never reduce
   a measure to a single number**: reliability and validity are population- and
   parameter-dependent, so the unit is "evidence about this measure under these
   conditions."
5. **The spec is executable.** Every paradigm carries a machine-checkable test
   definition. A passing suite is the operational meaning of "this instantiates
   the paradigm's contrast and scoring."
6. **Metadata-only, legal by design.** Describe and link; never rehost scripts,
   stimuli, or data. Data collection always happens at the source.
7. **Don't burn the floor for the ceiling.** The descriptive and platform-guide
   layers have real if modest value. The strategic failure mode is
   over-investing in them because they feel productive while being largely
   commoditised.

## The validation-state model

This is the mechanism that lets the project ship now and improve continuously
without ever putting expert availability on the critical path. Every spec field
and every measurement claim has a state:

- **`sourced`** — literature-linked; machine-extracted or contributor-entered;
  unreviewed. This is the honest default, and it is already useful.
- **`corroborated`** — cross-checked against multiple independent sources.
- **`expert-annotated`** — an advisor has reviewed it and endorsed, qualified, or
  contested it.
- **`contested`** — sources or advisors disagree; the disagreement is displayed,
  not resolved away.

Publication never waits on `expert-annotated`. An un-reviewed entry degrades to
`sourced`, which is truthful and still informative — not to "blocked." Advisors
and contributors move entries up the ladder asynchronously. Grant-funded
advisory work becomes a **continuous enrichment stream**, never a gate.

## Tracks and horizons

The project runs as parallel tracks, not a strict phase sequence. Horizons
(Near / Mid / Long / Aspirational) are marked per track.

### Track A — The descriptive floor *(Near; mostly built)*

The browsable catalog by domain and paradigm, search and filters, link health,
and the platform guide (online capability, cost, browser-RT fidelity, in-lab vs.
online trade-offs). The platform guide is the most defensible piece of the floor
and the one AI answers least cleanly — keep it. Otherwise: maintain, label
honestly as the floor, do not over-invest.

### Track B — The specification layer *(Near → Mid; the core product)*

A machine-readable schema for the paradigm-spec record, from day one. Each
record carries: the construct(s) operationalised and any contested
construct→paradigm mappings; the defining contrast; the design parameters that
materially move results, with literature-backed defaults and ranges; the known
variants and what each one measures differently; the stimulus sets it depends
on, with validation and licensing status; and canonical references. Existing
implementation links migrate here as reference instances tagged for
spec-conformance. This track is what differentiates the resource from an
ontology plus an awesome-list plus a code generator.

### Track C — Executable specs: automated task testing *(Mid → Aspirational)*

The IT/ML core, and the part most worth building well. It separates two
questions that "does this task work" silently conflates — **instrumentation
correctness** (right stimulus, right timing, RT clocked from onset, correct
scoring, balanced conditions, nothing dropped) and **psychological validity**
(does it elicit the effect, at the right size, with adequate reliability) — and
gives each its own oracle.

- **C1 — Synthetic responders + property-based testing** *(Mid; highest ROI).*
  Deterministic agents with fully known policies, asserted against what the real
  pipeline logs: an *oracle* (always correct, fixed RT) to catch RT-clock and
  scoring bugs; an *anti-oracle* (responds to the distractors) to prove the
  manipulation is actually encoded and scored; *lapse* and *fast-guess* agents
  for missing/anticipatory responses; an *effect-injecting* agent (e.g. +50 ms on
  incongruent trials) pushed through the *real* analysis to confirm the pipeline
  recovers the effect end-to-end. Plus fuzzing over the design space (trial
  counts, timings, set sizes) to assert structural invariants. Because the ground
  truth is the agent's known policy, a failure localises to the task rather than
  to a black box. This is the direct answer to "testing is tedious."

- **C2 — Generative-model parameter recovery** *(Mid).* Generate data from
  interpretable process models (drift-diffusion, reinforcement-learning,
  Bayesian-observer) with known parameters, run it through the real logging and
  analysis, and check the parameters come back. Catches under-powered designs,
  confounds, and analysis bugs against true ground truth. Interpretable
  generators specifically, because their parameters *are* the quantities being
  recovered — neural nets are worse here, since their weights are not
  psychological quantities.

- **C3 — Perception nets and stimulus parsers** *(Long; Aspirational).* A small
  vision model that asserts the rendered canvas matches the spec (a left arrow
  flanked by right arrows, correct colour, size, position) — the natural and
  otherwise-untestable defence against silent rendering bugs from CSS, fonts,
  scaling, or colour profiles. Plus a stimulus parser so a synthetic responder
  can know the ground-truth correct answer for arbitrarily generated
  high-dimensional stimuli. Both are instrumentation helpers, **not** human
  models.

The payoff for the catalog: a passing suite **is** the executable form of the
spec. A catalog badge meaning *"verified to instantiate this paradigm's contrast
and scoring"* is categorically stronger than *"the link loads,"* and nobody
currently offers it.

> Explicitly out of scope, and why: training a network to *simulate a human* and
> "testing" a task by checking the net reproduces the effect is circular — it
> shows only that task and model share assumptions, and a shared flaw passes with
> the task still broken. The fashionable LLM-as-participant variant inherits the
> same circularity plus training contamination. Fine as a smoke test that a task
> runs and emits parseable data; useless for validity. Do not let it creep into
> Track D.

### Track D — The measurement-audit layer *(Mid → Long; primary advisory surface)*

Reliability, validity, replication status, and typical effect sizes — recorded
as *evidence under stated conditions*, never as headline numbers. The
validation-state model applies most heavily here. The reliability paradox is the
worked example: a paradigm that produces a robust group-level effect can have
poor test–retest reliability for individual differences, which silently
invalidates the inference most people reach for it to make; the catalog should
surface that *at the point of task selection*.

Aspirational ML: assisted extraction of psychometric claims from the literature
(NLP over methods and results sections) to seed the `sourced` state at scale.
Honest flag — extraction will be wrong often; it **seeds, it does not
adjudicate**, and its output must enter at the lowest validation state only.
This is the primary place advisors plug in: review raises `sourced` →
`expert-annotated` or marks `contested`.

### Track E — Community, governance, interoperability *(Long)*

A reviewed contribution flow keyed to the validation-state model, so that
contributions and advisor reviews compose rather than collide. Visible
contributor recognition. Interoperability and machine-readable export to and
from the Cognitive Atlas, OSF, RDoC, and the Cognitive Paradigm Ontology — and
the executable spec (Track C) as a portable artifact others can run against their
own implementations.

## The advisory model: psychologists as advisors, never gating

Wherever the previous roadmap said a phase "requires expert validation before
publication," that dependency is removed and replaced by the validation-state
ladder. Advisors review and annotate; their work moves entries up the ladder.
Their *absence* degrades an entry to `sourced` / unreviewed — honest and still
useful — never to "blocked."

Consequences by design:

- The build and publish path **never** waits on recruiting, scheduling, or
  funding experts.
- Grant-funded advisory work attaches to **Track D** (and optionally the C2/C3 ML
  work), as enrichment, off the critical path. A future grant therefore *adds*
  capacity; its absence or delay does not stall the project.
- An advisory board's role is to weight edges and arbitrate `contested` entries,
  not to approve releases.

## Horizon summary

| Track | Near | Mid | Long | Aspirational |
| --- | --- | --- | --- | --- |
| A — Descriptive floor | ● |  |  |  |
| B — Specification layer | ● | ● |  |  |
| C — Executable testing | C1 | C1/C2 | C3 | C3 |
| D — Measurement audit |  | ● | ● | NLP extraction |
| E — Community / interop |  |  | ● |  |

## What this is not

- **Not a hosting or data-collection platform**, and **not a rehoster.** It
  describes and links; it never runs studies, stores participant data, or copies
  scripts or stimuli.
- **Not a ranking of platforms.** Platform-neutrality is a standing commitment.
- **But it is, deliberately, an opinionated and sourced assessment of measurement
  quality.** That asymmetry — neutral on tools, opinionated on measures — is the
  point, not an oversight.
- **Not a single-number authority.** No "Flanker reliability = X." Measurement
  claims are always conditioned and evidence-weighted.
- **Not a substitute for human judgment of construct validity.** See limits.

## Honest limits and risks

- **The task-versus-construct wall stays human.** Everything in Track C tests an
  implementation against its spec. None of it tells you the spec is the *right*
  operationalisation of the construct. That gap is irreducible and is exactly
  where advisors matter most.
- **Doing the measurement layer badly is worse than not doing it.** A
  confidently-wrong reliability number actively misleads. The validation-state
  model and the "evidence under conditions" framing are the mitigations; they are
  not optional polish.
- **Over-investing in the floor (Track A)** is the most likely strategic failure
  — it feels productive and is largely commoditised.
- **Automated extraction (Track D ML) will be frequently wrong** and must only
  ever seed the lowest validation state.

## Open questions for review

- **Schema.** What is the minimal paradigm-spec record that is both
  machine-checkable (for Track C) and honest about contested
  construct→paradigm mappings (for Track D)?
- **How loud, how early.** *Settled by the north star:* `sourced`-only claims
  may be surfaced but always render as explicitly unreviewed — opinion is
  permitted, masquerading as settled is not. *Open:* the exact UI treatment
  that makes the unreviewed state unmissable without burying the still-useful
  content.
- **Governance of contested edges.** Who can mark an entry `contested`, and how
  is that arbitrated without quietly recreating a gate?
- **First vertical.** Which paradigm is built end-to-end first as the reference
  exemplar of the whole stack? The Flanker is the obvious candidate — heavily
  studied, the reliability-paradox poster child, and trivial to drive with
  synthetic responders — making it the cleanest demonstration that the spec, the
  executable test, and the measurement audit all hang together.
