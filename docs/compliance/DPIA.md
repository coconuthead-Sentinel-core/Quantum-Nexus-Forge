# Data Protection Impact Assessment (DPIA)
## Quantum Nexus Forge v5.0.2

**Template source:** ICT Institute — DPIA Template (CC Attribution License)
**Prepared by:** Shannon Bryan Kelly
**Date:** April 2026
**Review Date:** April 2027

---

## 1. Introduction

This DPIA identifies, assesses, and documents privacy risks for the Quantum Nexus Forge platform. It is conducted in accordance with GDPR Article 35.

### Is a DPIA Required?

| Criterion | Present? |
|-----------|---------|
| Large-scale processing of special category data | No |
| Systematic monitoring of individuals | No |
| Automated decision-making with legal/significant effects | No |
| Innovative technology with privacy implications | Yes — AI processing |
| Processing that may prevent individuals from exercising rights | No |

**DPIA Decision: Recommended** — AI processing of user-provided text warrants documented assessment, even though processing is minimal.

---

## 2. System Description

**Quantum Nexus Forge** accepts text prompts from users, routes them through five AI agents (powered by Azure OpenAI GPT-5.4-nano), and returns synthesized AI responses. In default configuration, no data is stored after the session ends.

### Data Flow

```
User types prompt
      ↓
Flask backend (app.py) — in-memory only
      ↓
Azure OpenAI API (Microsoft cloud — USA/EU)
      ↓
AI response returned to user
      ↓
[Optional] Cosmos DB persistence — NOT active by default
```

---

## 3. Personal Data Inventory

| Data Element | Source | Purpose | Legal Basis | Stored? |
|-------------|--------|---------|-------------|---------|
| User prompt text | User input | Generate AI response | Legitimate interest / consent | No — in memory only |
| IP address | HTTP request | Server logging | Legitimate interest | No — not logged by default |
| Session data | Flask session | Request routing | Legitimate interest | No — session only |

**Special Category Data (GDPR Art. 9):**
- Not intentionally collected
- Users may inadvertently include health, disability, or other sensitive data in prompts
- No mechanism currently exists to detect or flag this

---

## 4. Privacy Risk Assessment

### Risk 1: User Enters Personal Data in Prompts

| Field | Detail |
|-------|--------|
| Description | User includes name, address, health info, or other personal data in a prompt |
| Likelihood | Medium |
| Severity | Medium |
| Risk Level | 🟡 MEDIUM |
| Mitigation | UI guidance advising users not to enter personal data; no persistent storage |
| Residual Risk | LOW |

---

### Risk 2: Azure OpenAI Processing Personal Data

| Field | Detail |
|-------|--------|
| Description | Microsoft processes user prompt data through Azure OpenAI |
| Likelihood | High (by design) |
| Severity | Low |
| Risk Level | 🟢 LOW |
| Mitigation | Microsoft Azure data processing terms apply; Azure OpenAI does not train models on customer data; Data Processing Agreement with Microsoft is in place via Azure subscription |
| Residual Risk | LOW |

---

### Risk 3: Cosmos DB Storing Conversation Data

| Field | Detail |
|-------|--------|
| Description | If Cosmos DB persistence is enabled, all conversation turns would be stored |
| Likelihood | Low (not yet enabled) |
| Severity | High |
| Risk Level | 🟡 MEDIUM |
| Mitigation | Cosmos DB integration is not activated; DPIA must be updated and privacy notice required before activation |
| Residual Risk | LOW (while disabled) |

---

### Risk 4: Unauthorized Access to Azure Credentials

| Field | Detail |
|-------|--------|
| Description | `.env` file containing API keys is accessed by unauthorized party |
| Likelihood | Low |
| Severity | High |
| Risk Level | 🟡 MEDIUM |
| Mitigation | `.env` excluded from GitHub via `.gitignore`; credentials not shared; access limited to owner |
| Residual Risk | LOW |

---

## 5. Overall Privacy Risk Summary

| Risk | Residual Level |
|------|----------------|
| Personal data in prompts | 🟢 LOW |
| Azure OpenAI processing | 🟢 LOW |
| Cosmos DB persistence | 🟢 LOW (while disabled) |
| Credential exposure | 🟢 LOW |

**Overall DPIA Result: LOW RISK** — Acceptable for current single-user local deployment.

---

## 6. Measures in Place

| Measure | Status |
|---------|--------|
| No persistent data storage by default | ✅ Built-in |
| Azure OpenAI data processing terms accepted | ✅ Via Azure subscription |
| `.env` credentials excluded from version control | ✅ `.gitignore` configured |
| User guidance not to enter personal data | ⚠️ Add to UI/README |
| Privacy notice for users | ⚠️ Required before multi-user deployment |
| Data retention policy | N/A — no data retained |

---

## 7. Data Subject Rights

| Right | How Handled |
|-------|-------------|
| Right to access | No personal data stored — nothing to access |
| Right to erasure | No personal data stored — nothing to erase |
| Right to rectification | Not applicable |
| Right to portability | Not applicable |
| Right to object to automated decisions | No automated decisions about individuals |

---

## 8. International Data Transfers

| Transfer | Safeguard |
|----------|-----------|
| Prompts → Azure OpenAI (USA/EU) | Microsoft Azure Standard Contractual Clauses |

---

## 9. DPIA Conclusion

**Processing may proceed** under current configuration. DPIA must be updated before:
- Enabling Cosmos DB persistence
- Deploying to multiple users
- Adding authentication/user accounts
- Expanding to healthcare or employment contexts

---

## 10. Sign-Off

| Role | Name | Date |
|------|------|------|
| Data Controller / Architect | Shannon Bryan Kelly | April 2026 |

---

*Template adapted from ICT Institute DPIA Template under Creative Commons Attribution License.*
*Source: https://github.com/swzaken/freetemplates*
