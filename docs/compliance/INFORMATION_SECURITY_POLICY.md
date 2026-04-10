# Information Security Policy
## Quantum Nexus Forge v5.0.2

**Template source:** ICT Institute — Information Security Policy Template (CC Attribution License)
**Standard:** ISO/IEC 27001:2022
**Prepared by:** Shannon Bryan Kelly
**Effective Date:** April 2026
**Review Date:** April 2027

---

## 1. Purpose

This policy establishes the information security objectives, principles, and commitments for **Quantum Nexus Forge**. It protects the confidentiality, integrity, and availability of all information assets associated with the platform.

---

## 2. Scope

This policy applies to:
- All source code, configuration files, and documentation
- Azure OpenAI API credentials and `.env` configuration
- GitHub repositories and CI/CD pipeline
- Any future user data or conversation logs

---

## 3. Information Security Objectives

| Objective | Target |
|-----------|--------|
| No credentials committed to version control | Zero incidents |
| CI pipeline passes before any deployment | 100% of releases |
| Azure API keys rotated if suspected compromise | Within 24 hours |
| Security incidents logged and reviewed | 100% of incidents |
| Platform accessible only to authorized users | Until multi-user deployment |

---

## 4. Principles

### 4.1 Confidentiality
- All API keys, endpoints, and credentials stored in `.env` files only
- `.env` files excluded from Git via `.gitignore` — never committed to GitHub
- Source code reviewed for hardcoded secrets before any commit

### 4.2 Integrity
- All changes committed to GitHub with meaningful commit messages
- CI pipeline validates code on every push — no deployment without passing tests
- Version history maintained in `docs/project_log.txt`

### 4.3 Availability
- Mock mode (`MOCK_AI=true`) ensures platform remains operational if Azure is unavailable
- Flask server auto-installs dependencies on first run
- Auto-browser launch reduces startup friction

---

## 5. Asset Classification

| Asset | Classification | Owner |
|-------|---------------|-------|
| Azure OpenAI API key | 🔴 Confidential | Shannon Bryan Kelly |
| Azure endpoint URL | 🔴 Confidential | Shannon Bryan Kelly |
| `.env` file | 🔴 Confidential | Shannon Bryan Kelly |
| Source code (`app.py`, `azure_adapter.py`) | 🟡 Internal | Shannon Bryan Kelly |
| GitHub repository (public) | 🟢 Public | Shannon Bryan Kelly |
| SDLC documentation | 🟢 Public | Shannon Bryan Kelly |
| Compliance documentation | 🟢 Public | Shannon Bryan Kelly |

---

## 6. Access Control

| Resource | Access | Authorization |
|----------|--------|---------------|
| GitHub repository | Read: public; Write: owner only | GitHub account control |
| Azure OpenAI resource | Owner only | Azure portal credentials |
| `.env` file | Owner machine only | Local file system |
| Flask admin endpoints | Localhost only | No authentication yet |

**Note:** Before any multi-user deployment, authentication must be implemented for all API endpoints.

---

## 7. Acceptable Use

- Platform used for legitimate knowledge synthesis, portfolio, and research purposes
- No credential sharing with third parties
- No processing of sensitive personal data without updated DPIA
- Employees / contractors must read and acknowledge this policy before contributing

---

## 8. Supplier Security

| Supplier | Service | Security Assessment |
|----------|---------|---------------------|
| Microsoft Azure | OpenAI API, Cosmos DB | ISO 27001 certified; SOC 2 Type II; Data Processing Agreement via subscription |
| GitHub (Microsoft) | Version control, CI/CD | ISO 27001 certified; SOC 2 Type II |
| Anthropic | Claude AI (development) | Enterprise privacy terms accepted |

---

## 9. Incident Response

| Step | Action | Timeframe |
|------|--------|-----------|
| 1 | Detect and identify incident | Immediate |
| 2 | Log incident in INCIDENT_LOG.md | Within 1 hour |
| 3 | Contain — disable live AI if needed | Within 1 hour |
| 4 | Rotate any compromised credentials via Azure portal | Within 24 hours |
| 5 | Review root cause | Within 48 hours |
| 6 | Update controls to prevent recurrence | Within 1 week |

---

## 10. Business Continuity

- Mock mode fallback ensures system remains operational during Azure outages
- GitHub repository serves as full source code backup
- `.env` credentials backed up securely offline by owner

---

## 11. Compliance

| Regulation / Standard | Applicability |
|----------------------|---------------|
| GDPR | Applicable — see DPIA.md |
| EU AI Act | Applicable — see AI_POLICY.md and FRIA.md |
| ISO 27001:2022 | Framework adopted — see STATEMENT_OF_APPLICABILITY.md |
| Microsoft Azure DPA | Applicable — accepted via Azure subscription |

---

## 12. Roles and Responsibilities

| Role | Responsibility |
|------|---------------|
| Shannon Bryan Kelly (Data Controller / Architect) | Owns all security decisions, credential management, incident response, policy review |

---

## 13. Policy Review

This policy is reviewed:
- Annually (April each year)
- Following any security incident
- Before any significant architecture change or deployment expansion

---

*Template adapted from ICT Institute Information Security Policy Template under Creative Commons Attribution License.*
*Source: https://github.com/swzaken/freetemplates*
