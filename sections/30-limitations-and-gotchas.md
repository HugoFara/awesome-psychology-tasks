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
