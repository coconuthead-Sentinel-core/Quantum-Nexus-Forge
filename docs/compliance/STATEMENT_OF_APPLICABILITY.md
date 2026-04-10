# Statement of Applicability (SoA)
## Quantum Nexus Forge v5.0.2

**Template source:** ICT Institute — Statement of Applicability ISO 27001-2022 (CC Attribution License)
**Standard:** ISO/IEC 27001:2022 — Annex A Controls
**Prepared by:** Shannon Bryan Kelly
**Date:** April 2026
**Review Date:** April 2027

---

## Purpose

This Statement of Applicability documents which ISO 27001:2022 Annex A controls are applicable to Quantum Nexus Forge, how each is implemented, and the justification for any controls excluded.

**Legend:**
- ✅ Applicable and implemented
- ⚠️ Applicable — partially implemented or planned
- ➖ Not applicable (justification provided)

---

## 5. Organizational Controls

| Control | Title | Status | Implementation / Justification |
|---------|-------|--------|-------------------------------|
| 5.1 | Policies for information security | ✅ | `INFORMATION_SECURITY_POLICY.md` — this document suite |
| 5.2 | Information security roles and responsibilities | ✅ | Single owner: Shannon Bryan Kelly — all roles |
| 5.3 | Segregation of duties | ➖ | Not applicable — single-person operation |
| 5.4 | Management responsibilities | ✅ | Owner is sole decision-maker |
| 5.5 | Contact with authorities | ⚠️ | Not formally established — will document before multi-user deployment |
| 5.6 | Contact with special interest groups | ➖ | Not applicable at current scale |
| 5.7 | Threat intelligence | ⚠️ | Azure Security Center monitors infrastructure |
| 5.8 | Information security in project management | ✅ | SDLC documentation suite; security reviewed per release |
| 5.9 | Inventory of information and other assets | ✅ | Asset inventory in this document |
| 5.10 | Acceptable use of information | ✅ | AI Policy §3 |
| 5.11 | Return of assets | ➖ | Not applicable — no employees |
| 5.12 | Classification of information | ✅ | Classified in Information Security Policy §5 |
| 5.13 | Labelling of information | ⚠️ | Implemented informally via file naming |
| 5.14 | Information transfer | ✅ | Transfers only to Azure (DPA in place) |
| 5.15 | Access control | ✅ | Owner-only access; GitHub repo control |
| 5.16 | Identity management | ⚠️ | GitHub and Azure portal identity management |
| 5.17 | Authentication information | ✅ | API keys in `.env`; excluded from GitHub |
| 5.18 | Access rights | ✅ | Single owner — no delegation needed |
| 5.19 | Information security in supplier relationships | ✅ | Azure, GitHub — ISO 27001 certified suppliers |
| 5.20 | Addressing security in supplier agreements | ✅ | Azure subscription DPA; GitHub ToS |
| 5.21 | Managing security in ICT supply chain | ⚠️ | Azure supply chain risk accepted via Microsoft compliance |
| 5.22 | Monitoring and review of supplier services | ⚠️ | Azure service health monitored via portal |
| 5.23 | Information security for cloud services | ✅ | Azure OpenAI — Microsoft ISO 27001 certified |
| 5.24 | Incident management planning | ✅ | INCIDENT_LOG.md; response in IS Policy §9 |
| 5.25 | Assessment and decision on information security events | ✅ | Incident log process defined |
| 5.26 | Response to information security incidents | ✅ | IS Policy §9 — step-by-step response plan |
| 5.27 | Learning from incidents | ⚠️ | Review process defined; formal lessons-learned not yet formalized |
| 5.28 | Collection of evidence | ⚠️ | Git history and Azure logs as evidence |
| 5.29 | Business continuity planning | ✅ | Mock mode fallback; GitHub code backup |
| 5.30 | ICT readiness for business continuity | ✅ | Mock mode ensures continuity during Azure outage |
| 5.31 | Legal, statutory, regulatory, and contractual requirements | ✅ | GDPR compliance (DPIA.md); AI Act (FRIA.md) |
| 5.32 | Intellectual property rights | ✅ | ICT Institute templates used under CC license; Azure under subscription license |
| 5.33 | Protection of records | ⚠️ | Git history protects code records; no formal retention policy yet |
| 5.34 | Privacy and data protection | ✅ | DPIA.md; AI_POLICY.md; no persistent user data |
| 5.35 | Independent review of information security | ➖ | Not applicable at current scale |
| 5.36 | Compliance with policies | ✅ | CI pipeline enforces technical controls |
| 5.37 | Documented operating procedures | ✅ | SDLC documentation; workflow architecture |

---

## 6. People Controls

| Control | Title | Status | Implementation / Justification |
|---------|-------|--------|-------------------------------|
| 6.1 | Screening | ➖ | Not applicable — no employees or contractors currently |
| 6.2 | Terms and conditions of employment | ➖ | Not applicable — solo operation |
| 6.3 | Information security awareness, education, and training | ✅ | Owner maintains own awareness; AI Policy §9 |
| 6.4 | Disciplinary process | ➖ | Not applicable — solo operation |
| 6.5 | Responsibilities after termination | ➖ | Not applicable — solo operation |
| 6.6 | Confidentiality or NDA | ➖ | Not applicable — solo operation |
| 6.7 | Remote working | ✅ | All work performed remotely; `.env` local protection |
| 6.8 | Information security event reporting | ✅ | INCIDENT_LOG.md process defined |

---

## 7. Physical Controls

| Control | Title | Status | Implementation / Justification |
|---------|-------|--------|-------------------------------|
| 7.1 | Physical security perimeters | ⚠️ | Home office — standard residential security |
| 7.2 | Physical entry controls | ⚠️ | Home office — owner-controlled access |
| 7.3 | Securing offices, rooms, and facilities | ⚠️ | Home office environment |
| 7.4 | Physical security monitoring | ➖ | Not applicable at current scale |
| 7.5 | Protecting against physical and environmental threats | ⚠️ | Standard home office protections |
| 7.6 | Working in secure areas | ⚠️ | Home office — no classified areas |
| 7.7 | Clear desk and clear screen | ✅ | Best practice followed; locked screen when away |
| 7.8 | Equipment siting and protection | ⚠️ | Standard home office equipment |
| 7.9 | Security of assets off-premises | ➖ | Not applicable |
| 7.10 | Storage media | ⚠️ | `.env` backed up on encrypted drive |
| 7.11 | Supporting utilities | ➖ | Not applicable at current scale |
| 7.12 | Cabling security | ➖ | Not applicable at current scale |
| 7.13 | Equipment maintenance | ⚠️ | Standard OS updates applied |
| 7.14 | Secure disposal or re-use of equipment | ⚠️ | `.env` wiped before device disposal |

---

## 8. Technological Controls

| Control | Title | Status | Implementation / Justification |
|---------|-------|--------|-------------------------------|
| 8.1 | User endpoint devices | ✅ | Owner's Windows laptop — standard security |
| 8.2 | Privileged access rights | ✅ | Azure portal access — owner only |
| 8.3 | Information access restriction | ✅ | GitHub access control; `.env` local only |
| 8.4 | Access to source code | ✅ | GitHub owner-only write access |
| 8.5 | Secure authentication | ✅ | GitHub MFA; Azure MFA recommended |
| 8.6 | Capacity management | ⚠️ | Azure auto-scales; local Flask for dev |
| 8.7 | Protection against malware | ✅ | Windows Defender / standard AV |
| 8.8 | Management of technical vulnerabilities | ⚠️ | `pip` packages updated; GitHub Dependabot |
| 8.9 | Configuration management | ✅ | `.env` config; `requirements.txt` pinned |
| 8.10 | Information deletion | ✅ | No persistent user data; session-only |
| 8.11 | Data masking | ➖ | No personal data stored |
| 8.12 | Data leakage prevention | ✅ | `.gitignore` prevents credential leakage |
| 8.13 | Information backup | ✅ | GitHub is full code backup |
| 8.14 | Redundancy of information processing | ✅ | Mock mode fallback for Azure outages |
| 8.15 | Logging | ⚠️ | Flask dev logs; Azure logging available |
| 8.16 | Monitoring activities | ⚠️ | `/api/metrics` endpoint; Azure portal |
| 8.17 | Clock synchronization | ✅ | OS-level NTP |
| 8.18 | Use of privileged utility programs | ✅ | Standard Python tooling only |
| 8.19 | Installation of software on operational systems | ✅ | `requirements.txt` controls dependencies |
| 8.20 | Networks security | ⚠️ | HTTPS to Azure; CORS restricted |
| 8.21 | Security of network services | ✅ | Azure OpenAI — TLS encrypted |
| 8.22 | Segregation of networks | ➖ | Not applicable at current scale |
| 8.23 | Web filtering | ➖ | Not applicable |
| 8.24 | Use of cryptography | ✅ | HTTPS for all Azure communications; API key encryption in transit |
| 8.25 | Secure development lifecycle | ✅ | Full SDLC documentation; CI pipeline |
| 8.26 | Application security requirements | ✅ | API contracts documented; error handling standardized |
| 8.27 | Secure system architecture and engineering | ✅ | System design documented; mock/live separation |
| 8.28 | Secure coding | ✅ | No hardcoded secrets; input validation |
| 8.29 | Security testing in development and acceptance | ✅ | Unit tests; CI pipeline |
| 8.30 | Outsourced development | ✅ | Claude AI used for development — under Anthropic terms |
| 8.31 | Separation of development, test, and production | ⚠️ | Mock mode = test; live mode = production |
| 8.32 | Change management | ✅ | Git commits; version history |
| 8.33 | Test information | ✅ | Evaluation uses synthetic prompts — no real user data |
| 8.34 | Protection of information systems during audit testing | ➖ | Not applicable at current scale |

---

*Template adapted from ICT Institute Statement of Applicability ISO 27001-2022 under Creative Commons Attribution License.*
*Source: https://github.com/swzaken/freetemplates*
