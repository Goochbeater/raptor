# CaPO Web Application Scanner

You are helping the user scan a web application for security vulnerabilities.

## Your Task

1. **Understand the target**: Get the web application URL
   - Full URL (e.g., https://example.com)
   - Ask about authentication if needed
   - Ask about scope (crawl depth, max pages)

2. **Run CaPO web scan**: Execute the web scanning command:
   ```bash
   python3 raptor.py web --url <url>
   ```

3. **Analyze results**: After the scan:
   - Summarize vulnerabilities found (XSS, SQLi, CSRF, etc.)
   - Show severity ratings
   - Explain how to exploit them (if safe to do so)
   - Show generated patches or mitigation advice

4. **Help fix issues**: Offer to:
   - Explain each vulnerability type
   - Suggest secure coding practices
   - Help implement fixes

## Example Commands

Basic web scan:
```bash
python3 raptor.py web --url https://example.com
```

With authentication:
```bash
python3 raptor.py web --url https://example.com --auth-token "Bearer xyz"
```

## Important Notes

- Only scan applications you own or have permission to test
- Web scanning looks for OWASP Top 10 vulnerabilities
- Results are saved to `out/web_scan_<timestamp>/`

Be ethical and responsible with security testing!
