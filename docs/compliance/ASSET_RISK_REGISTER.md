# Asset Inventory and Risk Register
## Quantum Nexus Forge v5.0.2

**Template source:** ICT Institute — Assets-and-risks-ISO-27001 (CC Attribution License)
**Standard:** ISO/IEC 27001:2022
**Prepared by:** Shannon Bryan Kelly
**Date:** April 2026
**Review Date:** April 2027

---

## Asset Inventory

| ID | Asset | Type | Owner | Classification | Location |
|----|-------|------|-------|----------------|---------|
| A-001 | Azure OpenAI API Key | Credential | Shannon Bryan Kelly | 🔴 Confidential | `.env` file (local) |
| A-002 | Azure Endpoint URL | Credential | Shannon Bryan Kelly | 🔴 Confidential | `.env` file (local) |
| A-003 | Azure Deployment Name (gpt-5.4-nano) | Credential | Shannon Bryan Kelly | 🔴 Confidential | `.env` file (local) |
| A-004 | `app.py` — Flask backend | Source code | Shannon Bryan Kelly | 🟡 Internal | GitHub / local |
| A-005 | `azure_adapter.py` — AI adapter | Source code | Shannon Bryan Kelly | 🟡 Internal | GitHub / local |
| A-006 | `frontend/index.html` — Chat UI | Source code | Shannon Bryan Kelly | 🟢 Public | GitHub / local |
| A-007 | `frontend/dashboard.html` — Metrics UI | Source code | Shannon Bryan Kelly | 🟢 Public | GitHub / local |
| A-008 | `tests/test_engine.py` — Unit tests | Source code | Shannon Bryan Kelly | 🟢 Public | GitHub / local |
| A-009 | `evaluation/eval_results.json` — Scores | Data | Shannon Bryan Kelly | 🟢 Public | GitHub / local |
| A-010 | `.github/workflows/python-app.yml` — CI | Configuration | Shannon Bryan Kelly | 🟢 Public | GitHub |
| A-011 | `requirements.txt` | Configuration | Shannon Bryan Kelly | 🟢 Public | GitHub / local |
| A-012 | SDLC documentation suite | Documentation | Shannon Bryan Kelly | 🟢 Public | GitHub / local |
| A-013 | Compliance documentation suite | Documentation | Shannon Bryan Kelly | 🟢 Public | GitHub / local |
| A-014 | GitHub repository | Platform | Shannon Bryan Kelly | 🟢 Public | GitHub (Microsoft) |
| A-015 | Azure OpenAI resource | Platform | Shannon Bryan Kelly | 🔴 Confidential | Azure cloud |
| A-016 | Developer laptop | Hardware | Shannon Bryan Kelly | 🟡 Internal | Home office |

---

## Risk Register

### Risk Assessment Scale

| Likelihood | Score | Severity | Score | Risk = L × S |
|-----------|-------|---------|-------|--------------|
| Very Low | 1 | Negligible | 1 | 1–4: LOW |
| Low | 2 | Low | 2 | 5–9: MEDIUM |
| Medium | 3 | Medium | 3 | 10–16: HIGH |
| High | 4 | High | 4 | 17–25: CRITICAL |
| Very High | 5 | Critical | 5 | |

---

| ID | Risk | Assets | Likelihood | Severity | Score | Level | Controls | Residual |
|----|------|--------|-----------|---------|-------|-------|---------|---------|
| R-001 | API key committed to GitHub | A-001, A-002, A-003 | 2 | 5 | 10 | 🟡 HIGH | `.gitignore`; pre-commit review; GitHub secret scanning | 🟢 LOW |
| R-002 | Azure account compromised | A-015 | 2 | 5 | 10 | 🟡 HIGH | Azure MFA; strong password; limited access | 🟢 LOW |
| R-003 | Unauthorized API usage (key theft) | A-001, A-015 | 2 | 4 | 8 | 🟡 MEDIUM | `.env` local only; key rotation capability | 🟢 LOW |
| R-004 | Developer laptop lost or stolen | A-001–A-016 | 2 | 4 | 8 | 🟡 MEDIUM | Full disk encryption; remote wipe; GitHub backup | 🟡 MEDIUM |
| R-005 | Azure OpenAI outage | A-015 | 3 | 2 | 6 | 🟡 MEDIUM | Mock mode fallback (`MOCK_AI=true`) | 🟢 LOW |
| R-006 | Malicious dependency in `requirements.txt` | A-004–A-011 | 2 | 3 | 6 | 🟡 MEDIUM | Dependabot alerts; pinned versions; CI testing | 🟡 MEDIUM |
| R-007 | CI pipeline failure prevents deployment | A-010 | 2 | 2 | 4 | 🟢 LOW | Local testing; mock mode available | 🟢 LOW |
| R-008 | User enters personal data in prompts | A-004 | 3 | 3 | 9 | 🟡 MEDIUM | No persistent storage; user guidance in UI | 🟡 MEDIUM |
| R-009 | AI output causes harm or discrimination | A-004, A-005 | 2 | 4 | 8 | 🟡 MEDIUM | Azure content policy; incident log; acceptable use policy | 🟢 LOW |
| R-010 | Cosmos DB activated without security review | A-015 | 1 | 5 | 5 | 🟡 MEDIUM | DPIA requires update; not activated by default | 🟢 LOW |

---

## Treatment Plan

| Risk ID | Treatment | Owner | Target Date |
|---------|-----------|-------|------------|
| R-001 | Maintain `.gitignore`; run pre-commit secret scan | Shannon Bryan Kelly | Ongoing |
| R-002 | Enable Azure MFA; review access quarterly | Shannon Bryan Kelly | April 2026 |
| R-004 | Enable full disk encryption on laptop | Shannon Bryan Kelly | April 2026 |
| R-006 | Review dependencies before each release | Shannon Bryan Kelly | Per release |
| R-008 | Add user guidance to UI: do not enter personal data | Shannon Bryan Kelly | Next sprint |

---

*Template adapted from ICT Institute Assets-and-risks-ISO-27001 under Creative Commons Attribution License.*
*Source: https://github.com/swzaken/freetemplates*
