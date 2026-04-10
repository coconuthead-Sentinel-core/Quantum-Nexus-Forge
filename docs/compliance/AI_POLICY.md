# AI Policy
## Quantum Nexus Forge v5.0.2

**Template source:** ICT Institute — AI Policy Template V1.0 (CC Attribution License)
**Adapted by:** Shannon Bryan Kelly
**Implementation:** Claude AI (Anthropic)
**Effective Date:** April 2026
**Review Date:** April 2027

---

## 1. Purpose and Scope

This policy governs the design, development, operation, and use of artificial intelligence within the **Quantum Nexus Forge** platform. It applies to:

- Shannon Bryan Kelly (Architect / Owner)
- Any contractors, consultants, or contributors working on the platform
- Any end users interacting with the system

---

## 2. What Quantum Nexus Forge Is

Quantum Nexus Forge is an AI-powered multi-agent orchestration platform. It routes user prompts through five named AI agents powered by **Azure OpenAI GPT-5.4-nano**:

| Agent | Role |
|-------|------|
| Shannon-Sentinel | Lead Architect — activates the field |
| Mirror-Pool | Pattern Reflector — surfaces hidden patterns |
| Nexus-Node | Core Connector — bridges concepts |
| Omega-1 | Deep Processor — final synthesis |
| A1-Forge | Filing Architect — classifies and archives |

The system processes text prompts and returns multi-perspective AI-generated responses.

---

## 3. Acceptable Use Principles

### ✅ Acceptable Use
- Personal knowledge exploration and synthesis
- Creative ideation and problem-solving support
- Research and concept mapping
- Portfolio and demonstration purposes
- Internal business use by the architect

### ❌ Unacceptable Use
- Generating content that discriminates on the basis of race, gender, disability, religion, or other protected characteristics
- Producing false, misleading, or defamatory content presented as fact
- Attempting to bypass AI safety guardrails
- Processing sensitive personal data (health, financial, legal) without explicit consent and DPIA review
- Using the platform as a substitute for licensed professional advice (medical, legal, financial)
- Reverse-engineering or extracting Azure OpenAI model weights or training data

---

## 4. AI Act Compliance

### Risk Classification
Under the EU AI Act, Quantum Nexus Forge is classified as a **General-Purpose AI application** — not a high-risk AI system as defined in Annex III of the AI Act.

**Rationale:**
- The system does not make consequential decisions about individuals
- It does not affect employment, credit, law enforcement, or critical infrastructure
- It is a knowledge exploration and synthesis tool

### Obligations Under the AI Act
- **Transparency:** Users are informed they are interacting with AI agents
- **Human oversight:** All outputs are advisory — no automated decisions without human review
- **Documentation:** This policy and the FRIA serve as the required AI governance documentation
- **Prohibited practices:** None of the practices prohibited under Article 5 of the AI Act are present in this system

---

## 5. Privacy and GDPR Compliance

- **No personal data is collected** by default — the system does not require login or registration
- User prompts are processed in memory only and are not stored persistently (unless Cosmos DB is enabled)
- If Cosmos DB persistence is enabled, a full DPIA review must be completed before deployment
- Azure OpenAI processes prompts under Microsoft's data processing terms — no model training on user data
- Users should not enter personal data (names, addresses, health information) into prompts

---

## 6. Approved AI Services

| Service | Provider | Purpose | Status |
|---------|----------|---------|--------|
| Azure OpenAI (GPT-5.4-nano) | Microsoft | Core AI responses | ✅ Approved |
| Claude AI (Anthropic) | Anthropic | Development assistance | ✅ Approved |
| GitHub Copilot | Microsoft/GitHub | Code assistance | ✅ Approved (no proprietary code) |
| ChatGPT (OpenAI) | OpenAI | Research only | ⚠️ Approved — no confidential data |
| Gemini | Google | Research only | ⚠️ Approved — no confidential data |

**Rule:** No proprietary source code, credentials, API keys, or personal data may be entered into public AI tools (ChatGPT, Gemini, DALL-E, etc.).

---

## 7. Transparency Requirements

- All AI-generated responses must be clearly identified as AI-generated
- Agent names (Shannon-Sentinel, Mirror-Pool, etc.) are displayed alongside responses
- The system does not impersonate real human individuals
- Mock mode vs. live AI mode is always declared in `/api/status`

---

## 8. Security and Confidentiality

- Azure API keys are stored in `.env` files — never committed to GitHub
- `.gitignore` excludes all `.env` files from version control
- Azure OpenAI endpoint and deployment names are treated as confidential
- Any future multi-user deployment requires authentication review before launch

---

## 9. Training and Awareness

- This policy must be reviewed by any contributor before working on the platform
- All AI outputs must be verified before use in any client-facing or public-facing context
- Contributors must not use platform outputs as professional advice

---

## 10. Incident Reporting

If an AI output causes harm, produces discriminatory content, or behaves unexpectedly:
1. Document the prompt and output immediately
2. Log the incident in `docs/compliance/INCIDENT_LOG.md`
3. Disable live AI mode (`MOCK_AI=true`) if needed
4. Review and remediate before re-enabling

---

## 11. Policy Review

This policy is reviewed annually or when:
- A new AI service is added
- The EU AI Act implementing rules are updated
- A significant incident occurs
- The platform is deployed to new users or contexts

---

*Template adapted from ICT Institute AI Policy Template V1.0 under Creative Commons Attribution License.*
*Source: https://github.com/swzaken/freetemplates*
