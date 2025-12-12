 Security Requirements Document (SRD)
## Secure Notes Application - CYC386 Final Project
## OWASP ASVS v4.0 Level 1 Compliance
## Version: 1.0 | Date: $(date +"%Y-%m-%d")

---

## 1. EXECUTIVE SUMMARY

This document outlines **12 critical security requirements** mapped to OWASP Application Security Verification Standard (ASVS) v4.0 Level 1 for the Secure Notes Application. These requirements ensure basic security controls are implemented to protect against common web application vulnerabilities.

## 2. OWASP ASVS SECURITY REQUIREMENTS (12+ ITEMS)

### **REQUIREMENT 1: Secure Communication** 🔒
**OWASP ASVS: 7.1.1** - Verify that all forms of communication are encrypted using TLS.
- **Requirement ID**: COMM-001
- **Description**: All client-server communications MUST use TLS 1.2 or higher
- **Verification**: HTTPS enforced, HTTP redirects to HTTPS
- **Implementation**: Flask-TLS/SSL configuration, production deployment with SSL certificate
- **Priority**: CRITICAL ⚠️

### **REQUIREMENT 2: Password Storage** 🔐
**OWASP ASVS: 2.1.2** - Verify that passwords are stored securely using strong hashing.
- **Requirement ID**: AUTH-001
- **Description**: Passwords MUST be hashed using bcrypt with minimum work factor of 10
- **Verification**: No plain text passwords in database or logs
- **Implementation**: `bcrypt` library with `bcrypt.hashpw(password, bcrypt.gensalt(rounds=10))`
- **Priority**: CRITICAL ⚠️

### **REQUIREMENT 3: SQL Injection Prevention** 🛡️
**OWASP ASVS: 5.3.1** - Verify that SQL queries use parameterized queries.
- **Requirement ID**: VAL-001
- **Description**: ALL database queries MUST use parameterized queries or ORM
- **Verification**: No string concatenation in SQL queries
- **Implementation**: SQLAlchemy ORM or `cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))`
- **Priority**: CRITICAL ⚠️

### **REQUIREMENT 4: Input Validation** ✅
**OWASP ASVS: 5.1.1** - Verify that all input is validated on the server side.
- **Requirement ID**: VAL-002
- **Description**: Validate ALL user inputs for type, length, format, and range
- **Verification**: Input validation functions for every endpoint
- **Implementation**: Flask-WTF forms, custom validation functions, regex patterns
- **Priority**: HIGH 🔴

### **REQUIREMENT 5: XSS Prevention** 🚫
**OWASP ASVS: 5.4.1** - Verify that output encoding is applied to prevent XSS.
- **Requirement ID**: OUT-001
- **Description**: Apply context-aware output encoding for HTML, JavaScript, and CSS contexts
- **Verification**: User input rendered safely in templates
- **Implementation**: Jinja2 auto-escaping, `|safe` filter only for trusted content
- **Priority**: HIGH 🔴

### **REQUIREMENT 6: Session Management** 🔄
**OWASP ASVS: 3.1.1** - Verify that a standard session management mechanism is used.
- **Requirement ID**: SESS-001
- **Description**: Use secure session tokens (JWT) with proper expiration
- **Verification**: Sessions expire after 30 minutes of inactivity
- **Implementation**: Flask-JWT-Extended with HS256 signing, 30-minute expiration
- **Priority**: HIGH 🔴

### **REQUIREMENT 7: Error Handling** 📝
**OWASP ASVS: 8.3.1** - Verify that error messages do not disclose sensitive information.
- **Requirement ID**: ERR-001
- **Description**: Generic error messages in production, no stack traces
- **Verification**: `app.debug = False` in production, custom error handlers
- **Implementation**: Flask error handlers returning JSON: `{"error": "Something went wrong"}`
- **Priority**: MEDIUM 🟡

### **REQUIREMENT 8: Account Lockout** 🔐
**OWASP ASVS: 2.1.6** - Verify account locking after multiple failed authentication attempts.
- **Requirement ID**: AUTH-002
- **Description**: Lock accounts after 5 failed login attempts within 15 minutes
- **Verification**: Failed attempt tracking in database
- **Implementation**: Login attempt counter with timestamp in users table
- **Priority**: MEDIUM 🟡

### **REQUirement 9: Security Headers** 📋
**OWASP ASVS: 6.2.1** - Verify that security headers are set appropriately.
- **Requirement ID**: HEAD-001
- **Description**: Implement security HTTP headers (CSP, HSTS, X-Frame-Options)
- **Verification**: Headers present in HTTP responses
- **Implementation**: Flask-Talisman or custom middleware
- **Priority**: MEDIUM 🟡

### **REQUIREMENT 10: Access Control** 👥
**OWASP ASVS: 4.1.1** - Verify that users can only access their own resources.
- **Requirement ID**: AC-001
- **Description**: Users can ONLY access their own notes, not other users' data
- **Verification**: User ID verification before data access
- **Implementation**: `if current_user.id != note.user_id: return error`
- **Priority**: HIGH 🔴

### **REQUIREMENT 11: Logging** 📊
**OWASP ASVS: 8.1.1** - Verify that security events are logged.
- **Requirement ID**: LOG-001
- **Description**: Log all authentication attempts (success/failure)
- **Verification**: Authentication logs in structured format
- **Implementation**: Python logging module with JSON format
- **Priority**: MEDIUM 🟡

### **REQUIREMENT 12: Dependency Management** 📦
**OWASP ASVS: 11.1.1** - Verify that components are up to date and free from vulnerabilities.
- **Requirement ID**: DEP-001
- **Description**: Regular vulnerability scanning of dependencies
- **Verification**: `requirements.txt` with pinned versions, security scans
- **Implementation**: `pip freeze > requirements.txt`, Dependabot/GitHub Security
- **Priority**: MEDIUM 🟡

---

## 3. ADDITIONAL REQUIREMENTS (Bonus - Beyond 12)

### **REQUIREMENT 13: Data Encryption** 🔏
**OWASP ASVS: 7.2.1** - Verify that sensitive data is encrypted at rest.
- **Requirement ID**: CRYPTO-001
- **Description**: Encrypt sensitive note content in database using AES-256
- **Implementation**: `cryptography` library with Fernet encryption
- **Priority**: HIGH 🔴

### **REQUIREMENT 14: CSRF Protection** 🛡️
**OWASP ASVS: 4.4.1** - Verify that CSRF protection is in place for state-changing operations.
- **Requirement ID**: CSRF-001
- **Description**: CSRF tokens for POST, PUT, DELETE operations
- **Implementation**: Flask-WTF CSRF protection
- **Priority**: MEDIUM 🟡

### **REQUIREMENT 15: File Upload Security** 📎
**OWASP ASVS: 5.5.1** - Verify that file uploads are validated and scanned.
- **Requirement ID**: FILE-001
- **Description**: Validate file type, size, and scan for malware
- **Implementation**: File extension validation, size limits, ClamAV integration
- **Priority**: LOW 🟢

---

## 4. IMPLEMENTATION STATUS

### **Insecure Version (Before):**
| Requirement | Status | Vulnerabilities |
|------------|--------|-----------------|
| COMM-001 | ❌ FAIL | HTTP only, no TLS |
| AUTH-001 | ❌ FAIL | Plain text passwords |
| VAL-001 | ❌ FAIL | SQL concatenation, injection possible |
| VAL-002 | ❌ FAIL | No input validation |
| OUT-001 | ❌ FAIL | Raw HTML rendering, XSS possible |
| SESS-001 | ❌ FAIL | No session management |
| ERR-001 | ❌ FAIL | Debug mode ON, stack traces exposed |
| AUTH-002 | ❌ FAIL | No account lockout |
| HEAD-001 | ❌ FAIL | No security headers |
| AC-001 | ❌ FAIL | No access control checks |
| LOG-001 | ❌ FAIL | No security logging |
| DEP-001 | ❌ FAIL | No dependency management |

### **Secure Version (After):**
| Requirement | Status | Implementation Evidence |
|------------|--------|-------------------------|
| COMM-001 | ✅ PASS | TLS 1.2+ configured |
| AUTH-001 | ✅ PASS | bcrypt password hashing |
| VAL-001 | ✅ PASS | Parameterized SQL queries |
| VAL-002 | ✅ PASS | Input validation functions |
| OUT-001 | ✅ PASS | Jinja2 auto-escaping |
| SESS-001 | ✅ PASS | JWT with expiration |
| ERR-001 | ✅ PASS | Custom error handlers |
| AUTH-002 | ✅ PASS | Login attempt tracking |
| HEAD-001 | ✅ PASS | Security headers middleware |
| AC-001 | ✅ PASS | User ID verification |
| LOG-001 | ✅ PASS | Structured logging |
| DEP-001 | ✅ PASS | requirements.txt with versions |

---

## 5. TESTING PROCEDURES

### **Test Case 1: SQL Injection Prevention**
```bash
# Test Insecure Version (Should FAIL)
curl "http://localhost:5000/search?q=' OR '1'='1"

# Test Secure Version (Should PASS/Block)
curl "http://localhost:5001/secure_search?q=' OR '1'='1"
