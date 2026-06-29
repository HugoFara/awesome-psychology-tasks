## Paradigm Specifications

The catalog's core is shifting from *where a task is implemented* to *what it means
to implement the paradigm correctly*. A **paradigm specification** records the
construct(s) a paradigm operationalises, its **defining contrast** (the
manipulation and the prediction that make it that paradigm and not another), the
design parameters that materially move results, and an **executable test** — a
machine-checkable definition of the contrast and scoring.

**Two independent signals, never conflated.** Read each spec on two axes:

- **Validation state** — *has a human expert reviewed the measurement claims?* Every
  spec below is **`sourced`**: literature-linked, LLM-assisted or contributor-drafted,
  and **unreviewed**. This is the honest default and already useful; it is **not**
  an endorsement. Expert review would raise it to `corroborated` / `expert-annotated`,
  or mark it `contested` — that ladder is the project's moat, and nothing here has
  climbed it yet.
- **Executable spec** — *does an implementation instantiate the contrast and scoring?*
  This is a **machine** check (a synthetic responder with a known policy is driven
  through the real task and the contrast must be encoded, scored, and recovered). A
  passing check is a genuine instrumentation guarantee — categorically stronger than
  "the link loads" — but it is **not** human validation. A green badge never raises
  the validation state.

The wall between them is deliberate and irreducible: the executable test confirms a
task is wired the way the spec says; it cannot tell you the spec is the *right*
operationalisation of the construct. That judgement stays human.

Specs and their executable contracts are produced by the paradigm-test-harness (the
catalog's executable-spec tooling) and vendored here as `data/specs.json`; this
catalog only *reads* the proven signal — it never hosts task code, stimuli, or data.
