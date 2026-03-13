# Awesome Psychology Tasks [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated list of experimental psychology tasks and paradigms, the platforms to run them, and the repositories where you can find ready-made implementations.

## Contents

- [Platforms & Frameworks](#platforms--frameworks)
  - [Open Source](#open-source)
  - [Commercial / Freemium](#commercial--freemium)
  - [Hosting & Backend Services](#hosting--backend-services)
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

---

## Platforms & Frameworks

Software for creating and running psychology experiments.

### Open Source

| Platform | Description | Language / Tech | Online Support |
|----------|-------------|-----------------|----------------|
| [jsPsych](https://www.jspsych.org) | Plugin-based JavaScript framework for browser-based behavioral experiments. | JavaScript | Yes (native) |
| [PsychoPy](https://www.psychopy.org) | Full-featured experiment builder with graphical Builder and Python Coder views. Exports to JS via PsychoJS. | Python; JS (PsychoJS) | Via Pavlovia |
| [lab.js](https://lab.js.org) | Drag-and-drop visual experiment builder that runs in the browser. Exports to JATOS, Open Lab, Pavlovia. | JavaScript | Yes (native) |
| [OpenSesame](https://osdoc.cogsci.nl) | Graphical experiment builder with Python inline scripting. Online via OSWeb + JATOS. | Python; JS (OSWeb) | Partial (OSWeb) |
| [PEBL](https://pebl.sourceforge.net) | Cross-platform experiment building language with a 100+ test battery included. | Custom language (SDL) | No (desktop) |
| [oTree](https://www.otree.org) | Framework for interactive/multiplayer experiments, strong in game theory and economics. | Python (Django); JS | Yes |
| [Empirica](https://empirica.ly) | Platform for real-time multiplayer behavioral experiments. | JavaScript (React) | Yes |
| [Pushkin](https://github.com/pushkin-consortium/pushkin) | Platform for large-scale citizen-science online psychology experiments. | JS (React/Node); Docker | Yes |
| [psychTestR](https://pmcharrison.github.io/psychTestR/) | R package for behavioral experiment interfaces, strong in adaptive testing. | R (Shiny) | Yes (Shiny) |
| [Tatool Web](https://www.tatool.ch) | Framework for cognitive training and experimental tasks with a built-in task library. | JavaScript (AngularJS) | Yes |
| [Collector](https://github.com/gikeymarcia/Collector) | Web-based experiment platform using spreadsheet-like trial definitions. | PHP, JS, MySQL | Yes |

### Commercial / Freemium

| Platform | Description | Language / Tech | Online Support |
|----------|-------------|-----------------|----------------|
| [Gorilla](https://gorilla.sc) | Cloud-based drag-and-drop experiment builder with participant recruitment integration. | Web GUI; JS/HTML/CSS | Yes |
| [Pavlovia](https://pavlovia.org) | Hosting platform integrated with PsychoPy. Supports PsychoJS, jsPsych, and lab.js experiments. | Web platform; JS | Yes |
| [Inquisit (Millisecond)](https://www.millisecond.com) | Precise psychological measurement software with a 900+ test library. Desktop and web versions. | Proprietary scripting | Yes (Inquisit Web) |
| [E-Prime](https://pstnet.com/products/e-prime/) | Widely used in lab-based cognitive/neuro research. Precise timing, EEG/fMRI integration. | E-Basic (VB-like) | Limited (E-Prime Go) |
| [PsyToolkit](https://www.psytoolkit.org) | Free toolkit for online experiments and surveys with a built-in experiment library. | Custom scripting | Yes |
| [Testable](https://www.testable.org) | Web-based experiment platform with a graphical editor and template library. | Web GUI; JS | Yes |
| [FindingFive](https://www.findingfive.com) | Cloud platform using a grammar-based study design approach. | JSON-like grammar | Yes |
| [Labvanced](https://www.labvanced.com) | No-code experiment builder with 600+ templates. Supports webcam eye-tracking. | Web GUI (proprietary) | Yes |
| [Cognition.run](https://www.cognition.run) | Free hosting platform for jsPsych experiments with automatic data collection. | Hosts jsPsych / JS | Yes |

### Hosting & Backend Services

| Service | Description | Hosts Experiments From |
|---------|-------------|------------------------|
| [JATOS](https://www.jatos.org) | Open-source server for managing and running online experiments. | jsPsych, lab.js, OSWeb, PsychoJS, any HTML/JS |
| [MindProbe](https://mindprobe.eu) | Free JATOS-based hosting by the European Society for Cognitive Psychology (ESCoP). | jsPsych, lab.js, OSWeb, PsychoJS |
| [Open Lab](https://open-lab.online) | Free platform for hosting and sharing lab.js and jsPsych experiments. | lab.js, jsPsych |
| [Cognition.run](https://www.cognition.run) | Free hosting with simple upload and CSV data download. | jsPsych, lab.js |

---

## Repositories & Collections

Where to find ready-made experiment implementations.

| Collection | Platform | Approx. Tasks | Description |
|------------|----------|---------------|-------------|
| [Millisecond Test Library](https://www.millisecond.com/download/library) | Inquisit | 909 | Largest single library — covers nearly all domains of psychology. |
| [Labvanced Templates](https://www.labvanced.com/content/research/en/tasks/) | Labvanced | 600+ | Pre-loaded templates across cognitive, developmental, and behavioral economics. |
| [Pavlovia Explore](https://pavlovia.org/explore) | PsychoPy/jsPsych/lab.js | Thousands | Public experiments shared by the community on Pavlovia's GitLab. |
| [Gorilla Open Materials](https://app.gorilla.sc/openmaterials) | Gorilla | Hundreds | Open-access experiments, tasks, and questionnaires. |
| [E-Prime Experiment Library](https://support.pstnet.com/hc/en-us/categories/115000077168) | E-Prime | 150+ | Ready-to-run experiments across core domains. |
| [PEBL Test Battery](https://pebl.sourceforge.net) | PEBL | 100+ | Built-in battery of cognitive tests. |
| [The Experiment Factory](https://expfactory.github.io) | jsPsych/Docker | 80+ | Reproducible web-based experiments in Docker containers. |
| [PsyToolkit Experiment Library](https://www.psytoolkit.org/experiment-library/) | PsyToolkit | 50+ | Free library of classic cognitive experiments with source code. |
| [Testable Library](https://www.testable.org/library) | Testable | 50+ | Ready-made classic experiment templates. |
| [jsPsych Contrib](https://github.com/jspsych/jspsych-contrib) | jsPsych | 30+ plugins | Community-contributed plugins and extensions. |
| [jsPsych Experiment Demos](https://github.com/jspsych/experiment-demos) | jsPsych | Demos | Full example experiments from the jsPsych team. |
| [Niv Lab jsPsych Demos](https://nivlab.github.io/jspsych-demos/) | jsPsych | Demos | Complete task implementations with interactive demos. |
| [PsychoPyParadigms](https://github.com/djangraw/PsychoPyParadigms) | PsychoPy | Varies | Community collection of PsychoPy experiment implementations. |
| [NCMlab/CognitiveTasks](https://github.com/NCMlab/CognitiveTasks) | Various | Varies | Cognitive assessment tasks with GUIs. |
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

### Attention

| Task | Description | Key Reference |
|------|-------------|---------------|
| Stroop Task | Name the ink color of color-words (e.g., "RED" in blue ink). Measures selective attention and inhibitory control. | Stroop, 1935 |
| Eriksen Flanker Task | Respond to a central target flanked by congruent or incongruent distractors. Measures focused attention and response conflict. | Eriksen & Eriksen, 1974 |
| Visual Search | Search for a target among distractors. Set-size effects reveal parallel (pop-out) vs. serial search. | Treisman & Gelade, 1980 |
| Posner Cueing Task | Spatial cue (valid/invalid) precedes a target. Measures covert attentional orienting and disengagement. | Posner, 1980 |
| Attentional Blink | Detect two targets in a rapid serial visual presentation (RSVP) stream. The second target is often missed at 200–500 ms lag. | Raymond, Shapiro, & Arnell, 1992 |
| Attention Network Test (ANT) | Combines Flanker with cue conditions to independently measure alerting, orienting, and executive attention networks. | Fan et al., 2002 |
| Continuous Performance Task (CPT) | Respond to infrequent targets in a sustained stimulus stream. Measures vigilance and impulsivity. | Rosvold et al., 1956 |
| Dichotic Listening | Different messages to each ear; shadow one. Measures selective auditory attention. | Cherry, 1953 |
| Multiple Object Tracking (MOT) | Track a subset of moving objects among identical distractors. Measures attentional capacity across space and time. | Pylyshyn & Storm, 1988 |
| Useful Field of View (UFOV) | Identify a central target while localizing a peripheral target. Measures spatial extent of attentional processing. | Ball et al., 1988 |
| Global/Local (Navon) Task | Identify the global or local level of hierarchical stimuli (large letter made of small letters). | Navon, 1977 |
| Inhibition of Return (IOR) | Posner cueing variant with long intervals — slower RTs at previously cued locations. | Posner & Cohen, 1984 |
| Inattentional Blindness | Failure to notice an unexpected stimulus during an attention-demanding primary task. | Simons & Chabris, 1999 |
| Sustained Attention to Response Task (SART) | Respond to every stimulus except an infrequent target (reverse CPT). Commission errors index attention lapses and mind-wandering. | Robertson et al., 1997 |
| Rapid Visual Information Processing (RVP) | Detect target sequences (e.g., three consecutive odd numbers) in a pseudo-random digit stream. Measures sustained visual attention. | Sahakian & Owen, 1992 |
| Negative Priming | Respond to a target that was a distractor on the preceding trial. Slowed RTs reflect lingering inhibition of previously ignored stimuli. | Tipper, 1985 |
| Dual-Task Paradigm | Perform two tasks simultaneously. Performance costs reveal capacity limits and attentional resource allocation. | Pashler, 1994 |
| Psychological Refractory Period (PRP) | Two stimuli at varying SOAs each require a response. RT2 increases at short SOAs, revealing a central processing bottleneck. | Telford, 1931 |
| Exogenous vs. Endogenous Cueing | Compare peripheral flash (reflexive) vs. central arrow (voluntary) cues to separate reflexive from voluntary orienting. | Jonides, 1981 |
| RSVP Single-Target Detection | Detect a single target in a rapid stream of items (~10/sec). Measures temporal attention resolution. | Potter, 1975 |

### Memory

| Task | Description | Key Reference |
|------|-------------|---------------|
| N-back | Indicate whether the current stimulus matches the one N items back. Working memory updating; difficulty scales with N. | Kirchner, 1958 |
| Sternberg Task | Judge whether a probe was in a previously shown memory set. RT increases linearly with set size. | Sternberg, 1966 |
| Free Recall | Study a list, then recall items in any order. Serial position effects reveal storage/retrieval dynamics. | Murdock, 1962 |
| Recognition Memory | Distinguish old from new items after study. Analyzed with signal detection theory (d', criterion). | Mandler, 1980 |
| Corsi Block-Tapping | Reproduce a sequence of block taps. Measures visuospatial working memory span. | Corsi, 1972 |
| Digit Span (Forward/Backward) | Repeat digit sequences in order or reverse. Forward = storage; backward = storage + manipulation. | Wechsler, 1939 |
| Operation Span (OSPAN) | Alternate between math problems and remembering items. Measures WM capacity under dual-task load. | Turner & Engle, 1989 |
| Change Detection (Visual WM) | Judge whether an item changed in a briefly viewed array after a delay. Estimates visual WM capacity (Cowan's K). | Luck & Vogel, 1997 |
| Paired Associates Learning | Learn arbitrary pairs (e.g., word–word); tested via cued recall. Measures associative memory binding. | Calkins, 1894 |
| Deese-Roediger-McDermott (DRM) | Study semantically related words; frequently falsely recall/recognize the non-presented critical lure. | Roediger & McDermott, 1995 |
| Rey Auditory Verbal Learning Test (RAVLT) | 15-word list across five learning trials, interference list, delayed recall. Measures verbal learning and retention. | Rey, 1941 |
| Serial Recall | Recall items in exact presentation order. Reveals phonological similarity and word-length effects. | Conrad & Hull, 1964 |
| Reading Span | Read sentences while remembering final words. Measures WM capacity in a language context. | Daneman & Carpenter, 1980 |
| Directed Forgetting | Some items cued "forget," others "remember." Comparing memory for each reveals intentional memory control. | Bjork, 1970 |
| Prospective Memory | Remember to perform a future action while engaged in an ongoing task. | Einstein & McDaniel, 1990 |
| Source Memory | Recall contextual details about how/where information was learned. Measures episodic source monitoring. | Johnson, Hashtroudi, & Lindsay, 1993 |
| Delayed Matching to Sample (DMS) | Match a complex visual pattern to alternatives after a delay. Measures short-term visual recognition memory. | Sahakian et al., 1988 |
| Pattern Recognition Memory (PRM) | Recognize previously seen abstract visual patterns among novel foils. Measures visual pattern recognition. | Sahakian & Owen, 1992 |
| Retrieval-Induced Forgetting (RIF) | Practicing retrieval of some category members impairs recall of related unpracticed items. Reveals inhibitory retrieval processes. | Anderson, Bjork, & Bjork, 1994 |
| Think/No-Think Paradigm | After learning word pairs, suppress retrieval of some targets when cued. Tests voluntary memory suppression. | Anderson & Green, 2001 |
| Spatial Recognition Memory (SRM) | Remember spatial locations and discriminate old from novel locations after a delay. | Owen et al., 1995 |
| Brief Visuospatial Memory Test (BVMT-R) | Copy and recall geometric figures across learning trials. Tests visuospatial learning and delayed recall. | Benedict, 1997 |
| List Sorting Working Memory Test | Reorder sequences of visually and orally presented stimuli (e.g., animals by size). NIH Toolbox WM measure. | Tulsky et al., 2014 |
| Part-Set Cuing | Providing some list items as cues paradoxically impairs recall of remaining items. Demonstrates retrieval competition. | Slamecka, 1968 |

### Executive Function

| Task | Description | Key Reference |
|------|-------------|---------------|
| Wisconsin Card Sorting Test (WCST) | Sort cards by an unknown, shifting rule. Perseverative errors measure cognitive flexibility. | Berg, 1948 |
| Tower of London / Hanoi | Rearrange disks to match a goal in minimum moves. Measures planning and problem-solving. | Shallice, 1982 |
| Go/No-Go | Respond to frequent "go" stimuli, withhold to "no-go." Measures response inhibition. | Donders, 1868 |
| Stop-Signal Task | Cancel an initiated response when a stop signal appears. SSRT estimates inhibitory control speed. | Logan & Cowan, 1984 |
| Task Switching | Alternate between tasks; switch cost measures mental set reconfiguration. | Rogers & Monsell, 1995 |
| Trail Making Test (TMT) | Part A: connect numbers. Part B: alternate numbers and letters. B–A indexes cognitive flexibility. | Reitan, 1958 |
| Simon Task | Respond based on a non-spatial feature while stimulus location is congruent/incongruent with the response. | Simon & Rudell, 1967 |
| Antisaccade | Look away from a peripheral stimulus. Measures inhibitory control of eye movements. | Hallett, 1978 |
| Verbal Fluency (FAS / Category) | Generate words starting with a letter or from a category within a time limit. | Thurstone, 1938 |
| AX-CPT | Respond to A-then-X sequences; measures proactive vs. reactive cognitive control. | Braver et al., 2001 |
| Hayling Sentence Completion | Complete sentences with a congruent word (Part A), then an incongruent word (Part B). Part B = suppression. | Burgess & Shallice, 1997 |
| Brixton Spatial Anticipation | Predict dot position as rules change. Errors after rule changes measure set-shifting. | Burgess & Shallice, 1997 |
| Intra-Extra Dimensional Set Shift (IED) | Learn stimulus–reward rules based on one dimension, then shift to a new dimension. Separates intra- from extradimensional shifting. | Sahakian & Owen, 1992 |
| Stockings of Cambridge (SOC) | Plan a sequence of moves to match a goal arrangement of colored balls (computerized Tower of London). | Owen et al., 1990 |
| Dimensional Change Card Sort (DCCS) | Sort cards by one dimension (e.g., color), then switch to another (e.g., shape). NIH Toolbox EF measure. | Zelazo, 2006 |
| Pattern Comparison Processing Speed | Judge whether two side-by-side visual patterns are same or different as quickly as possible. NIH Toolbox processing speed measure. | Carlozzi et al., 2015 |
| Letter-Number Sequencing | Reorder intermixed letters and numbers (numbers ascending, letters alphabetical). Measures WM manipulation. | Gold et al., 1997 |
| Color-Word Interference (D-KEFS) | Extended Stroop with four conditions including inhibition/switching. Part of the Delis-Kaplan Executive Function System. | Delis, Kaplan, & Kramer, 2001 |

### Decision Making

| Task | Description | Key Reference |
|------|-------------|---------------|
| Iowa Gambling Task (IGT) | Choose from four decks with varying reward/punishment. Measures affective decision-making under ambiguity. | Bechara et al., 1994 |
| Balloon Analogue Risk Task (BART) | Pump a virtual balloon for increasing reward; risk losing all if it pops. Indexes risk-taking propensity. | Lejuez et al., 2002 |
| Delay Discounting | Choose between smaller-sooner and larger-later rewards. Discounting steepness measures impulsivity. | Mazur, 1987 |
| Cambridge Gambling Task (CGT) | Bet on outcomes with explicit probabilities displayed. Separates risk-taking from learning. | Rogers et al., 1999 |
| Ultimatum Game | Proposer splits money; responder accepts or rejects. Measures fairness norms and punishment. | Guth, Schmittberger, & Schwarze, 1982 |
| Dictator Game | One player allocates money to a passive other. Purer measure of altruism/prosocial preferences. | Kahneman, Knetsch, & Thaler, 1986 |
| Trust Game | Investor sends money (multiplied) to trustee who decides return. Measures trust and reciprocity. | Berg, Dickhaut, & McCabe, 1995 |
| Prisoner's Dilemma | Cooperate or defect; iterated versions measure cooperation strategies. | Axelrod, 1984 |
| Public Goods Game | Contribute to a shared pool (multiplied, redistributed). Measures cooperation and free-riding. | Ledyard, 1995 |
| Effort-Based Decision Making (EEfRT) | Choose low-effort/low-reward vs. high-effort/high-reward tasks. Measures motivation and effort discounting. | Treadway et al., 2009 |
| Trolley Dilemma | Decide whether to divert a trolley to kill one person to save five. Classic moral dilemma indexing utilitarian reasoning. | Foot, 1967; Greene et al., 2001 |
| Footbridge Dilemma | Decide whether to push a person to stop a trolley killing five. "Personal" moral dilemma engaging stronger emotional processing. | Thomson, 1985; Greene et al., 2001 |
| Pavlovian-to-Instrumental Transfer (PIT) | Pavlovian cues associated with outcomes bias instrumental responding toward the associated action. | Holland, 2004 |
| Outcome Devaluation | After learning an action–outcome association, the outcome is devalued. Sensitivity distinguishes goal-directed from habitual behavior. | Adams & Dickinson, 1981 |
| Decisions from Experience | Participants sample from payoff distributions before choosing, rather than seeing described probabilities. Reveals the description–experience gap. | Hertwig et al., 2004 |
| Beads Task (Jumping to Conclusions) | Draw beads from jars of known ratios; decide which jar they come from. Fewer draws = jumping to conclusions bias. | Huq, Garety, & Hemsley, 1988 |
| Moral Foundations Questionnaire | Rate the relevance of moral principles (care, fairness, loyalty, authority, purity) to moral judgments. | Graham et al., 2011 |

### Perception

| Task | Description | Key Reference |
|------|-------------|---------------|
| Mental Rotation | Judge whether two rotated 3D objects are same or mirror images. RT scales with angular disparity. | Shepard & Metzler, 1971 |
| Gabor Patch Detection | Detect presence/orientation of Gabor patches at varying contrasts. Measures visual sensitivity. | Watson & Pelli, 1983 |
| Random Dot Motion (RDK) | Judge global motion direction with varying coherence levels. Measures motion perception and perceptual decision-making. | Newsome & Pare, 1988 |
| Change Detection (Perceptual) | Detect differences between alternating scene versions separated by a blank. | Rensink, O'Regan, & Clark, 1997 |
| Muller-Lyer Illusion | Judge line lengths with inward/outward arrowheads. Measures susceptibility to geometric illusions. | Muller-Lyer, 1889 |
| Psychophysical Staircase | Stimulus intensity adjusted trial-by-trial to converge on perceptual threshold. | Levitt, 1971 |
| Binocular Rivalry | Different images to each eye; perception alternates. Probes perceptual competition and conscious awareness. | Blake & Logothetis, 2002 |
| Embedded Figures Test | Locate a simple shape within a complex pattern. Measures field independence. | Witkin et al., 1971 |
| Contour Integration | Detect aligned Gabor elements forming a path among random elements. Measures contour grouping. | Field, Hayes, & Hess, 1993 |
| Temporal Order Judgment (TOJ) | Report which of two stimuli appeared first. Measures temporal resolution. | Sternberg & Knoll, 1973 |
| Biological Motion (Point-Light Walker) | Identify actions from sparse point-light displays. | Johansson, 1973 |
| Judgment of Line Orientation (JLO) | Match the orientation of two angled lines to a response array. Measures visuospatial perception. | Benton et al., 1978 |
| Continuous Flash Suppression (CFS) | High-contrast dynamic patterns to one eye suppress a static target in the other from awareness. Measures unconscious visual processing. | Tsuchiya & Koch, 2005 |
| Backward Masking | A briefly presented target is immediately followed by a mask, rendering it invisible. Measures temporal limits of conscious perception. | Breitmeyer & Ogmen, 2000 |
| Apparent Motion | Two spatially separated stimuli in alternation produce the illusion of movement. Probes motion correspondence mechanisms. | Wertheimer, 1912 |
| Time Reproduction / Interval Timing | Reproduce the duration of a presented interval. Measures internal clock precision and scalar timing. | Gibbon, Church, & Meck, 1984 |
| Simultaneity Judgment (SJ) | Judge whether two stimuli appeared at the same time or at different times. Measures temporal binding window. | Hirsh & Sherrick, 1961 |
| Crowding | Identify a peripheral target flanked by nearby distractors. Impaired identification probes spatial limits of object recognition. | Bouma, 1970 |
| Vernier Acuity | Judge the offset of two line segments. Measures hyperacuity — spatial resolution finer than photoreceptor spacing. | Westheimer & McKee, 1977 |

### Language

| Task | Description | Key Reference |
|------|-------------|---------------|
| Lexical Decision | Classify letter strings as real words or nonwords. Reveals lexical access speed and word frequency effects. | Meyer & Schvaneveldt, 1971 |
| Semantic Priming | A related prime speeds target recognition. Measures spreading activation in semantic memory. | Neely, 1977 |
| Reading Span | Read sentences while remembering final words. WM capacity in a language context. | Daneman & Carpenter, 1980 |
| Picture Naming | Name depicted objects as quickly as possible. Sensitive to lexical retrieval and word frequency. | Snodgrass & Vanderwart, 1980 |
| Word Naming (Pronunciation) | Read aloud presented words. Naming latency reflects phonological encoding and regularity effects. | Coltheart et al., 2001 |
| Self-Paced Reading | Press a key to reveal each word; reading times at critical regions reveal parsing strategies. | Just, Carpenter, & Woolley, 1982 |
| Visual World Paradigm | Eye movements to objects during spoken language reveal real-time word recognition. | Tanenhaus et al., 1995 |
| Sentence Verification | Judge true/false (e.g., "A canary is a bird"). Indexes category typicality. | Collins & Quillian, 1969 |
| Sentence Completion (Cloze) | Complete a sentence with the most likely word. Cloze probability used in ERP research (N400). | Taylor, 1953 |
| Phoneme Monitoring | Detect a target phoneme in speech. Measures speech segmentation. | Foss, 1969 |
| Nonword Repetition | Repeat novel nonsense words of increasing length. Measures phonological short-term memory. | Gathercole & Baddeley, 1990 |
| Syntactic Priming | Exposure to a syntactic structure (e.g., passive) increases production of that structure in subsequent sentences. | Bock, 1986 |
| Garden Path Sentences | Sentences with temporary syntactic ambiguity lead to initial misparse and recovery. Reading time increase measures reanalysis. | Frazier & Rayner, 1982 |
| Cross-Modal Priming | Auditory sentence + visual word probe at critical points. RT to probe reveals real-time lexical activation during speech. | Swinney, 1979 |
| Word Superiority Effect | Letters identified more accurately when embedded in words than in nonwords or alone. Demonstrates top-down influence. | Reicher, 1969 |
| Masked Priming | A very briefly presented, masked prime word facilitates recognition of a related target. Reveals automatic lexical processing. | Forster & Davis, 1984 |
| Picture Vocabulary Test | Select from four pictures the one matching a spoken word. NIH Toolbox receptive vocabulary measure. | Gershon et al., 2014 |
| Oral Reading Recognition | Read aloud single words of increasing difficulty. NIH Toolbox reading decoding measure. | Gershon et al., 2014 |

### Social Cognition

| Task | Description | Key Reference |
|------|-------------|---------------|
| Reading the Mind in the Eyes (RMET) | Infer mental states from photographs of the eye region. Measures advanced theory of mind. | Baron-Cohen et al., 2001 |
| Implicit Association Test (IAT) | Rapidly categorize stimuli along two dimensions; RT difference measures implicit bias. | Greenwald, McGhee, & Schwartz, 1998 |
| Cambridge Face Memory Test | Learn and identify faces. Measures face recognition ability. | Duchaine & Nakayama, 2006 |
| False Belief Task (Sally-Anne) | Predict where a character will look for an object moved in their absence. First-order theory of mind. | Wimmer & Perner, 1983 |
| Cyberball | Virtual ball-tossing game where the participant is gradually excluded. Measures social exclusion effects. | Williams, Cheung, & Choi, 2000 |
| Heider-Simmel Animation | Describe movements of geometric shapes. Reveals spontaneous social/intentional attribution. | Heider & Simmel, 1944 |
| Faux Pas Recognition | Identify social faux pas in stories. Measures advanced theory of mind. | Baron-Cohen et al., 1999 |
| Gaze Cueing | A central face looks left/right before a target. Measures automatic social attention following. | Friesen & Kingstone, 1998 |
| Face Inversion Effect | Recognize upright vs. inverted faces. Disproportionate inversion cost demonstrates configural face processing. | Yin, 1969 |
| Asch Conformity Paradigm | Judge line lengths after confederates give unanimously wrong answers. Measures conformity to social pressure. | Asch, 1951 |
| Milgram Obedience Paradigm | Administer apparent electric shocks under authority instruction. Measures obedience to authority figures. | Milgram, 1963 |
| Minimal Group Paradigm | Categorize participants into arbitrary groups; measure in-group favoritism in resource allocation. | Tajfel et al., 1971 |
| Strange Situation | Caregiver–infant separations and reunions in a structured lab setting. Classifies attachment styles. | Ainsworth et al., 1978 |
| Director Task | Take into account another person's visual perspective when selecting objects. Measures perspective-taking. | Keysar et al., 2000 |
| Empathy for Pain Paradigm | Observe another person receiving a painful stimulus while neural/physiological responses are measured. | Singer et al., 2004 |

### Learning

| Task | Description | Key Reference |
|------|-------------|---------------|
| Probabilistic Learning (Two-Armed Bandit) | Choose between options with different reward probabilities. Modeled with reinforcement learning. | Daw et al., 2006 |
| Serial Reaction Time (SRT) | Respond to stimuli in a repeating spatial sequence. RT speedup indexes implicit sequence learning. | Nissen & Bullemer, 1987 |
| Weather Prediction Task | Predict outcomes from probabilistic cue combinations. Dissociates declarative from procedural learning. | Knowlton, Squire, & Gluck, 1994 |
| Reversal Learning | After learning a stimulus–reward association, contingencies reverse. Measures flexibility in reward learning. | Dias, Robbins, & Roberts, 1996 |
| Fear Conditioning and Extinction | Tone (CS) paired with shock (US); CS alone then elicits fear. Extinction via CS-alone trials. | Phelps et al., 2004 |
| Statistical Learning | Exposure to streams with embedded regularities. Sensitivity to transitional probabilities measures implicit learning. | Saffran, Aslin, & Newport, 1996 |
| Artificial Grammar Learning | Study strings from a finite-state grammar; classify new strings as grammatical or not. | Reber, 1967 |
| Contextual Cueing | Repeated spatial configurations speed visual search without explicit awareness. | Chun & Jiang, 1998 |
| Information Integration Category Learning | Categorize stimuli by integrating multiple dimensions (not easily verbalized). Relies on implicit systems. | Ashby & Maddox, 2005 |
| Classical (Pavlovian) Conditioning | Neutral stimulus paired with US until it elicits a conditioned response. | Pavlov, 1927 |
| Latent Inhibition | Pre-exposure to a stimulus without consequences retards subsequent conditioning to that stimulus. Measures learned irrelevance. | Lubow & Moore, 1959 |
| Sensory Preconditioning | Two neutral stimuli are paired; one is then conditioned. Testing the other reveals indirect associative transfer. | Brogden, 1939 |
| Trace Conditioning | CS offset precedes US onset by a temporal gap. Requires hippocampal-dependent bridging of the CS–US gap. | Clark & Squire, 1998 |
| Sign-Tracking vs. Goal-Tracking | After Pavlovian conditioning, some subjects approach the predictive cue (sign) while others approach the reward location (goal). | Robinson & Flagel, 2009 |
| Visuomotor Rotation Adaptation | Cursor feedback is rotated relative to hand movement; participants gradually adapt. Measures sensorimotor error-based learning. | Krakauer et al., 2000 |
| Instrumental (Operant) Conditioning | Participants learn that actions produce specific outcomes. Schedule manipulations measure goal-directed vs. habitual learning. | Skinner, 1938 |

### Emotion

| Task | Description | Key Reference |
|------|-------------|---------------|
| Emotional Stroop | Name ink color of emotionally valenced words. Slowed naming for emotional words indexes attentional capture. | Williams, Mathews, & MacLeod, 1996 |
| Dot Probe (Attentional Bias) | Probe replaces one of two stimuli (emotional/neutral). Faster detection at emotional location = attentional bias. | MacLeod, Mathews, & Tata, 1986 |
| Affective Go/No-Go | Respond to one emotional category, withhold to another. Measures emotion–inhibition interaction. | Murphy et al., 1999 |
| Emotion Recognition (Ekman Faces) | Label facial expressions of the six basic emotions. Measures facial emotion recognition accuracy. | Ekman & Friesen, 1976 |
| Emotion Regulation Task | Reappraise, suppress, or attend to emotional images. Indexes regulation strategy effectiveness. | Ochsner et al., 2004 |
| IAPS Viewing | View standardized emotional images while physiological/neural responses are measured. | Lang, Bradley, & Cuthbert, 1997 |
| Affective Priming | Emotional prime facilitates/inhibits evaluation of a subsequent target. Measures automatic affective processing. | Fazio et al., 1986 |
| Emotional Flanker | Emotional distractors flank a central target. Measures involuntary attentional capture by emotional stimuli. | Fenske & Eastwood, 2003 |
| Startle Reflex Modulation | Eyeblink startle to sudden noise during emotional images — potentiated during negative, attenuated during positive. | Lang, Bradley, & Cuthbert, 1990 |
| Mood Induction Procedures | Film clips, music, or recall used to induce transient mood states as experimental variables. | Westermann et al., 1996 |
| Approach-Avoidance Task (AAT) | Push/pull a joystick in response to emotional stimuli. Congruence effects reveal automatic approach/avoidance tendencies. | Rinck & Becker, 2007 |
| Fear-Potentiated Startle | Startle probe during a fear-conditioned stimulus produces enhanced eyeblink. Measures conditioned fear physiologically. | Davis, 1986 |
| Trier Social Stress Test (TSST) | Public speaking + mental arithmetic before evaluators. Gold-standard lab stress induction producing cortisol responses. | Kirschbaum, Pirke, & Hellhammer, 1993 |
| Emotional Faces Dot Probe | Dot-probe variant using emotional faces. Widely used in anxiety and depression research for attentional bias to threat. | Mogg, Philippot, & Bradley, 2004 |
| Facial Action Coding System (FACS) Paradigm | Systematically code facial muscle movements (Action Units) to measure spontaneous emotional expression. | Ekman & Friesen, 1978 |

### Creativity

| Task | Description | Key Reference |
|------|-------------|---------------|
| Alternate Uses Task (AUT) | Generate as many unusual uses for a common object (e.g., brick) as possible. Scores fluency, flexibility, and originality. | Guilford, 1967 |
| Remote Associates Test (RAT) | Given three words (e.g., "falling, actor, dust"), find a fourth linking them all ("star"). Measures convergent creative thinking. | Mednick, 1962 |
| Compound Remote Associates (CRA) | Given three compound-word stems, find the word that completes all three. Modernized RAT variant. | Bowden & Jung-Beeman, 2003 |
| Torrance Tests of Creative Thinking (TTCT) | Battery of verbal and figural tasks yielding fluency, flexibility, originality, and elaboration scores. | Torrance, 1966 |
| Insight Problems (Matchstick, Nine-Dot) | Solve problems requiring restructuring of the initial representation. Measures insight vs. analytic problem solving. | Metcalfe & Wiebe, 1987 |
| Consensual Assessment Technique (CAT) | Experts independently rate creative products (stories, collages, poems). Measures real-world creative output. | Amabile, 1982 |

### Metacognition

| Task | Description | Key Reference |
|------|-------------|---------------|
| Judgment of Learning (JOL) | After studying each item, predict the likelihood of recalling it later. Accuracy measures metacognitive monitoring. | Nelson & Dunlosky, 1991 |
| Feeling of Knowing (FOK) | After failing to recall, judge the likelihood of recognizing the item later. Prospective metacognitive judgment. | Hart, 1965 |
| Retrospective Confidence Judgment (RCJ) | Rate confidence in the correctness of a just-given response. Calibration and resolution metrics measure metacognitive accuracy. | Koriat, 2007 |
| Tip-of-the-Tongue (TOT) Paradigm | Retrieve answers to general knowledge questions; report TOT states. Measures retrieval failure awareness. | Brown & McNeill, 1966 |
| Perceptual Confidence / Meta-d' | After perceptual discrimination, rate confidence. Meta-d' quantifies metacognitive sensitivity independently of task performance. | Maniscalco & Lau, 2012 |
| Ease of Learning (EOL) | Before study, judge how easy each item will be to learn. Measures pre-study metacognitive prediction. | Underwood, 1966 |

### Motor Control

| Task | Description | Key Reference |
|------|-------------|---------------|
| Finger Tapping Task | Tap a key as fast as possible (or at a specified rate). Measures motor speed, rhythm, and lateralization. | Reitan & Wolfson, 1985 |
| Purdue Pegboard | Place pegs into holes as quickly as possible with each hand and both together. Measures fine manual dexterity. | Tiffin & Asher, 1948 |
| Fitts's Law Pointing | Move to targets of varying distance and width. Movement time scales logarithmically with index of difficulty. | Fitts, 1954 |
| Force-Field Adaptation | A robotic arm applies velocity-dependent forces during reaching; participants learn to compensate. Measures internal model formation. | Shadmehr & Mussa-Ivaldi, 1994 |
| Grip Force Task | Lift an object and maintain stable grip; perturbations reveal predictive and reactive force control. | Johansson & Westling, 1988 |
| Mirror Tracing | Trace a shape while viewing only a mirror reflection. Measures visuomotor adaptation and procedural learning. | Milner, 1962 |
| Visuomotor Rotation Task | Cursor feedback is rotated relative to hand movement; participants adapt reaching over trials. Measures sensorimotor adaptation. | Krakauer, 2009 |

### Numerical Cognition

| Task | Description | Key Reference |
|------|-------------|---------------|
| Number Comparison (Symbolic) | Judge which of two Arabic digits is larger. Distance effect reveals analogue magnitude representation. | Moyer & Landauer, 1967 |
| SNARC Task | Classify numbers while responding left/right. Faster left responses to small numbers reveals spatial–numerical mapping. | Dehaene, Bossini, & Giraux, 1993 |
| Subitizing | Enumerate briefly flashed dot arrays. Fast and accurate for 1–4 items (subitizing range), slower beyond. | Kaufman et al., 1949 |
| Approximate Number System (ANS) Task | Judge which of two dot arrays is more numerous (non-symbolic). Ratio-dependent accuracy indexes ANS precision. | Halberda, Mazzocco, & Feigenson, 2008 |
| Number Line Estimation | Place a number on a physical line anchored at 0 and 100/1000. Shift from logarithmic to linear mapping tracks development. | Siegler & Opfer, 2003 |

### Developmental

| Task | Description | Key Reference |
|------|-------------|---------------|
| A-not-B Error Task | Infant searches at location A after repeated finds there, even after watching the toy moved to B. Measures object permanence. | Piaget, 1954; Diamond, 1985 |
| Conservation Task | Transform the appearance of a quantity (e.g., pour water into a taller glass) and ask if the amount changed. Piagetian concrete operations. | Piaget, 1952 |
| Violation of Expectation (VoE) | Infants look longer at "impossible" events (e.g., object through solid barrier). Looking time indexes early physical knowledge. | Baillargeon, Spelke, & Wasserman, 1985 |
| Preferential Looking | Present two stimuli side by side; differential looking time reveals visual preference or discrimination in pre-verbal infants. | Fantz, 1961 |
| Marshmallow Test (Delay of Gratification) | Child chooses one marshmallow now or waits for two. Measures self-control and delay of gratification in preschoolers. | Mischel, Shoda, & Rodriguez, 1989 |
| Picture Sequence Memory | Remember and reproduce the order of a sequence of activity pictures. NIH Toolbox episodic memory measure for all ages. | Bauer et al., 2013 |

### Clinical / Screening

| Task | Description | Key Reference |
|------|-------------|---------------|
| Mini-Mental State Examination (MMSE) | 30-point screening covering orientation, registration, attention, recall, and language. Global cognitive screening tool. | Folstein, Folstein, & McHugh, 1975 |
| Montreal Cognitive Assessment (MoCA) | Brief screening for mild cognitive impairment across visuospatial, executive, memory, attention, language, and orientation. | Nasreddine et al., 2005 |
| Repeatable Battery for Assessment of Neuropsychological Status (RBANS) | Brief battery spanning immediate memory, visuospatial, language, attention, and delayed memory. | Randolph et al., 1998 |
| Symbol Digit Modalities Test (SDMT) | Match symbols to digits using a key as quickly as possible. Measures processing speed and incidental learning. | Smith, 1982 |
| Clock Drawing Test | Draw a clock face showing a specified time. Screens for visuospatial, executive, and semantic deficits. | Freedman et al., 1994 |

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

## License

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)
