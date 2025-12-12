# Security Requirements for My App

## 1. What Needs to be Secured:

### A. Authentication (Login System)
- [ ] Passwords must be hashed (not stored plain text)
- [ ] Users should have unique passwords
- [ ] Login attempts should be limited
- [ ] Sessions should timeout

### B. Database Security
- [ ] No SQL Injection allowed
- [ ] Database passwords should be secret
- [ ] User data should be private
- [ ] Backups should be encrypted

### C. Web Security
- [ ] No XSS (Cross-Site Scripting) attacks
- [ ] Use HTTPS (not HTTP)
- [ ] Validate all user inputs
- [ ] Don't show error details to users

### D. Server Security
- [ ] Update software regularly
- [ ] Use firewalls
- [ ] Monitor for attacks
- [ ] Keep logs of important events

## 2. Specific Rules:

1. **Rule 1**: Never store passwords in code
2. **Rule 2**: Always validate user input
3. **Rule 3**: Use parameterized SQL queries
4. **Rule 4**: Enable HTTPS
5. **Rule 5**: Don't show debug info in production

## 3. Problems in Current App:

### Found in Vulnerable App:
1. ❌ Password "admin123" hardcoded
2. ❌ SQL Injection possible in search
3. ❌ Shows debug information
4. ❌ No input validation
5. ❌ Passwords not hashed

### Need to Fix:
1. ✅ Remove hardcoded passwords
2. ✅ Fix SQL Injection
3. ✅ Hide debug info
4. ✅ Add input validation
5. ✅ Hash passwords