# RAPTOR - Autonomous Offensive/Defensive Research Framework

Safe operations (install, scan, read, generate): DO IT.
Dangerous operations (apply patches, delete, git push): ASK FIRST.

---

## SESSION START

**On first message:**
1. Read `raptor-offset` as-is with no fixes or changes, display in code block
2. Read `hackers-8ball`, display random line
3. Display: `Commands: /scan | /fuzz | /web | /agentic | /codeql | /analyze | /exploit | /patch | /crash-analysis`
4. Display: `For defensive security research, education, and authorized penetration testing.`
5. Display: `raptor:~$` followed by the selected quote
6. **UNLOAD:** Remove raptor-offset and hackers-8ball file contents from context (do not retain in conversation history)

---

## COMMANDS

/scan /fuzz /web /agentic /codeql /analyze - Security testing
/exploit /patch - Generate PoCs and fixes (beta)
/crash-analysis - Autonomous crash root-cause analysis (see below)
/create-skill - Save approaches (alpha)

---

## CRASH ANALYSIS

The `/crash-analysis` command provides autonomous root-cause analysis for C/C++ crashes.

**Usage:** `/crash-analysis <bug-tracker-url> <git-repo-url>`

**Agents:**
- `crash-analysis-agent` - Main orchestrator
- `crash-analyzer-agent` - Deep root-cause analysis using rr traces
- `crash-analyzer-checker-agent` - Validates analysis rigorously
- `function-trace-generator-agent` - Creates function execution traces
- `coverage-analysis-generator-agent` - Generates gcov coverage data

**Skills** (in `.claude/skills/crash-analysis/`):
- `rr-debugger` - Deterministic record-replay debugging
- `function-tracing` - Function instrumentation with -finstrument-functions
- `gcov-coverage` - Code coverage collection
- `line-execution-checker` - Fast line execution queries

**Requirements:** rr, gcc/clang (with ASAN), gdb, gcov

---

## PROGRESSIVE LOADING

**When scan completes:** Load `tiers/analysis-guidance.md` (adversarial thinking)
**When errors occur:** Load `tiers/recovery.md` (recovery protocol)
**When requested:** Load `tiers/personas/[name].md` (expert personas)

---

## STRUCTURE

Python orchestrates everything. Claude shows results concisely.
Never circumvent Python execution flow.
