# CaPO + Claude Code Integration

This directory contains custom slash commands that let you use CaPO with plain English via Claude Code.

## Available Slash Commands

### `/raptor` - General CaPO Assistant
The main command that helps you decide which CaPO mode to use.

**Examples:**
- "Hey Claude, /raptor - scan my code for vulnerabilities"
- "/raptor - I need to fuzz a binary"
- "/raptor - test my web application"

### `/raptor-scan` - Code Scanning
Runs CaPO's autonomous code scanning (Semgrep + CodeQL + LLM analysis).

**Examples:**
- "/raptor-scan - scan the current directory"
- "/raptor-scan - check this repository for security issues"
- "/raptor-scan - find vulnerabilities in /path/to/my/app"

### `/raptor-fuzz` - Binary Fuzzing
Fuzzes binaries with AFL++ and generates exploits from crashes.

**Examples:**
- "/raptor-fuzz - fuzz ./my_binary for 10 minutes"
- "/raptor-fuzz - test /usr/local/bin/myapp for crashes"
- "/raptor-fuzz - find bugs in this binary"

### `/raptor-web` - Web Application Testing
Scans web applications for OWASP Top 10 vulnerabilities.

**Examples:**
- "/raptor-web - scan https://myapp.com"
- "/raptor-web - test my website for XSS and SQLi"

## How to Use

1. **Type the slash command** in Claude Code
2. **Add your request in plain English** after the dash
3. **Claude will**:
   - Ask clarifying questions if needed
   - Run the appropriate CaPO command
   - Analyze the results
   - Summarize vulnerabilities found
   - Show exploits and patches
   - Help you fix issues

## Example Workflow

```
You: /raptor-scan - scan this directory for secrets and vulnerabilities

Claude: I'll run a comprehensive security scan on the current directory.
        Let me start by running CaPO in agentic mode...

        [Runs: python3 raptor.py agentic --repo /current/path]

        ✓ Scan complete! Found 5 vulnerabilities:
        1. Hardcoded AWS credentials (HIGH) - app/config.py:23
        2. SQL Injection (CRITICAL) - api/users.py:45
        3. XSS vulnerability (MEDIUM) - web/templates/index.html:67
        ...

        I've also generated:
        - 3 working exploit PoCs in out/exploits/
        - 5 secure patches in out/patches/

        Would you like me to:
        1. Apply the patches automatically?
        2. Explain each vulnerability in detail?
        3. Show the exploit code?
```

## Natural Language Examples

You can use very natural language:

- "Hey Claude, scan my code"
- "Fuzz this binary for me"
- "Check if my website has XSS"
- "Find security bugs in ./myapp"
- "Test /usr/bin/vulnerable_program for crashes"
- "Scan this repo for hardcoded secrets"

Claude will understand your intent and run the appropriate CaPO command!

## What Happens Behind the Scenes

1. **Slash command loads** the context/instructions for that CaPO mode
2. **Claude understands** what you want to test and which parameters to use
3. **CaPO runs** via the Bash tool (python3 raptor.py ...)
4. **Results are analyzed** by reading output files from the `out/` directory
5. **Claude summarizes** findings in plain English
6. **Next steps offered** - apply patches, explain vulnerabilities, etc.

## Benefits

✅ **No need to remember command syntax** - just use plain English
✅ **Intelligent defaults** - Claude picks good parameters
✅ **Results interpretation** - Claude explains what was found
✅ **Interactive** - Ask follow-up questions, drill into findings
✅ **Helpful** - Offers to apply patches, explain concepts, etc.

## Tips

- Be specific about what you want to test
- Claude will ask for paths if you don't provide them
- You can chain requests: "scan this, then fuzz that binary"
- Claude remembers context, so you can say "now explain finding #2"

## Requirements

- Claude Code CLI installed
- CaPO installed (python3, dependencies)
- For fuzzing: AFL++ properly configured
- For full analysis: ANTHROPIC_API_KEY or OPENAI_API_KEY set

---

**Start using CaPO with natural language now!** Just type `/raptor` and tell Claude what you want to test.
