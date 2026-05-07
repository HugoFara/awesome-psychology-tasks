# Awesome Psychology Tasks [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated list of experimental psychology tasks and paradigms, the platforms to run them, and the repositories where you can find ready-made implementations.

## Contents

- [Choosing a Platform](#choosing-a-platform)
- [Platforms & Frameworks](#platforms--frameworks)
  - [Open Source](#open-source)
  - [Commercial / Freemium](#commercial--freemium)
  - [Survey & Clinical Tools](#survey--clinical-tools)
  - [Hosting & Backend Services](#hosting--backend-services)
- [Platform Limitations & Gotchas](#platform-limitations--gotchas)
- [Repositories & Collections](#repositories--collections)
- [Tasks by Cognitive Domain](#tasks-by-cognitive-domain)
  - [Attention](#attention)
  - [Memory](#memory)
  - [Executive Function](#executive-function)
  - [Decision Making](#decision-making)
  - [Perception](#perception)
  - [Language](#language)
  - [Social Cognition](#social-cognition)
  - [Learning](#learning)
  - [Emotion](#emotion)
  - [Creativity](#creativity)
  - [Metacognition](#metacognition)
  - [Motor Control](#motor-control)
  - [Numerical Cognition](#numerical-cognition)
  - [Developmental](#developmental)
  - [Clinical / Screening](#clinical--screening)
- [Contributing](#contributing)
- [Acknowledgments](#acknowledgments)
- [License](#license)

---

## Choosing a Platform

A quick decision tree for common scenarios:

- **Need lab-quality timing + EEG/fMRI triggers?**
  → [PsychoPy](https://www.psychopy.org) (free) or [E-Prime](https://pstnet.com/products/e-prime/) (paid)
- **Need online + no coding?**
  → [Gorilla](https://gorilla.sc) (paid) or [lab.js](https://lab.js.org) + [MindProbe](https://mindprobe.eu) (free)
- **Need a ready-made validated task library?**
  → [Inquisit](https://www.millisecond.com) (909 tasks, paid) or [Labvanced](https://www.labvanced.com) (600+ templates, freemium)
- **Need free + flexible + can code JavaScript?**
  → [jsPsych](https://www.jspsych.org) + [Cognition.run](https://www.cognition.run) or [JATOS](https://www.jatos.org)
- **On a tight budget with no coding skills?**
  → [PsyToolkit](https://www.psytoolkit.org) or [OpenSesame](https://osdoc.cogsci.nl) + [MindProbe](https://mindprobe.eu)
- **Need multiplayer / interactive experiments?**
  → [oTree](https://www.otree.org) (game theory) or [Empirica](https://empirica.ly) (real-time)
- **Need to run PsychoPy experiments online?**
  → [Pavlovia](https://pavlovia.org) (the official route, paid per participant)
- **Need clinical / validated assessment batteries?**
  → [NIH Toolbox](https://www.healthmeasures.net/explore-measurement-systems/nih-toolbox) (iPad app) or [Inquisit](https://www.millisecond.com)

---

## Platforms & Frameworks

Software for creating and running psychology experiments.

**Legend** — Status: 🟢 Active (regular updates) · 🟡 Maintained (occasional updates) · 🔴 Legacy/Abandoned — Timing: Lab (<1 ms, desktop) · Good (~1 ms, desktop) · Browser (~10–16 ms)

### Open Source

| Platform | Description | Language / Tech | Online | Status | Timing | Pricing |
|----------|-------------|-----------------|--------|--------|--------|---------|
| [jsPsych](https://www.jspsych.org) | Plugin-based JavaScript framework for browser-based behavioral experiments. | JavaScript | Yes (native) | 🟢 | Browser | Free |
| [PsychoPy](https://www.psychopy.org) | Full-featured experiment builder with graphical Builder and Python Coder views. Exports to JS via PsychoJS. | Python; JS (PsychoJS) | Via Pavlovia | 🟢 | Lab (desktop) / Browser (online) | Free |
| [lab.js](https://lab.js.org) | Drag-and-drop visual experiment builder that runs in the browser. Exports to JATOS, Open Lab, Pavlovia. | JavaScript | Yes (native) | 🟢 | Browser | Free |
| [OpenSesame](https://osdoc.cogsci.nl) | Graphical experiment builder with Python inline scripting. Online via OSWeb + JATOS. | Python; JS (OSWeb) | Partial (OSWeb) | 🟢 | Good (desktop) / Browser (online) | Free |
| [oTree](https://www.otree.org) | Framework for interactive/multiplayer experiments, strong in game theory and economics. | Python (Django); JS | Yes | 🟢 | Browser | Free |
| [Empirica](https://empirica.ly) | Platform for real-time multiplayer behavioral experiments. | JavaScript (React) | Yes | 🟢 | Browser | Free |
| [TaskBeacon](https://github.com/TaskBeacon) | Community-driven platform for sharing and standardizing psychological paradigms. AI-assisted experiment generation. | Python (PsychoPy); TypeScript (jsPsych) | Yes (psyflow-web) | 🟢 | Browser / Lab | Free |
| [psychTestR](https://pmcharrison.github.io/psychTestR/) | R package for behavioral experiment interfaces, strong in adaptive testing. | R (Shiny) | Yes (Shiny) | 🟡 | Browser | Free |
| [PEBL](https://pebl.sourceforge.net) | Cross-platform experiment building language with a 100+ test battery included. Now supports WebAssembly. | Custom language (SDL) | Partial (WASM) | 🟡 | Good (desktop) | Free |
| [Pushkin](https://github.com/pushkin-consortium/pushkin) | Platform for large-scale citizen-science online psychology experiments. | JS (React/Node); Docker | Yes | 🟡 | Browser | Free |
| [Tatool Web](https://www.tatool.ch) | Framework for cognitive training and experimental tasks with a built-in task library. | JavaScript (AngularJS) | Yes | 🟡 | Browser | Free |
| [Collector](https://github.com/gikeymarcia/Collector) | Web-based experiment platform using spreadsheet-like trial definitions. | PHP, JS, MySQL | Yes | 🔴 | Browser | Free |

### Commercial / Freemium

| Platform | Description | Language / Tech | Online | Status | Timing | Pricing |
|----------|-------------|-----------------|--------|--------|--------|---------|
| [Gorilla](https://gorilla.sc) | Cloud-based drag-and-drop experiment builder with participant recruitment integration. | Web GUI; JS/HTML/CSS | Yes | 🟢 | Browser | Free to build; ~£1/participant (token system) |
| [Pavlovia](https://pavlovia.org) | Hosting platform integrated with PsychoPy. Supports PsychoJS, jsPsych, and lab.js experiments. | Web platform; JS | Yes | 🟢 | Browser | ~€1/participant (credit system) or ~£1,800/yr institutional |
| [Inquisit (Millisecond)](https://www.millisecond.com) | Precise psychological measurement software (v7) with a 900+ test library. Desktop and web versions. | Proprietary scripting | Yes (Inquisit Web) | 🟢 | Lab (desktop) / Browser (web) | License (quote-based, academic pricing available) |
| [E-Prime](https://pstnet.com/products/e-prime/) | Widely used in lab-based cognitive/neuro research. Precise timing, EEG/fMRI integration. | E-Basic (VB-like) | Limited (E-Prime Go) | 🟢 | Lab (desktop) | License ~$1,000+ |
| [PsyToolkit](https://www.psytoolkit.org) | Free toolkit for online experiments and surveys with a built-in experiment library. | Custom scripting | Yes | 🟢 | Browser | Free |
| [Testable](https://www.testable.org) | Web-based experiment platform with a graphical editor and template library. | Web GUI; JS | Yes | 🟢 | Browser | Free tier; $299–699/yr academic |
| [FindingFive](https://www.findingfive.com) | Cloud platform using a grammar-based study design approach. Nonprofit (501(c)(3)). | JSON-like grammar | Yes | 🟢 | Browser | Free to build; $0.75/participant |
| [Labvanced](https://www.labvanced.com) | No-code experiment builder with 600+ templates. Supports webcam eye-tracking. | Web GUI (proprietary) | Yes | 🟢 | Browser | Free tier; $69–299/mo paid |
| [Cognition.run](https://www.cognition.run) | Hosting platform for jsPsych experiments with automatic data collection and AI experiment generation. | Hosts jsPsych / JS | Yes | 🟡 | Browser | Freemium |

### Survey & Clinical Tools

| Platform | Description | Online | Pricing |
|----------|-------------|--------|---------|
| [Qualtrics](https://www.qualtrics.com) | Survey platform widely used for questionnaire-embedded RT tasks and branching logic in psychology. | Yes | Institutional license |
| [REDCap](https://www.project-redcap.org) | Secure web application for building and managing online surveys and databases, common in clinical psychology research. | Yes | Free (institutional) |
| [NIH Toolbox](https://www.healthmeasures.net/explore-measurement-systems/nih-toolbox) | Validated neurobehavioral assessment battery (7 cognition tests). Administered via iPad app. Ages 3–85. | iPad app | License fee |

### Hosting & Backend Services

| Service | Description | Hosts Experiments From |
|---------|-------------|------------------------|
| [JATOS](https://www.jatos.org) | Open-source server for managing and running online experiments. | jsPsych, lab.js, OSWeb, PsychoJS, any HTML/JS |
| [MindProbe](https://mindprobe.eu) | Free JATOS-based hosting by the European Society for Cognitive Psychology (ESCoP). | jsPsych, lab.js, OSWeb, PsychoJS |
| [Open Lab](https://open-lab.online) | Free platform for hosting and sharing lab.js and jsPsych experiments. ⚠️ Site currently returning errors (Mar 2026); [source](https://github.com/Yury-Shevchenko/openlab) still available. | lab.js, jsPsych |
| [Cognition.run](https://www.cognition.run) | Free hosting with simple upload and CSV data download. | jsPsych, lab.js |

---

## Platform Limitations & Gotchas

Honest notes to help you avoid common pitfalls.

- **PsychoPy → Pavlovia**: The Python-to-JavaScript auto-translation (PsychoJS) is the most complained-about issue in PsychoPy forums. Not all Python components translate correctly — test online early and often.
- **Gorilla**: Per-participant token pricing (~£1/token) adds up at scale. A 200-participant Prolific study costs ~£200 in platform fees alone, on top of participant payment. Institutional site licenses can reduce costs.
- **jsPsych**: Requires self-hosting unless you use [Cognition.run](https://www.cognition.run) (free) or [JATOS](https://www.jatos.org). No built-in graphical editor — you write JavaScript.
- **E-Prime**: Desktop-only for full functionality. E-Prime Go (online) is significantly more limited than the desktop version. Locked to Windows. Expensive license.
- **Browser timing**: All browser-based platforms share a fundamental limitation — display refresh (~16 ms at 60 Hz) caps visual timing precision. For most RT-based research this is fine, but for tachistoscopic presentation or sub-millisecond timing, use desktop software.
- **OpenSesame → OSWeb**: Not all OpenSesame features work in the OSWeb (browser) backend. Check the [OSWeb compatibility list](https://osdoc.cogsci.nl/4.0/manual/osweb/) before designing for online use.
- **Inquisit**: The 909-task library is a major draw, but requires a paid license even to preview scripts. Web version timing is less precise than the desktop client.
- **PEBL**: Development has slowed considerably, though v2.3 added WebAssembly support. The 100+ test battery remains useful but documentation is thin.
- **Tatool Web**: Built on AngularJS 1.x. Still receives occasional updates but not actively developed. Best for cognitive training paradigms it was designed for.
- **Labvanced**: Powerful no-code editor, but the proprietary format means you can't easily export experiments to other platforms.
- **PsyToolkit**: Great for teaching and quick studies, but the custom scripting language has a learning curve and limited flexibility compared to jsPsych or PsychoPy.
- **Pavlovia**: Credits cost ~€1/participant. Use "piloting mode" to test without consuming credits. Institutional licenses (~£1,800/yr) can be more economical for high-volume labs.
- **oTree**: Excellent for game theory and multiplayer experiments, but its Django-based architecture is heavier than needed for simple single-participant tasks. The new OTAI feature (AI-powered app builder) is experimental.
- **FindingFive**: The JSON-like grammar is unique but has a learning curve. At $0.75/participant it's affordable, but the format is not portable to other platforms.

---

## Repositories & Collections

Where to find ready-made experiment implementations.

| Collection | Platform | Approx. Tasks | Description |
|------------|----------|---------------|-------------|
| [Millisecond Test Library](https://www.millisecond.com/download/library/) | Inquisit | 909 | Largest single library — covers nearly all domains of psychology. Browsable by [category](https://www.millisecond.com/download/library/). |
| [Labvanced Templates](https://www.labvanced.com/content/research/en/tasks/) | Labvanced | 600+ | Pre-loaded templates across cognitive, developmental, and behavioral economics. |
| [Pavlovia Explore](https://pavlovia.org/explore) | PsychoPy/jsPsych/lab.js | Thousands | Public experiments shared by the community on Pavlovia's GitLab. |
| [Gorilla Open Materials](https://app.gorilla.sc/openmaterials) | Gorilla | Hundreds | Open-access experiments, tasks, and questionnaires. Clone directly into your Gorilla project. |
| [E-Prime Experiment Library](https://support.pstnet.com/hc/en-us/categories/115000077168) | E-Prime | 150+ | Ready-to-run experiments across core domains. |
| [PEBL Test Battery](https://pebl.sourceforge.net) | PEBL | 100+ | Built-in battery of cognitive tests. |
| [The Experiment Factory](https://expfactory.github.io/experiments/) | jsPsych/Docker | 80+ | Reproducible web-based experiments in Docker containers. [Individual repos](https://github.com/expfactory-experiments). |
| [PsyToolkit Experiment Library](https://www.psytoolkit.org/experiment-library/) | PsyToolkit | 50+ | Free library of classic cognitive experiments — runnable in-browser with source code. |
| [Testable Library](https://www.testable.org/library) | Testable | 50+ | Ready-made classic experiment templates. |
| [jsPsych Contrib](https://github.com/jspsych/jspsych-contrib/tree/main/packages) | jsPsych | 30+ plugins | Community-contributed plugins and extensions (RDK, Corsi blocks, flanker, etc.). |
| [jsPsych Experiment Demos](https://github.com/jspsych/experiment-demos) | jsPsych | Demos | Full example experiments from the jsPsych team. |
| [Niv Lab jsPsych Demos](https://nivlab.github.io/jspsych-demos/) | jsPsych | Demos | Complete task implementations ([two-step](https://nivlab.github.io/jspsych-demos/tasks/two-step/experiment.html), [bandit](https://nivlab.github.io/jspsych-demos/tasks/3arm/experiment.html), etc.) with live interactive demos. |
| [PsychoPyParadigms](https://github.com/djangraw/PsychoPyParadigms) | PsychoPy | Varies | Community collection of PsychoPy experiment implementations. |
| [NCMlab/CognitiveTasks](https://github.com/NCMlab/CognitiveTasks) | Various | Varies | Cognitive assessment tasks with GUIs. |
| [TaskBeacon Tasks](https://github.com/TaskBeacon) | PsychoPy / jsPsych | Growing | Standardized paradigms (BART, Go/No-Go, Stop-Signal, AX-CPT, MID, Emotional Dot Probe, etc.) with structured formats. |
| [APA Online Psychology Lab](https://opl.apa.org) | Web-based | Dozens | Peer-reviewed interactive experiments for teaching. |

### Collaborative Replication Projects

| Project | URL | Description |
|---------|-----|-------------|
| [Many Labs 1](https://osf.io/wx7ck/) | OSF | 13 classic effects replicated across 36 labs. |
| [Many Labs 2](https://osf.io/8cd4r/) | OSF | ~28 effects replicated across 100+ labs in 20+ countries. |
| [Psychological Science Accelerator](https://psysciacc.org) | psysciacc.org | Global network of 1,000+ researchers conducting large-scale collaborative studies. |

### Data Repositories

| Repository | URL | Description |
|------------|-----|-------------|
| [Databrary](https://databrary.org) | databrary.org | Digital data library for video/audio behavioral research data (access-controlled). |
| [Open Science Framework](https://osf.io) | osf.io | General-purpose repository for research materials, data, and preprints. |

---

## Tasks by Cognitive Domain

In the **Implementations** column, abbreviations link to ready-made versions:
**[PT]** = [PsyToolkit](https://www.psytoolkit.org/experiment-library/) · **[Ms]** = [Millisecond/Inquisit](https://www.millisecond.com/download/library/) · **[EF]** = [Experiment Factory](https://github.com/expfactory-experiments) · **[Go]** = [Gorilla Open Materials](https://app.gorilla.sc/openmaterials) · **[Pv]** = [Pavlovia](https://pavlovia.org/explore) · **[jP]** = [jsPsych demos](https://github.com/jspsych/experiment-demos) · **[TB]** = [TaskBeacon](https://github.com/TaskBeacon)

### Attention

| Task | Description | Key Reference | Implementations |
|------|-------------|---------------|-----------------|
| Attention Network Test (ANT) | Combines Flanker with cue conditions to independently measure alerting, orienting, and executive attention networks. | Fan et al., 2002 | [PT](https://www.psytoolkit.org/experiment-library/ant.html) · [Ms](https://www.millisecond.com/download/library/ant/) · [Pv](https://pavlovia.org/AdrianaChachi/the-attention-network-task) |
| Attentional Blink | Detect two targets in a rapid serial visual presentation (RSVP) stream. The second target is often missed at 200–500 ms lag. | Raymond, Shapiro, & Arnell, 1992 | [PT](https://www.psytoolkit.org/experiment-library/ab.html) · [Ms](https://www.millisecond.com/download/library/attentionalblink/) |
| Choice Reaction Time | Press one of several keys depending on which stimulus appears. RT scales with number of alternatives (Hick's law); measures speed of stimulus-response selection. | Hick, 1952 | [PT](https://www.psytoolkit.org/experiment-library/deary_liewald.html) · [Pv](https://pavlovia.org/demos/choicertt) |
| Continuous Performance Task (CPT) | Respond to infrequent targets in a sustained stimulus stream. Measures vigilance and impulsivity. | Rosvold et al., 1956 | [PT](https://www.psytoolkit.org/experiment-library/mackworth.html) · [Ms](https://www.millisecond.com/download/library/cpt/) · [Pv](https://pavlovia.org/Khojah/continuousperformancetest) |
| Dichotic Listening | Different messages to each ear; shadow one. Measures selective auditory attention. | Cherry, 1953 |  |
| Dual-Task Paradigm | Perform two tasks simultaneously. Performance costs reveal capacity limits and attentional resource allocation. | Pashler, 1994 | [PT](https://www.psytoolkit.org/experiment-library/prp.html) |
| Eriksen Flanker Task | Respond to a central target flanked by congruent or incongruent distractors. Measures focused attention and response conflict. | Eriksen & Eriksen, 1974 | [PT](https://www.psytoolkit.org/experiment-library/flanker.html) · [Pv](https://pavlovia.org/Amandi/children-flanker-task) |
| Exogenous vs. Endogenous Cueing | Compare peripheral flash (reflexive) vs. central arrow (voluntary) cues to separate reflexive from voluntary orienting. | Jonides, 1981 | [PT](https://www.psytoolkit.org/experiment-library/endo_exo_cueing.html) |
| Global/Local (Navon) Task | Identify the global or local level of hierarchical stimuli (large letter made of small letters). | Navon, 1977 | [PT](https://www.psytoolkit.org/experiment-library/navon.html) · [Pv](https://pavlovia.org/demos/navon_task) |
| Inattentional Blindness | Failure to notice an unexpected stimulus during an attention-demanding primary task. | Simons & Chabris, 1999 | [Pv](https://pavlovia.org/hanzh/recent-probe-task-2) |
| Inhibition of Return (IOR) | Posner cueing variant with long intervals — slower RTs at previously cued locations. | Posner & Cohen, 1984 | [PT](https://www.psytoolkit.org/experiment-library/ior.html) · [Ms](https://www.millisecond.com/download/library/ior/) |
| Multiple Object Tracking (MOT) | Track a subset of moving objects among identical distractors. Measures attentional capacity across space and time. | Pylyshyn & Storm, 1988 |  |
| Negative Priming | Respond to a target that was a distractor on the preceding trial. Slowed RTs reflect lingering inhibition of previously ignored stimuli. | Tipper, 1985 | [PT](https://www.psytoolkit.org/experiment-library/negative_priming.html) · [Ms](https://www.millisecond.com/download/library/negativepriming/) |
| Posner Cueing Task | Spatial cue (valid/invalid) precedes a target. Measures covert attentional orienting and disengagement. | Posner, 1980 | [PT](https://www.psytoolkit.org/experiment-library/cueing.html) · [Pv](https://pavlovia.org/yuki0922/posnerfortry) |
| Psychological Refractory Period (PRP) | Two stimuli at varying SOAs each require a response. RT2 increases at short SOAs, revealing a central processing bottleneck. | Telford, 1931 | [PT](https://www.psytoolkit.org/experiment-library/prp.html) |
| Rapid Visual Information Processing (RVP) | Detect target sequences (e.g., three consecutive odd numbers) in a pseudo-random digit stream. Measures sustained visual attention. | Sahakian & Owen, 1992 | [Pv](https://pavlovia.org/david.smailes/rvip) · [GitHub](https://github.com/ccraddock/RVIP) |
| RSVP Single-Target Detection | Detect a single target in a rapid stream of items (~10/sec). Measures temporal attention resolution. | Potter, 1975 |  |
| Simple Reaction Time | Press a single key as quickly as possible whenever any stimulus appears. Measures basic detection + motor speed; baseline for more complex RT paradigms. | Donders, 1868 | [PT](https://www.psytoolkit.org/experiment-library/pvtb.html) · [Pv](https://pavlovia.org/demos/jsPsych_SimpleReactionTime) |
| Stroop Task | Name the ink color of color-words (e.g., "RED" in blue ink). Measures selective attention and inhibitory control. | Stroop, 1935 | [PT](https://www.psytoolkit.org/experiment-library/stroop.html) · [Ms](https://www.millisecond.com/download/library/stroop/) · [EF](https://github.com/expfactory-experiments/stroop-5min) · [Pv](https://pavlovia.org/dejan.draschkow/onlineworkshopstroop) |
| Sustained Attention to Response Task (SART) | Respond to every stimulus except an infrequent target (reverse CPT). Commission errors index attention lapses and mind-wandering. | Robertson et al., 1997 | [PT](https://www.psytoolkit.org/experiment-library/sart.html) · [Ms](https://www.millisecond.com/download/library/sart/) · [Pv](https://pavlovia.org/Virgi/sartengversion) |
| Useful Field of View (UFOV) | Identify a central target while localizing a peripheral target. Measures spatial extent of attentional processing. | Ball et al., 1988 |  |
| Visual Search | Search for a target among distractors. Set-size effects reveal parallel (pop-out) vs. serial search. | Treisman & Gelade, 1980 | [PT](https://www.psytoolkit.org/experiment-library/search.html) · [Ms](https://www.millisecond.com/download/library/visualsearch/) · [Pv](https://pavlovia.org/AMlab.UCF/vwm_ssm_task) |

### Memory

| Task | Description | Key Reference | Implementations |
|------|-------------|---------------|-----------------|
| Brief Visuospatial Memory Test (BVMT-R) | Copy and recall geometric figures across learning trials. Tests visuospatial learning and delayed recall. | Benedict, 1997 |  |
| Change Detection (Visual WM) | Judge whether an item changed in a briefly viewed array after a delay. Estimates visual WM capacity (Cowan's K). | Luck & Vogel, 1997 | [PT](https://www.psytoolkit.org/experiment-library/retrocue.html) · [Pv](https://pavlovia.org/bforys/change-detection-task) · [GitHub](https://github.com/shahar-lab/working_memory_capacity_change_detection_task) |
| Corsi Block-Tapping | Reproduce a sequence of block taps. Measures visuospatial working memory span. | Corsi, 1972 | [PT](https://www.psytoolkit.org/experiment-library/corsi.html) · [Pv](https://pavlovia.org/afiske/corsi_blocks) · [jP](https://github.com/nivlab/jspsych-demos/tree/main/tasks/spatial-recall) |
| Deese-Roediger-McDermott (DRM) | Study semantically related words; frequently falsely recall/recognize the non-presented critical lure. | Roediger & McDermott, 1995 | [Pv](https://pavlovia.org/Ao-Inc/drm-final) |
| Delayed Matching to Sample (DMS) | Match a complex visual pattern to alternatives after a delay. Measures short-term visual recognition memory. | Sahakian et al., 1988 | [Pv](https://pavlovia.org/amanoogian/rlwm_trauma) · [GitHub](https://github.com/soheilbr82/BluegrassWorkingMemory) |
| Digit Span (Forward/Backward) | Repeat digit sequences in order or reverse. Forward = storage; backward = storage + manipulation. | Wechsler, 1939 | [PT](https://www.psytoolkit.org/experiment-library/digitspan.html) · [Ms](https://www.millisecond.com/download/library/digitspan/) · [EF](https://github.com/expfactory-experiments/digit-span) · [Pv](https://pavlovia.org/sawabedog/digit-span) |
| Directed Forgetting | Some items cued "forget," others "remember." Comparing memory for each reveals intentional memory control. | Bjork, 1970 | [Pv](https://pavlovia.org/joy/dfexpfr_tbv2) |
| Free Recall | Study a list, then recall items in any order. Serial position effects reveal storage/retrieval dynamics. | Murdock, 1962 |  |
| List Sorting Working Memory Test | Reorder sequences of visually and orally presented stimuli (e.g., animals by size). NIH Toolbox WM measure. | Tulsky et al., 2014 | [NIH Toolbox](https://www.healthmeasures.net/explore-measurement-systems/nih-toolbox) |
| N-back | Indicate whether the current stimulus matches the one N items back. Working memory updating; difficulty scales with N. | Kirchner, 1958 | [PT](https://www.psytoolkit.org/experiment-library/nback2.html) · [Ms](https://www.millisecond.com/download/library/nback/) · [Pv](https://pavlovia.org/carolina.guerra/progetto-figurella-goldsmiths) |
| Operation Span (OSPAN) | Alternate between math problems and remembering items. Measures WM capacity under dual-task load. | Turner & Engle, 1989 | [PT](https://www.psytoolkit.org/experiment-library/aospan.html) · [Ms](https://www.millisecond.com/download/library/ospan/) · [Pv](https://pavlovia.org/DariaAbuzova/ospan) |
| Paired Associates Learning | Learn arbitrary pairs (e.g., word–word); tested via cued recall. Measures associative memory binding. | Calkins, 1894 |  |
| Part-Set Cuing | Providing some list items as cues paradoxically impairs recall of remaining items. Demonstrates retrieval competition. | Slamecka, 1968 |  |
| Pattern Recognition Memory (PRM) | Recognize previously seen abstract visual patterns among novel foils. Measures visual pattern recognition. | Sahakian & Owen, 1992 |  |
| Prospective Memory | Remember to perform a future action while engaged in an ongoing task. | Einstein & McDaniel, 1990 | [Pv](https://pavlovia.org/Laera/time-based-prospective-memory-demo) · [GitHub](https://github.com/mcvinding/PM_volition) |
| Reading Span | Read sentences while remembering final words. Measures WM capacity in a language context. | Daneman & Carpenter, 1980 |  |
| Recognition Memory | Distinguish old from new items after study. Analyzed with signal detection theory (d', criterion). | Mandler, 1980 | [Pv](https://pavlovia.org/Gabriela/animals) |
| Retrieval-Induced Forgetting (RIF) | Practicing retrieval of some category members impairs recall of related unpracticed items. Reveals inhibitory retrieval processes. | Anderson, Bjork, & Bjork, 1994 |  |
| Rey Auditory Verbal Learning Test (RAVLT) | 15-word list across five learning trials, interference list, delayed recall. Measures verbal learning and retention. | Rey, 1941 |  |
| Serial Recall | Recall items in exact presentation order. Reveals phonological similarity and word-length effects. | Conrad & Hull, 1964 |  |
| Source Memory | Recall contextual details about how/where information was learned. Measures episodic source monitoring. | Johnson, Hashtroudi, & Lindsay, 1993 |  |
| Spatial Recognition Memory (SRM) | Remember spatial locations and discriminate old from novel locations after a delay. | Owen et al., 1995 | [Pv](https://pavlovia.org/Consultancy/change_localization_public) |
| Sternberg Task | Judge whether a probe was in a previously shown memory set. RT increases linearly with set size. | Sternberg, 1966 | [Ms](https://www.millisecond.com/download/library/sternberg/) · [Pv](https://pavlovia.org/demos/sternberg) |
| Think/No-Think Paradigm | After learning word pairs, suppress retrieval of some targets when cued. Tests voluntary memory suppression. | Anderson & Green, 2001 |  |

### Executive Function

| Task | Description | Key Reference | Implementations |
|------|-------------|---------------|-----------------|
| Antisaccade | Look away from a peripheral stimulus. Measures inhibitory control of eye movements. | Hallett, 1978 | [Pv](https://pavlovia.org/demos/antisaccade) |
| AX-CPT | Respond to A-then-X sequences; measures proactive vs. reactive cognitive control. | Braver et al., 2001 | [PT](https://www.psytoolkit.org/experiment-library/ax-cpt.html) · [TB](https://github.com/TaskBeacon/H000001-ax-cpt) |
| Brixton Spatial Anticipation | Predict dot position as rules change. Errors after rule changes measure set-shifting. | Burgess & Shallice, 1997 |  |
| Choice Reaction Time | Press one of several keys depending on which stimulus appears. RT scales with number of alternatives (Hick's law); measures speed of stimulus-response selection. | Hick, 1952 | [PT](https://www.psytoolkit.org/experiment-library/deary_liewald.html) · [Pv](https://pavlovia.org/demos/choicertt) |
| Color-Word Interference (D-KEFS) | Extended Stroop with four conditions including inhibition/switching. Part of the Delis-Kaplan Executive Function System. | Delis, Kaplan, & Kramer, 2001 | [Pv](https://pavlovia.org/ckoch/homophones) |
| Dimensional Change Card Sort (DCCS) | Sort cards by one dimension (e.g., color), then switch to another (e.g., shape). NIH Toolbox EF measure. | Zelazo, 2006 | [PT](https://www.psytoolkit.org/experiment-library/dccs.html) · [NIH Toolbox](https://www.healthmeasures.net/explore-measurement-systems/nih-toolbox) |
| Go/No-Go | Respond to frequent "go" stimuli, withhold to "no-go." Measures response inhibition. | Donders, 1868 | [PT](https://www.psytoolkit.org/experiment-library/go-no-go.html) · [Ms](https://www.millisecond.com/download/library/gonogo/) · [Pv](https://pavlovia.org/ag2036/go-nogo-task) · [TB](https://github.com/TaskBeacon/T000005-go-nogo) |
| Hayling Sentence Completion | Complete sentences with a congruent word (Part A), then an incongruent word (Part B). Part B = suppression. | Burgess & Shallice, 1997 |  |
| Intra-Extra Dimensional Set Shift (IED) | Learn stimulus–reward rules based on one dimension, then shift to a new dimension. Separates intra- from extradimensional shifting. | Sahakian & Owen, 1992 | [Pv](https://pavlovia.org/aalbayati/wisconsin-card-sorting-task) · [GitHub](https://github.com/margdarna/IDED) |
| Letter-Number Sequencing | Reorder intermixed letters and numbers (numbers ascending, letters alphabetical). Measures WM manipulation. | Gold et al., 1997 |  |
| Pattern Comparison Processing Speed | Judge whether two side-by-side visual patterns are same or different as quickly as possible. NIH Toolbox processing speed measure. | Carlozzi et al., 2015 | [Pv](https://pavlovia.org/kerblooee/pattern_glare3) · [NIH Toolbox](https://www.healthmeasures.net/explore-measurement-systems/nih-toolbox) |
| Simon Task | Respond based on a non-spatial feature while stimulus location is congruent/incongruent with the response. | Simon & Rudell, 1967 | [PT](https://www.psytoolkit.org/experiment-library/simon.html) · [Pv](https://pavlovia.org/lammed/simon-task-1) |
| Stockings of Cambridge (SOC) | Plan a sequence of moves to match a goal arrangement of colored balls (computerized Tower of London). | Owen et al., 1990 | [Pv](https://pavlovia.org/jeongminshin97/tower-of-london) · [jsPsych](https://github.com/jspsych/jspsych-contrib/tree/main/packages/plugin-tower-of-london) |
| Stop-Signal Task | Cancel an initiated response when a stop signal appears. SSRT estimates inhibitory control speed. | Logan & Cowan, 1984 | [PT](https://www.psytoolkit.org/experiment-library/stopsignal.html) · [TB](https://github.com/TaskBeacon/H000012-sst) |
| Task Switching | Alternate between tasks; switch cost measures mental set reconfiguration. | Rogers & Monsell, 1995 | [PT](https://www.psytoolkit.org/experiment-library/taskswitching.html) · [Ms](https://www.millisecond.com/download/library/taskswitching/) · [Pv](https://pavlovia.org/fedegiovannetti/attention_switching_demo) |
| Tower of London / Hanoi | Rearrange disks to match a goal in minimum moves. Measures planning and problem-solving. | Shallice, 1982 | [PT](https://www.psytoolkit.org/experiment-library/tower_hanoi.html) · [Ms](https://www.millisecond.com/download/library/toweroflondon/) · [EF](https://github.com/expfactory-experiments/tower-of-london) · [Pv](https://pavlovia.org/cgambi/tower_of_london_pav) |
| Trail Making Test (TMT) | Part A: connect numbers. Part B: alternate numbers and letters. B–A indexes cognitive flexibility. | Reitan, 1958 | [Pv](https://pavlovia.org/c8b/trail-making-task) |
| Verbal Fluency (FAS / Category) | Generate words starting with a letter or from a category within a time limit. | Thurstone, 1938 | [Pv](https://pavlovia.org/anastasijamarkovic/word-fluency-task-dutch-animals) |
| Wisconsin Card Sorting Test (WCST) | Sort cards by an unknown, shifting rule. Perseverative errors measure cognitive flexibility. | Berg, 1948 | [PT](https://www.psytoolkit.org/experiment-library/wcst.html) · [Ms](https://www.millisecond.com/download/library/cardsort/) · [Pv](https://pavlovia.org/vespr/wisconsin-card-sorting-task) |

### Decision Making

| Task | Description | Key Reference | Implementations |
|------|-------------|---------------|-----------------|
| Balloon Analogue Risk Task (BART) | Pump a virtual balloon for increasing reward; risk losing all if it pops. Indexes risk-taking propensity. | Lejuez et al., 2002 | [PT](https://www.psytoolkit.org/experiment-library/bart.html) · [Ms](https://www.millisecond.com/download/library/bart/) · [Pv](https://pavlovia.org/ChZ_CC/bart) · [TB](https://github.com/TaskBeacon/H000002-bart) |
| Beads Task (Jumping to Conclusions) | Draw beads from jars of known ratios; decide which jar they come from. Fewer draws = jumping to conclusions bias. | Huq, Garety, & Hemsley, 1988 | [Pv](https://pavlovia.org/auzworld/beads-distractor) |
| Cambridge Gambling Task (CGT) | Bet on outcomes with explicit probabilities displayed. Separates risk-taking from learning. | Rogers et al., 1999 | [GitHub](https://github.com/jspickering/Experiments) |
| Decisions from Experience | Participants sample from payoff distributions before choosing, rather than seeing described probabilities. Reveals the description–experience gap. | Hertwig et al., 2004 | [Pv](https://pavlovia.org/hammerking/d-e-gap) · [GitHub](https://github.com/sappelhoff/sp_experiment) |
| Delay Discounting | Choose between smaller-sooner and larger-later rewards. Discounting steepness measures impulsivity. | Mazur, 1987 | [Pv](https://pavlovia.org/abordeianu/e4e_delaydiscounting_v2) |
| Dictator Game | One player allocates money to a passive other. Purer measure of altruism/prosocial preferences. | Kahneman, Knetsch, & Thaler, 1986 | [Ms](https://www.millisecond.com/download/library/dictatorgame/) |
| Effort-Based Decision Making (EEfRT) | Choose low-effort/low-reward vs. high-effort/high-reward tasks. Measures motivation and effort discounting. | Treadway et al., 2009 | [GitHub](https://github.com/bizerkmaverick/EEfRT-9-9-16) · [jsPsych](https://github.com/belieflab/eEfRT) |
| Footbridge Dilemma | Decide whether to push a person to stop a trolley killing five. "Personal" moral dilemma engaging stronger emotional processing. | Thomson, 1985; Greene et al., 2001 |  |
| Iowa Gambling Task (IGT) | Choose from four decks with varying reward/punishment. Measures affective decision-making under ambiguity. | Bechara et al., 1994 | [PT](https://www.psytoolkit.org/experiment-library/igt.html) · [Ms](https://www.millisecond.com/download/library/iowagamblingtask/) · [Pv](https://pavlovia.org/h_broadbent/iowa_gambling_4choice_h) |
| Moral Foundations Questionnaire | Rate the relevance of moral principles (care, fairness, loyalty, authority, purity) to moral judgments. | Graham et al., 2011 |  |
| Outcome Devaluation | After learning an action–outcome association, the outcome is devalued. Sensitivity distinguishes goal-directed from habitual behavior. | Adams & Dickinson, 1981 |  |
| Pavlovian-to-Instrumental Transfer (PIT) | Pavlovian cues associated with outcomes bias instrumental responding toward the associated action. | Holland, 2004 |  |
| Prisoner's Dilemma | Cooperate or defect; iterated versions measure cooperation strategies. | Axelrod, 1984 |  |
| Public Goods Game | Contribute to a shared pool (multiplied, redistributed). Measures cooperation and free-riding. | Ledyard, 1995 | [oTree](https://github.com/chapkovski/fehr-and-gaechter) |
| Trolley Dilemma | Decide whether to divert a trolley to kill one person to save five. Classic moral dilemma indexing utilitarian reasoning. | Foot, 1967; Greene et al., 2001 |  |
| Trust Game | Investor sends money (multiplied) to trustee who decides return. Measures trust and reciprocity. | Berg, Dickhaut, & McCabe, 1995 | [Ms](https://www.millisecond.com/download/library/trustgame/) |
| Ultimatum Game | Proposer splits money; responder accepts or rejects. Measures fairness norms and punishment. | Guth, Schmittberger, & Schwarze, 1982 | [Ms](https://www.millisecond.com/download/library/ultimatumgame/) · [Pv](https://pavlovia.org/In/facial-expression-in-ultimatum-game) |

### Perception

| Task | Description | Key Reference | Implementations |
|------|-------------|---------------|-----------------|
| Apparent Motion | Two spatially separated stimuli in alternation produce the illusion of movement. Probes motion correspondence mechanisms. | Wertheimer, 1912 | [Pv](https://pavlovia.org/lpxrh6/cross-bounce-illusion) · [OSF](https://osf.io/jntqz/) |
| Backward Masking | A briefly presented target is immediately followed by a mask, rendering it invisible. Measures temporal limits of conscious perception. | Breitmeyer & Ogmen, 2000 | [Pv](https://pavlovia.org/hoplab/tim_exp1) · [GitHub](https://github.com/AdrienSF/psychopy-target-mask-sequence) |
| Binocular Rivalry | Different images to each eye; perception alternates. Probes perceptual competition and conscious awareness. | Blake & Logothetis, 2002 | [GitHub](https://github.com/janfreyberg/binocular-rivalry) · [OSF](https://osf.io/xpy7r/) |
| Biological Motion (Point-Light Walker) | Identify actions from sparse point-light displays. | Johansson, 1973 | [GitHub](https://github.com/hyiltiz/PLW) |
| Change Detection (Visual WM) | Judge whether an item changed in a briefly viewed array after a delay. Estimates visual WM capacity (Cowan's K). | Luck & Vogel, 1997 | [PT](https://www.psytoolkit.org/experiment-library/retrocue.html) · [Pv](https://pavlovia.org/bforys/change-detection-task) · [GitHub](https://github.com/shahar-lab/working_memory_capacity_change_detection_task) |
| Continuous Flash Suppression (CFS) | High-contrast dynamic patterns to one eye suppress a static target in the other from awareness. Measures unconscious visual processing. | Tsuchiya & Koch, 2005 |  |
| Contour Integration | Detect aligned Gabor elements forming a path among random elements. Measures contour grouping. | Field, Hayes, & Hess, 1993 |  |
| Crowding | Identify a peripheral target flanked by nearby distractors. Impaired identification probes spatial limits of object recognition. | Bouma, 1970 |  |
| Embedded Figures Test | Locate a simple shape within a complex pattern. Measures field independence. | Witkin et al., 1971 |  |
| Gabor Patch Detection | Detect presence/orientation of Gabor patches at varying contrasts. Measures visual sensitivity. | Watson & Pelli, 1983 | [jsPsych](https://github.com/kogpsy/jspsych-gabor-stimulus-plugin) |
| Judgment of Line Orientation (JLO) | Match the orientation of two angled lines to a response array. Measures visuospatial perception. | Benton et al., 1978 |  |
| Mental Rotation | Judge whether two rotated 3D objects are same or mirror images. RT scales with angular disparity. | Shepard & Metzler, 1971 | [PT](https://www.psytoolkit.org/experiment-library/mentalrotation.html) · [Ms](https://www.millisecond.com/download/library/mentalrotation/) · [Pv](https://pavlovia.org/einsteinlab/mrt-classic) |
| Muller-Lyer Illusion | Judge line lengths with inward/outward arrowheads. Measures susceptibility to geometric illusions. | Muller-Lyer, 1889 | [Pv](https://pavlovia.org/demos/muller_lyer_illusion) |
| Psychophysical Staircase | Stimulus intensity adjusted trial-by-trial to converge on perceptual threshold. | Levitt, 1971 | [Pv](https://pavlovia.org/demos/psychophysics_staircase) · [GitHub](https://github.com/hadrienj/StaircaseJS) · [jsPsych](https://github.com/kurokida/jsQuestPlus) |
| Random Dot Motion (RDK) | Judge global motion direction with varying coherence levels. Measures motion perception and perceptual decision-making. | Newsome & Pare, 1988 | [Pv](https://pavlovia.org/Consultancy/rdk_staircase_movies) · [jsPsych](https://github.com/jspsych/jspsych-contrib/tree/main/packages/plugin-rdk) |
| Simultaneity Judgment (SJ) | Judge whether two stimuli appeared at the same time or at different times. Measures temporal binding window. | Hirsh & Sherrick, 1961 |  |
| Temporal Order Judgment (TOJ) | Report which of two stimuli appeared first. Measures temporal resolution. | Sternberg & Knoll, 1973 | [Pv](https://pavlovia.org/epicpsych/sensory-adaptation) · [jsPsych](https://github.com/bjoluc/jspsych-toj-experiments) |
| Time Reproduction / Interval Timing | Reproduce the duration of a presented interval. Measures internal clock precision and scalar timing. | Gibbon, Church, & Meck, 1984 | [Pv](https://pavlovia.org/giulio.munaretto/time_reproduction_production) |
| Vernier Acuity | Judge the offset of two line segments. Measures hyperacuity — spatial resolution finer than photoreceptor spacing. | Westheimer & McKee, 1977 |  |

### Language

| Task | Description | Key Reference | Implementations |
|------|-------------|---------------|-----------------|
| Cross-Modal Priming | Auditory sentence + visual word probe at critical points. RT to probe reveals real-time lexical activation during speech. | Swinney, 1979 |  |
| Garden Path Sentences | Sentences with temporary syntactic ambiguity lead to initial misparse and recovery. Reading time increase measures reanalysis. | Frazier & Rayner, 1982 |  |
| Lexical Decision | Classify letter strings as real words or nonwords. Reveals lexical access speed and word frequency effects. | Meyer & Schvaneveldt, 1971 | [PT](https://www.psytoolkit.org/experiment-library/ldt.html) · [Pv](https://pavlovia.org/19004494/lexical-decision-task-19004494) |
| Masked Priming | A very briefly presented, masked prime word facilitates recognition of a related target. Reveals automatic lexical processing. | Forster & Davis, 1984 | [Pv](https://pavlovia.org/bangele/online-prime-ldt) |
| Nonword Repetition | Repeat novel nonsense words of increasing length. Measures phonological short-term memory. | Gathercole & Baddeley, 1990 | [Ms](https://www.millisecond.com/download/library/nonwordrepetition/) |
| Oral Reading Recognition | Read aloud single words of increasing difficulty. NIH Toolbox reading decoding measure. | Gershon et al., 2014 | [Pv](https://pavlovia.org/fcerpe/reading_test_en) · [NIH Toolbox](https://www.healthmeasures.net/explore-measurement-systems/nih-toolbox) |
| Phoneme Monitoring | Detect a target phoneme in speech. Measures speech segmentation. | Foss, 1969 |  |
| Picture Naming | Name depicted objects as quickly as possible. Sensitive to lexical retrieval and word frequency. | Snodgrass & Vanderwart, 1980 |  |
| Picture Vocabulary Test | Select from four pictures the one matching a spoken word. NIH Toolbox receptive vocabulary measure. | Gershon et al., 2014 | [NIH Toolbox](https://www.healthmeasures.net/explore-measurement-systems/nih-toolbox) |
| Self-Paced Reading | Press a key to reveal each word; reading times at critical regions reveal parsing strategies. | Just, Carpenter, & Woolley, 1982 | [PT](https://www.psytoolkit.org/experiment-library/pacedreading1.html) · [Pv](https://pavlovia.org/bangele/spr_turkish_wow) · [jsPsych](https://github.com/jspsych/jspsych-contrib/tree/main/packages/plugin-self-paced-reading) |
| Semantic Priming | A related prime speeds target recognition. Measures spreading activation in semantic memory. | Neely, 1977 | [Pv](https://pavlovia.org/kybu9101/ambiguous-images) |
| Sentence Completion (Cloze) | Complete a sentence with the most likely word. Cloze probability used in ERP research (N400). | Taylor, 1953 | [jsPsych](https://www.jspsych.org/7.3/plugins/cloze/) |
| Sentence Verification | Judge true/false (e.g., "A canary is a bird"). Indexes category typicality. | Collins & Quillian, 1969 | [Pv](https://pavlovia.org/ISA666/pre-segmented) |
| Syntactic Priming | Exposure to a syntactic structure (e.g., passive) increases production of that structure in subsequent sentences. | Bock, 1986 |  |
| Visual World Paradigm | Eye movements to objects during spoken language reveal real-time word recognition. | Tanenhaus et al., 1995 | [GitHub](https://github.com/aufrank/VisualWorld) |
| Word Naming (Pronunciation) | Read aloud presented words. Naming latency reflects phonological encoding and regularity effects. | Coltheart et al., 2001 | [Pv](https://pavlovia.org/apitiot/pronouncethewords) |
| Word Superiority Effect | Letters identified more accurately when embedded in words than in nonwords or alone. Demonstrates top-down influence. | Reicher, 1969 | [Pv](https://pavlovia.org/demos/word_superiority_effect) |

### Social Cognition

| Task | Description | Key Reference | Implementations |
|------|-------------|---------------|-----------------|
| Asch Conformity Paradigm | Judge line lengths after confederates give unanimously wrong answers. Measures conformity to social pressure. | Asch, 1951 |  |
| Cambridge Face Memory Test | Learn and identify faces. Measures face recognition ability. | Duchaine & Nakayama, 2006 | [Pv](https://pavlovia.org/ash24/glasgowfacematchingtask) |
| Cyberball | Virtual ball-tossing game where the participant is gradually excluded. Measures social exclusion effects. | Williams, Cheung, & Choi, 2000 | [Ms](https://www.millisecond.com/download/library/cyberball/) · [Pv](https://pavlovia.org/demos/cyberball) · [GitHub](https://github.com/azaleara/cyberball) |
| Director Task | Take into account another person's visual perspective when selecting objects. Measures perspective-taking. | Keysar et al., 2000 | [GitHub](https://github.com/pomodoren/psychopy-directortask) |
| Empathy for Pain Paradigm | Observe another person receiving a painful stimulus while neural/physiological responses are measured. | Singer et al., 2004 |  |
| Face Inversion Effect | Recognize upright vs. inverted faces. Disproportionate inversion cost demonstrates configural face processing. | Yin, 1969 |  |
| False Belief Task (Sally-Anne) | Predict where a character will look for an object moved in their absence. First-order theory of mind. | Wimmer & Perner, 1983 |  |
| Faux Pas Recognition | Identify social faux pas in stories. Measures advanced theory of mind. | Baron-Cohen et al., 1999 |  |
| Gaze Cueing | A central face looks left/right before a target. Measures automatic social attention following. | Friesen & Kingstone, 1998 | [Pv](https://pavlovia.org/kadel00/gender-differences-in-social-gaze-cueing-task) |
| Heider-Simmel Animation | Describe movements of geometric shapes. Reveals spontaneous social/intentional attribution. | Heider & Simmel, 1944 |  |
| Implicit Association Test (IAT) | Rapidly categorize stimuli along two dimensions; RT difference measures implicit bias. | Greenwald, McGhee, & Schwartz, 1998 | [PT](https://www.psytoolkit.org/experiment-library/iat.html) · [Ms](https://www.millisecond.com/download/library/iat/) · [Pv](https://pavlovia.org/demos/openiat) |
| Milgram Obedience Paradigm | Administer apparent electric shocks under authority instruction. Measures obedience to authority figures. | Milgram, 1963 |  |
| Minimal Group Paradigm | Categorize participants into arbitrary groups; measure in-group favoritism in resource allocation. | Tajfel et al., 1971 |  |
| Reading the Mind in the Eyes (RMET) | Infer mental states from photographs of the eye region. Measures advanced theory of mind. | Baron-Cohen et al., 2001 |  |
| Strange Situation | Caregiver–infant separations and reunions in a structured lab setting. Classifies attachment styles. | Ainsworth et al., 1978 |  |

### Learning

| Task | Description | Key Reference | Implementations |
|------|-------------|---------------|-----------------|
| Artificial Grammar Learning | Study strings from a finite-state grammar; classify new strings as grammatical or not. | Reber, 1967 | [OSF](https://osf.io/f5ksg/) |
| Classical (Pavlovian) Conditioning | Neutral stimulus paired with US until it elicits a conditioned response. | Pavlov, 1927 | [Pv](https://pavlovia.org/jaf2105/1010c) |
| Contextual Cueing | Repeated spatial configurations speed visual search without explicit awareness. | Chun & Jiang, 1998 | [GitHub](https://github.com/nimarek/Contextual-Cueing-Unity) |
| Fear Conditioning and Extinction | Tone (CS) paired with shock (US); CS alone then elicits fear. Extinction via CS-alone trials. | Phelps et al., 2004 | [GitHub](https://github.com/flare-kcl/flare-app) |
| Information Integration Category Learning | Categorize stimuli by integrating multiple dimensions (not easily verbalized). Relies on implicit systems. | Ashby & Maddox, 2005 | [Pv](https://pavlovia.org/catlab/type-i-shj-categorization-task) |
| Instrumental (Operant) Conditioning | Participants learn that actions produce specific outcomes. Schedule manipulations measure goal-directed vs. habitual learning. | Skinner, 1938 |  |
| Latent Inhibition | Pre-exposure to a stimulus without consequences retards subsequent conditioning to that stimulus. Measures learned irrelevance. | Lubow & Moore, 1959 |  |
| Probabilistic Learning (Two-Armed Bandit) | Choose between options with different reward probabilities. Modeled with reinforcement learning. | Daw et al., 2006 | [Pv](https://pavlovia.org/bliebenow/probabilistic-learning-task) · [jP](https://github.com/nivlab/jspsych-demos/tree/main/tasks/bandit) · [Niv Lab](https://nivlab.github.io/jspsych-demos/tasks/3arm/experiment.html) |
| Reversal Learning | After learning a stimulus–reward association, contingencies reverse. Measures flexibility in reward learning. | Dias, Robbins, & Roberts, 1996 | [jP](https://github.com/nivlab/jspsych-demos/tree/main/tasks/3arm) |
| Sensory Preconditioning | Two neutral stimuli are paired; one is then conditioned. Testing the other reveals indirect associative transfer. | Brogden, 1939 |  |
| Serial Reaction Time (SRT) | Respond to stimuli in a repeating spatial sequence. RT speedup indexes implicit sequence learning. | Nissen & Bullemer, 1987 | [Pv](https://pavlovia.org/davidcrowe/srtpredictionfinal) |
| Sign-Tracking vs. Goal-Tracking | After Pavlovian conditioning, some subjects approach the predictive cue (sign) while others approach the reward location (goal). | Robinson & Flagel, 2009 |  |
| Statistical Learning | Exposure to streams with embedded regularities. Sensitivity to transitional probabilities measures implicit learning. | Saffran, Aslin, & Newport, 1996 |  |
| Trace Conditioning | CS offset precedes US onset by a temporal gap. Requires hippocampal-dependent bridging of the CS–US gap. | Clark & Squire, 1998 |  |
| Visuomotor Rotation Adaptation | Cursor feedback is rotated relative to hand movement; participants gradually adapt. Measures sensorimotor error-based learning. | Krakauer et al., 2000 | [Pv](https://pavlovia.org/aalbayati/block_rotation) · [GitHub](https://github.com/alan-s-lee/OnPoint) |
| Weather Prediction Task | Predict outcomes from probabilistic cue combinations. Dissociates declarative from procedural learning. | Knowlton, Squire, & Gluck, 1994 |  |

### Emotion

| Task | Description | Key Reference | Implementations |
|------|-------------|---------------|-----------------|
| Affective Go/No-Go | Respond to one emotional category, withhold to another. Measures emotion–inhibition interaction. | Murphy et al., 1999 | [Ms](https://www.millisecond.com/download/library/affectivegonogo/) |
| Affective Priming | Emotional prime facilitates/inhibits evaluation of a subsequent target. Measures automatic affective processing. | Fazio et al., 1986 | [Ms](https://www.millisecond.com/download/library/affectivepriming/) · [OSF](https://osf.io/x8mn4/) |
| Approach-Avoidance Task (AAT) | Push/pull a joystick in response to emotional stimuli. Congruence effects reveal automatic approach/avoidance tendencies. | Rinck & Becker, 2007 | [PT](https://www.psytoolkit.org/experiment-library/vaast_images.html) |
| Dot Probe (Attentional Bias) | Probe replaces one of two stimuli (emotional/neutral). Faster detection at emotional location = attentional bias. | MacLeod, Mathews, & Tata, 1986 | [PT](https://www.psytoolkit.org/experiment-library/dotprobe.html) · [Ms](https://www.millisecond.com/download/library/dotprobe/) · [TB](https://github.com/TaskBeacon/T000003-emodot) |
| Emotion Recognition (Ekman Faces) | Label facial expressions of the six basic emotions. Measures facial emotion recognition accuracy. | Ekman & Friesen, 1976 | [Pv](https://pavlovia.org/abordeianu/e4e_emotionrecognition) |
| Emotion Regulation Task | Reappraise, suppress, or attend to emotional images. Indexes regulation strategy effectiveness. | Ochsner et al., 2004 | [EF](https://github.com/expfactory-experiments/emotion-regulation) |
| Emotional Faces Dot Probe | Dot-probe variant using emotional faces. Widely used in anxiety and depression research for attentional bias to threat. | Mogg, Philippot, & Bradley, 2004 | [Ms](https://www.millisecond.com/download/library/dotprobe/) |
| Emotional Flanker | Emotional distractors flank a central target. Measures involuntary attentional capture by emotional stimuli. | Fenske & Eastwood, 2003 |  |
| Emotional Stroop | Name ink color of emotionally valenced words. Slowed naming for emotional words indexes attentional capture. | Williams, Mathews, & MacLeod, 1996 | [Ms](https://www.millisecond.com/download/library/emotionalstroop/) |
| Facial Action Coding System (FACS) Paradigm | Systematically code facial muscle movements (Action Units) to measure spontaneous emotional expression. | Ekman & Friesen, 1978 | [Pv](https://pavlovia.org/demos/face_api) |
| Fear-Potentiated Startle | Startle probe during a fear-conditioned stimulus produces enhanced eyeblink. Measures conditioned fear physiologically. | Davis, 1986 |  |
| IAPS Viewing | View standardized emotional images while physiological/neural responses are measured. | Lang, Bradley, & Cuthbert, 1997 |  |
| Mood Induction Procedures | Film clips, music, or recall used to induce transient mood states as experimental variables. | Westermann et al., 1996 | [jsPsych](https://github.com/kywch/Mood-Induction_jsPsych) |
| Startle Reflex Modulation | Eyeblink startle to sudden noise during emotional images — potentiated during negative, attenuated during positive. | Lang, Bradley, & Cuthbert, 1990 |  |
| Trier Social Stress Test (TSST) | Public speaking + mental arithmetic before evaluators. Gold-standard lab stress induction producing cortisol responses. | Kirschbaum, Pirke, & Hellhammer, 1993 | [GitHub](https://github.com/MIEC/vr-tsst) |

### Creativity

| Task | Description | Key Reference | Implementations |
|------|-------------|---------------|-----------------|
| Alternate Uses Task (AUT) | Generate as many unusual uses for a common object (e.g., brick) as possible. Scores fluency, flexibility, and originality. | Guilford, 1967 |  |
| Compound Remote Associates (CRA) | Given three compound-word stems, find the word that completes all three. Modernized RAT variant. | Bowden & Jung-Beeman, 2003 | [GitHub](https://github.com/aesthetiffs/Compound-Remote-Associates-PsychoPy2) |
| Consensual Assessment Technique (CAT) | Experts independently rate creative products (stories, collages, poems). Measures real-world creative output. | Amabile, 1982 |  |
| Insight Problems (Matchstick, Nine-Dot) | Solve problems requiring restructuring of the initial representation. Measures insight vs. analytic problem solving. | Metcalfe & Wiebe, 1987 |  |
| Remote Associates Test (RAT) | Given three words (e.g., "falling, actor, dust"), find a fourth linking them all ("star"). Measures convergent creative thinking. | Mednick, 1962 |  |
| Torrance Tests of Creative Thinking (TTCT) | Battery of verbal and figural tasks yielding fluency, flexibility, originality, and elaboration scores. | Torrance, 1966 |  |

### Metacognition

| Task | Description | Key Reference | Implementations |
|------|-------------|---------------|-----------------|
| Ease of Learning (EOL) | Before study, judge how easy each item will be to learn. Measures pre-study metacognitive prediction. | Underwood, 1966 |  |
| Feeling of Knowing (FOK) | After failing to recall, judge the likelihood of recognizing the item later. Prospective metacognitive judgment. | Hart, 1965 |  |
| Judgment of Learning (JOL) | After studying each item, predict the likelihood of recalling it later. Accuracy measures metacognitive monitoring. | Nelson & Dunlosky, 1991 |  |
| Perceptual Confidence / Meta-d' | After perceptual discrimination, rate confidence. Meta-d' quantifies metacognitive sensitivity independently of task performance. | Maniscalco & Lau, 2012 | [GitHub](https://github.com/metacoglab/meta_dots) |
| Retrospective Confidence Judgment (RCJ) | Rate confidence in the correctness of a just-given response. Calibration and resolution metrics measure metacognitive accuracy. | Koriat, 2007 |  |
| Tip-of-the-Tongue (TOT) Paradigm | Retrieve answers to general knowledge questions; report TOT states. Measures retrieval failure awareness. | Brown & McNeill, 1966 |  |

### Motor Control

| Task | Description | Key Reference | Implementations |
|------|-------------|---------------|-----------------|
| Finger Tapping Task | Tap a key as fast as possible (or at a specified rate). Measures motor speed, rhythm, and lateralization. | Reitan & Wolfson, 1985 | [Ms](https://www.millisecond.com/download/library/fingertapping/) · [Pv](https://pavlovia.org/Jenny-D/tappingexperiment-gruppe-a) |
| Fitts's Law Pointing | Move to targets of varying distance and width. Movement time scales logarithmically with index of difficulty. | Fitts, 1954 | [PT](https://www.psytoolkit.org/experiment-library/fitts.html) · [GitHub](https://github.com/SimonWallner/uit-fitts-law) |
| Force-Field Adaptation | A robotic arm applies velocity-dependent forces during reaching; participants learn to compensate. Measures internal model formation. | Shadmehr & Mussa-Ivaldi, 1994 |  |
| Grip Force Task | Lift an object and maintain stable grip; perturbations reveal predictive and reactive force control. | Johansson & Westling, 1988 |  |
| Mirror Tracing | Trace a shape while viewing only a mirror reflection. Measures visuomotor adaptation and procedural learning. | Milner, 1962 | [GitHub](https://github.com/rcalinjageman/mirror_trace) |
| Purdue Pegboard | Place pegs into holes as quickly as possible with each hand and both together. Measures fine manual dexterity. | Tiffin & Asher, 1948 |  |
| Visuomotor Rotation Task | Cursor feedback is rotated relative to hand movement; participants adapt reaching over trials. Measures sensorimotor adaptation. | Krakauer, 2009 | [GitHub](https://github.com/alan-s-lee/OnPoint) |

### Numerical Cognition

| Task | Description | Key Reference | Implementations |
|------|-------------|---------------|-----------------|
| Approximate Number System (ANS) Task | Judge which of two dot arrays is more numerous (non-symbolic). Ratio-dependent accuracy indexes ANS precision. | Halberda, Mazzocco, & Feigenson, 2008 |  |
| Number Comparison (Symbolic) | Judge which of two Arabic digits is larger. Distance effect reveals analogue magnitude representation. | Moyer & Landauer, 1967 |  |
| Number Line Estimation | Place a number on a physical line anchored at 0 and 100/1000. Shift from logarithmic to linear mapping tracks development. | Siegler & Opfer, 2003 | [EF](https://github.com/expfactory-experiments/number-line) |
| SNARC Task | Classify numbers while responding left/right. Faster left responses to small numbers reveals spatial–numerical mapping. | Dehaene, Bossini, & Giraux, 1993 | [PT](https://www.psytoolkit.org/experiment-library/numerical_stroop.html) · [Pv](https://pavlovia.org/JulietteLNeel/stimuli-effect-on-the-spatial-numerical-association-of-response-codes) |
| Subitizing | Enumerate briefly flashed dot arrays. Fast and accurate for 1–4 items (subitizing range), slower beyond. | Kaufman et al., 1949 | [GitHub](https://github.com/flowersteam/cognitive-testbattery) |

### Developmental

| Task | Description | Key Reference | Implementations |
|------|-------------|---------------|-----------------|
| A-not-B Error Task | Infant searches at location A after repeated finds there, even after watching the toy moved to B. Measures object permanence. | Piaget, 1954; Diamond, 1985 |  |
| Conservation Task | Transform the appearance of a quantity (e.g., pour water into a taller glass) and ask if the amount changed. Piagetian concrete operations. | Piaget, 1952 |  |
| Marshmallow Test (Delay of Gratification) | Child chooses one marshmallow now or waits for two. Measures self-control and delay of gratification in preschoolers. | Mischel, Shoda, & Rodriguez, 1989 |  |
| Picture Sequence Memory | Remember and reproduce the order of a sequence of activity pictures. NIH Toolbox episodic memory measure for all ages. | Bauer et al., 2013 | [NIH Toolbox](https://www.healthmeasures.net/explore-measurement-systems/nih-toolbox) |
| Preferential Looking | Present two stimuli side by side; differential looking time reveals visual preference or discrimination in pre-verbal infants. | Fantz, 1961 |  |
| Violation of Expectation (VoE) | Infants look longer at "impossible" events (e.g., object through solid barrier). Looking time indexes early physical knowledge. | Baillargeon, Spelke, & Wasserman, 1985 |  |

### Clinical / Screening

| Task | Description | Key Reference | Implementations |
|------|-------------|---------------|-----------------|
| Clock Drawing Test | Draw a clock face showing a specified time. Screens for visuospatial, executive, and semantic deficits. | Freedman et al., 1994 | [GitHub](https://github.com/Guanluo76/Clock_Drawing_Test) |
| Mini-Mental State Examination (MMSE) | 30-point screening covering orientation, registration, attention, recall, and language. Global cognitive screening tool. | Folstein, Folstein, & McHugh, 1975 |  |
| Montreal Cognitive Assessment (MoCA) | Brief screening for mild cognitive impairment across visuospatial, executive, memory, attention, language, and orientation. | Nasreddine et al., 2005 |  |
| Repeatable Battery for Assessment of Neuropsychological Status (RBANS) | Brief battery spanning immediate memory, visuospatial, language, attention, and delayed memory. | Randolph et al., 1998 |  |
| Symbol Digit Modalities Test (SDMT) | Match symbols to digits using a key as quickly as possible. Measures processing speed and incidental learning. | Smith, 1982 | [PT](https://www.psytoolkit.org/experiment-library/digit_substitution.html) · [jP](https://github.com/nivlab/jspsych-demos/tree/main/tasks/dsst) |

---

## Cross-Domain Tasks

Several tasks span multiple domains:

- **Stroop Task** — Attention + Executive Function (inhibition)
- **Go/No-Go & Stop-Signal** — Executive Function + Emotion (affective variants)
- **Change Detection** — Perception + Memory (visual working memory)
- **WCST** — Executive Function + Learning (rule learning from feedback)
- **Dot Probe** — Attention + Emotion (attentional bias)
- **N-back** — Memory + Executive Function (updating)
- **IAT** — Social Cognition + Attention (automatic associations)
- **Reading Span** — Memory + Language (verbal working memory)
- **Visuomotor Rotation** — Motor Control + Learning (sensorimotor adaptation)
- **PIT / Outcome Devaluation** — Decision Making + Learning (goal-directed vs. habitual)
- **Trolley/Footbridge Dilemmas** — Decision Making + Emotion (moral cognition)
- **Mirror Tracing** — Motor Control + Learning (procedural memory)
- **SART** — Attention + Executive Function (sustained attention / inhibition)
- **Delay of Gratification** — Developmental + Decision Making (self-regulation)
- **Number Line Estimation** — Numerical Cognition + Developmental (magnitude representation)

---

## Contributing

Contributions are welcome! Please read the [contributing guidelines](CONTRIBUTING.md) first.

If you know of a task, platform, or repository that should be listed here, please open an issue or submit a pull request.

---

## Acknowledgments

<a href="https://evolvinglanguage.ch">
  <img src="assets/nccr-evolving-language-logo.png" alt="NCCR Evolving Language" width="300">
</a>

This project was developed at [NCCR Evolving Language](https://evolvinglanguage.ch), a National Centre of Competence in Research funded by the [Swiss National Science Foundation](https://www.snf.ch).

## License

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)
