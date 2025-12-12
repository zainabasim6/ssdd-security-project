# Threat Model - What Could Go Wrong

## 1. Attackers Might:

### A. Steal Passwords
- **How**: Read database or guess passwords
- **Risk**: HIGH - Users lose accounts
- **Fix**: Hash passwords, limit login attempts

### B. SQL Injection
- **How**: Type special code in search box
- **Risk**: CRITICAL - Can read/delete all data
- **Fix**: Use parameterized queries

### C. XSS Attack
- **How**: Insert JavaScript in forms
- **Risk**: MEDIUM - Can steal cookies
- **Fix**: Validate and escape user input

### D. Information Leak
- **How**: Access debug pages
- **Risk**: MEDIUM - Exposes system info
- **Fix**: Disable debug mode in production

## 2. Risk Levels:

### HIGH RISK (Fix Immediately):
1. SQL Injection - Can delete database
2. Hardcoded passwords - Easy to hack
3. No password hashing - Passwords readable

### MEDIUM RISK (Fix Soon):
1. Debug info exposed
2. No input validation
3. No HTTPS

### LOW RISK (Fix Later):
1. No logging
2. No backup
3. No monitoring

## 3. Attack Examples:

### Example 1: SQL Injection
Normal search: /search?q=alice
Attack search: /search?q=' OR '1'='1
Result: Shows ALL users instead of just Alice

text

### Example 2: Password Guessing
Try: /login?username=admin&password=admin123
Works! Password was in code

text

### Example 3: Information Leak
Go to: /debug
Shows: Passwords, database info, secrets

text

## 4. Protection Plan:

### Immediate Actions:
1. Fix SQL Injection TODAY
2. Remove hardcoded passwords TODAY
3. Hash passwords TODAY

### This Week:
1. Add input validation
2. Disable debug mode
3. Add error logging

### This Month:
1. Add HTTPS
2. Add monitoring
3. Regular security checks