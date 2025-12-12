# Risk Matrix - What's Most Dangerous

| Risk | Bad Things That Could Happen | Chance (1-5) | Damage (1-5) | Total Risk | Priority |
|------|------------------------------|--------------|--------------|------------|----------|
| SQL Injection | Hackers can read/delete all user data | 4 | 5 | 20 | 🔴 HIGH |
| Hardcoded Passwords | Anyone can login as admin | 5 | 4 | 20 | 🔴 HIGH |
| No Password Hashing | If database stolen, all passwords readable | 3 | 5 | 15 | 🔴 HIGH |
| Debug Info Exposed | Hackers learn about system | 4 | 3 | 12 | 🟡 MEDIUM |
| XSS Vulnerabilities | Can steal user sessions | 3 | 3 | 9 | 🟡 MEDIUM |
| No HTTPS | Data stolen in transit | 2 | 4 | 8 | 🟡 MEDIUM |
| No Logging | Can't track attacks | 3 | 2 | 6 | 🟢 LOW |
| No Backups | Lose all data if server crashes | 2 | 5 | 10 | 🟡 MEDIUM |

## Risk Scoring:
- **1-5**: Low risk (🟢 Green)
- **6-12**: Medium risk (🟡 Yellow)  
- **13-20**: High risk (🔴 Red)
- **21-25**: Critical risk (⚫ Black)

## Top 3 to Fix NOW:
1. 🔴 SQL Injection (Risk: 20)
2. 🔴 Hardcoded Passwords (Risk: 20)
3. 🔴 No Password Hashing (Risk: 15)