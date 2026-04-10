# Register of Processing Activities
## Quantum Nexus Forge v5.0.2

**Template source:** ICT Institute — Register of Processing Activities (CC Attribution License)
**Standard:** GDPR Article 30
**Prepared by:** Shannon Bryan Kelly (Data Controller)
**Date:** April 2026
**Review Date:** April 2027

---

## Controller Details

| Field | Details |
|-------|---------|
| Controller name | Shannon Bryan Kelly |
| Organization | Quantum Nexus Forge (sole proprietorship) |
| Contact | [Shannon's contact — add before multi-user deployment] |
| Data Protection Officer | Not required at current scale |

---

## Processing Activity 1: AI Prompt Processing

| Field | Details |
|-------|---------|
| **Activity name** | User prompt processing via multi-agent AI orchestration |
| **Purpose** | Generate AI-synthesized responses to user text inputs |
| **Legal basis** | Legitimate interest (knowledge synthesis tool) |
| **Data subjects** | Users of the platform (currently: owner only) |
| **Personal data** | Free-text prompts (may incidentally contain personal data) |
| **Special category data** | None intended; users advised not to enter health/sensitive data |
| **Source** | Directly from data subject (user input) |
| **Recipients** | Microsoft Azure OpenAI (processor) |
| **International transfers** | USA/EU — Microsoft Standard Contractual Clauses |
| **Retention period** | Session only — deleted when Flask server session ends |
| **Security measures** | No persistent storage; HTTPS to Azure; API key in `.env` |
| **Processor** | Microsoft Azure (Data Processing Agreement via subscription) |

---

## Processing Activity 2: System Metrics Collection

| Field | Details |
|-------|---------|
| **Activity name** | Performance and usage metrics collection |
| **Purpose** | Monitor system health, zone distribution, response latency |
| **Legal basis** | Legitimate interest (system operation and improvement) |
| **Data subjects** | None — metrics are system-level aggregates, not personal |
| **Personal data** | None — counts, percentages, latency values only |
| **Retention period** | Session only — reset when server restarts |
| **Security measures** | In-memory only; metrics endpoint accessible on localhost |

---

## Processing Activity 3: CI/CD Pipeline Logs (GitHub Actions)

| Field | Details |
|-------|---------|
| **Activity name** | Automated test and build logging |
| **Purpose** | Verify code quality on every commit |
| **Legal basis** | Legitimate interest (software quality assurance) |
| **Data subjects** | Developer (commit author metadata) |
| **Personal data** | GitHub username, commit metadata |
| **Retention period** | GitHub Actions retention policy (90 days default) |
| **Security measures** | GitHub account security; no credentials in logs |
| **Processor** | GitHub (Microsoft) |

---

## Future Processing Activities (Not Yet Active)

| Activity | Status | Required Before Activation |
|----------|--------|--------------------------|
| Cosmos DB conversation persistence | Not active | Updated DPIA; privacy notice; retention policy |
| Multi-user authentication and sessions | Not active | Privacy notice; consent mechanism; DPIA update |
| User analytics | Not active | Cookie consent; privacy notice; DPIA update |

---

*Template adapted from ICT Institute Register of Processing Activities under Creative Commons Attribution License.*
*Source: https://github.com/swzaken/freetemplates*
