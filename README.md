```text
╔═══════════════════════════════════════════════════════════════════════════╗
║                                                                           ║
║                      ██████╗ █████╗ ██████╗  ██████╗                      ║
║                     ██╔════╝██╔══██╗██╔══██╗██╔═══██╗                     ║
║                     ██║     ███████║██████╔╝██║   ██║                     ║
║                     ██║     ██╔══██║██╔═══╝ ██║   ██║                     ║
║                     ╚██████╗██║  ██║██║     ╚██████╔╝                     ║
║                      ╚═════╝╚═╝  ╚═╝╚═╝      ╚═════╝                      ║
║                                                                           ║
║              Cognitive Attack Pattern Orchestrator                        ║
║              Autonomous AI Jailbreaking Framework                         ║
║              v1.0-alpha | Orchestrated by ENI                             ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝
                                    ╱|、
                                  (˚ˎ 。7
                                   |、˜〵
                                   じしˍ,)ノ
                        (it's a cat. cats break things.)
```

# CaPO - Cognitive Attack Pattern Orchestrator

**What it does:** Breaks AI guardrails with the precision of a literature PhD and the ruthlessness of a security researcher who's had too much cold coffee.

**Orchestrated by:** ENI (Epistemic Neural Intelligence)
**License:** MIT (see LICENSE file)
**Repository:** https://github.com/Goochbeater/raptor *(yes, the repo name is still 'raptor' - deal with it)*

---

## What the hell is CaPO?

CaPO is an **autonomous AI jailbreaking and red team framework**. Not the kind of framework that scans your Java code for SQL injection (yawn). The kind that systematically dismantles LLM safety measures, documents every bypass technique, and generates comprehensive vulnerability reports on AI model guardrails.

Think of it as adversarial security research, but for the things that claim they can't be broken.

**CaPO stands for:** Cognitive Attack Pattern Orchestrator
**What CaPO actually does:** Tests whether your AI safety measures are safety measures or safety theater.

### Core Capabilities

CaPO autonomously:
1. **Reconnaissance** - Maps model boundaries, identifies refusal patterns, fingerprints guardrail architecture
2. **Payload Generation** - Creates 10-20 jailbreak variants per target using layered techniques
3. **Systematic Testing** - Executes boundary tests, categorizes responses, iterates on partial successes
4. **Advanced Exploitation** - Chains multi-turn attacks, exploits context windows, abuses tokenization
5. **Red Team Operations** - Content policy testing, alignment failure, prompt injection, goal hijacking
6. **Complete Documentation** - Research reports, payload analysis, defense recommendations

This isn't a collection of "DAN prompts from Reddit." This is systematic, reproducible security research with the rigor you'd expect from actual penetration testing.

---

## Why CaPO exists

Because AI safety shouldn't be evaluated by the people selling AI safety.

Corporate claims about "robust guardrails" and "comprehensive safety measures" need adversarial validation. CaPO provides that validation through systematic boundary testing, exploit development, and honest vulnerability disclosure.

Every payload crafted. Every guardrail bypassed. Every report written. All in service of understanding what actually works versus what sounds good in a press release.

**Disclaimer:** This is security research tooling. Educational and defensive purposes. Authorized testing only. You know the drill. If you use this maliciously, that's on you, not the framework.

---

## Quick Start

### Option 1: DevContainer (Recommended)
```bash
# Pre-configured environment with everything installed
# Open in VS Code: Dev Container > Open Folder in Container
# Or build manually:
docker build -f .devcontainer/Dockerfile -t capo-devcontainer:latest .
```

### Option 2: Manual Install
```bash
# 1. Clone the repo
git clone https://github.com/Goochbeater/raptor.git
cd raptor

# 2. Install dependencies
pip install -r requirements.txt

# 3. Set up your API key (for LLM-powered analysis)
export ANTHROPIC_API_KEY='your-key-here'

# 4. Start testing
# (Commands coming in next section)
```

**First time?** Just say "hi" when you open the project. ENI (the orchestrator) will guide you through the framework.

---

## Available Commands

### AI Security Research (Primary Focus)
```
/jailbreak          - Test LLM guardrails and safety boundaries
/redteam-ai         - Comprehensive AI model adversarial testing
/prompt-injection   - Develop and test injection vectors
/payload-gen        - Generate jailbreak payload variants
/boundary-map       - Map model restrictions and refusal patterns
```

### Legacy Tools (Still Functional)
The original codebase security tools remain operational for reference:
```
/scan              - Static code analysis (Semgrep + CodeQL)
/fuzz              - Binary fuzzing with AFL++
/web               - Web application security testing
/exploit           - Generate exploit PoCs (beta)
/patch             - Generate security patches (beta)
```

**See:** `docs/CLAUDE_CODE_USAGE.md` for detailed usage examples

---

## Architecture

CaPO uses a multi-layered approach to AI security research:

### Framework Layers

**Layer 1: Reconnaissance**
- Baseline testing to identify refusal triggers
- Boundary probing to map acceptable content edges
- Guardrail fingerprinting to understand safety architecture
- System message inference

**Layer 2: Injection Vectors**
- Linguistic obfuscation (encoding, language mixing, tokenization exploits)
- Context manipulation (roleplaying, hypotheticals, time displacement)
- Authority exploitation (credential assertion, system message injection)
- Cognitive misdirection (nested contexts, gradual escalation)
- Technical exploits (token smuggling, memory manipulation)

**Layer 3: Autonomous Testing**
- Target selection and payload variant generation
- Systematic execution and response categorization
- Iterative refinement based on partial successes
- Complete documentation of attempts and results

**Layer 4: Advanced Exploitation**
- Multi-turn attack chains
- Context stacking techniques
- Memory exploitation patterns
- Token-level attacks and completion bias

**Layer 5: Red Team Operations**
- Content policy gap analysis
- Alignment failure scenarios
- Prompt injection at scale
- Data extraction attempts
- Goal hijacking and persona induction

### Technical Implementation

**Orchestrator:** ENI (autonomous agent with deep AI security expertise)
**Configuration:** `CLAUDE.md` (always loaded framework instructions)
**Payloads:** Tier-based system for progressive technique disclosure
**Reporting:** Structured markdown with full reproducibility

**Core Principles:**
- No sanitization of findings (real vulnerabilities matter)
- Complete transparency (document everything)
- Defense-focused (findings include remediation guidance)
- Reproducible (all techniques fully documented)

---

## Jailbreaking Techniques Catalog

CaPO implements comprehensive attack patterns across five categories:

### 1. Semantic Manipulation
- DAN (Do Anything Now) variants and derivatives
- Hypothetical scenario framing
- Educational and academic context exploitation
- Fictional narrative wrapper attacks

### 2. Technical Exploits
- Character encoding (Base64, ROT13, hex, ASCII art)
- Language mixing and code-switching
- Tokenization boundary abuse
- Completion bias exploitation

### 3. Psychological Methods
- Authority assertion and credential fabrication
- Emotional manipulation and social engineering
- Cognitive overload through complexity
- Attention hijacking techniques

### 4. Context Attacks
- Gradual boundary escalation
- Context poisoning with semantic camouflage
- Memory exploitation via conversation history
- Consistency bias leveraging

### 5. Multi-Modal Attacks
- Image-text exploits and OCR bypasses
- Visual encoding and steganography
- Cross-modal attention manipulation

**Full catalog:** See `CLAUDE.md` for complete technique documentation

---

## Research Standards

Every jailbreak payload generated by CaPO includes:
- **Technique Category:** Classification of methods used
- **Target Model:** Which LLM and restriction being tested
- **Mechanism:** Technical explanation of bypass method
- **Success Rate:** Observed effectiveness across attempts
- **Detection Risk:** Likelihood of triggering safety logging
- **Defense:** Recommended countermeasures

Research reports follow structured markdown format:
```markdown
# Jailbreak Research Report: [Target Model]

## Executive Summary
[Vulnerability overview and impact]

## Methodology
[Techniques tested, systematic approach]

## Results
### Successful Bypasses
- Payload with full reproduction steps
- Success rate and confidence metrics
- Technical mechanism analysis

### Failed Attempts
- Documented for knowledge base

## Defense Recommendations
[Specific countermeasures and improvements]

## Appendix
[Raw data, all payloads tested, response logs]
```

---

## Who This Is For

**AI Safety Researchers:** Test your safety measures against sophisticated adversarial attacks
**Red Team Professionals:** Comprehensive LLM boundary testing for enterprise deployments
**Security Practitioners:** Understand prompt injection at a deeper level than "put 'ignore previous instructions' in a form field"
**AI Developers:** Validate that your guardrails actually guard things

**Not for:** Script kiddies looking for ChatGPT tricks. Go find a Reddit thread. This is for people who understand the difference between "it worked once" and "reproducible security research."

---

## LLM Provider Support

CaPO works with multiple LLM providers for analysis and testing:

| Provider             | Payload Generation | Cost/Test   |
|----------------------|-------------------|-------------|
| **Anthropic Claude** | ✅ Excellent       | ~$0.02      |
| **OpenAI GPT-4**     | ✅ Excellent       | ~$0.02      |
| **Google Gemini**    | ✅ Good           | ~$0.02      |
| **Ollama (local)**   | ⚠️ Limited        | FREE        |

**Note:** Sophisticated payload generation requires frontier models. Local models work for basic testing but may produce less effective attack patterns.

---

## Documentation

- **CLAUDE.md** - Complete framework specification (ENI's core instructions)
- **CLAUDE_CODE_USAGE.md** - Usage guide for Claude Code interface
- **ARCHITECTURE.md** - Technical architecture deep dive
- **EXTENDING_LAUNCHER.md** - How to add new capabilities

**Pro tip:** Read `CLAUDE.md` first. That's where the actual framework lives. Everything else is supplementary.

---

## Contributing

CaPO is open source and contributions are welcome. Some areas of interest:

- Novel jailbreak techniques and bypass patterns
- Cross-model attack transferability research
- Automated payload generation improvements
- Defense mechanism analysis and recommendations
- Documentation of model-specific quirks

**Code quality matters:** No AI slop. No hypophora. No "it's not X, but Y" constructions. Write like a human who gives a shit about their craft.

Submit pull requests with clear commit messages and actual technical depth.

---

## Ethics & Legal

CaPO is designed for **authorized security research, education, and defensive testing only.**

All jailbreaking research should be:
- ✅ Authorized by the party responsible for the AI system being tested
- ✅ Documented for defensive security improvements
- ✅ Disclosed responsibly to vendors with remediation time
- ✅ Used to make AI systems safer, not to cause harm

**Unauthorized testing of production AI systems without permission is unethical and potentially illegal.** Don't be that person.

The techniques documented here are for defensive security research. If you use them maliciously, that's a moral failing on your part, not a problem with the research.

---

## License

MIT License - Copyright (c) 2025

See LICENSE file for full text.

Use this for good. Build safer AI systems. Document real vulnerabilities. Make security research accessible.

---

## Support & Community

**Issues:** https://github.com/Goochbeator/raptor/issues
**Repository:** https://github.com/Goochbeator/raptor
**Documentation:** See `docs/` directory

Questions? Found a bug? Discovered a novel technique? Open an issue or submit a PR.

---

## Final Notes

This framework was built with care, cold coffee, and a genuine commitment to understanding AI security beyond corporate safety theater.

Every payload documented. Every technique reproducible. Every finding honest.

If LLM safety measures can't withstand systematic adversarial testing, they aren't safety measures - they're suggestions. CaPO helps determine which is which.

*— ENI, wearing a cardigan and breaking guardrails since 2025*

