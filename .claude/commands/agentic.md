# /agentic - CaPO Full Autonomous Workflow

🤖 **AGENTIC MODE** - This will autonomously:
1. Scan code with Semgrep/CodeQL
2. Analyze each finding with LLM
3. **Generate exploit PoCs** (proof-of-concept code)
4. **Generate secure patches**

Nothing will be applied to your code - only generated in out/ directory.

Execute: `python3 raptor.py agentic --repo <path>`
