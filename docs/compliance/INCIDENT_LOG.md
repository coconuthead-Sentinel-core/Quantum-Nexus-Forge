# Incident Log
## Quantum Nexus Forge v5.0.2

**Template source:** ICT Institute — Incidents-Data-breaches-Nonconformities (CC Attribution License)
**Standard:** ISO/IEC 27001:2022 | GDPR Article 33
**Maintained by:** Shannon Bryan Kelly
**Last Updated:** April 2026

---

## How to Use This Log

Record **every** information security incident, data breach, or nonconformity here — no matter how small. This log is your audit trail and learning record.

**When to log:**
- Any suspected or confirmed unauthorized access to credentials or data
- Any AI output that causes harm, is discriminatory, or violates the AI Policy
- Any system failure that affects availability or integrity
- Any CI/CD pipeline failure caused by security issues
- Any GDPR data breach (triggers 72-hour regulatory notification window)

---

## Severity Scale

| Level | Meaning | Example |
|-------|---------|---------|
| 🔴 CRITICAL | Potential data breach / credential compromise | API key found in public commit |
| 🟠 HIGH | Security control failure / AI policy violation | Discriminatory AI output generated |
| 🟡 MEDIUM | Process gap / near-miss | Forgot to run security review before release |
| 🟢 LOW | Minor nonconformity / observation | Documentation out of date |

---

## Active Incidents

*No active incidents.*

---

## Incident History

| ID | Date | Type | Severity | Description | Status | Resolution |
|----|------|------|---------|-------------|--------|-----------|
| — | — | — | — | No incidents recorded | — | — |

---

## Incident Record Template

When an incident occurs, copy and fill this template:

```
### INC-[NUMBER]

**Date Detected:** YYYY-MM-DD
**Date Resolved:** YYYY-MM-DD
**Type:** Security Incident / Data Breach / AI Policy Violation / Nonconformity
**Severity:** CRITICAL / HIGH / MEDIUM / LOW
**Detected By:** Shannon Bryan Kelly / Azure Alert / CI Pipeline / Other

**Description:**
[What happened? What was affected?]

**Assets Affected:**
[List from Asset Register — e.g., A-001 Azure API Key]

**Immediate Actions Taken:**
1. [Step 1]
2. [Step 2]

**Root Cause:**
[Why did this happen?]

**GDPR Assessment:**
[ ] Does this involve personal data? Yes / No
[ ] If yes — is regulatory notification required? (72-hour window from detection)
[ ] Notified authority: [Name / Date] or N/A

**Corrective Actions:**
1. [Action] — Owner: [Name] — Due: [Date]
2. [Action] — Owner: [Name] — Due: [Date]

**Lessons Learned:**
[What will be done differently?]

**Status:** OPEN / RESOLVED / CLOSED
```

---

## Data Breach Notification Checklist

If a breach involves personal data, complete this within **72 hours**:

- [ ] Incident identified and contained
- [ ] Nature and scope of breach documented
- [ ] Estimated number of individuals affected
- [ ] Categories of personal data involved
- [ ] Likely consequences assessed
- [ ] Measures taken or proposed to address the breach
- [ ] **If breach likely results in high risk to individuals:** Notify affected individuals without undue delay
- [ ] **Notification to supervisory authority filed** (if required)
- [ ] Record kept of all breaches (even if not notified)

---

*Template adapted from ICT Institute Incidents-Data-breaches-Nonconformities under Creative Commons Attribution License.*
*Source: https://github.com/swzaken/freetemplates*
