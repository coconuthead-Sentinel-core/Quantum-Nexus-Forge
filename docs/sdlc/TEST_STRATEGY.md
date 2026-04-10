# Test Strategy
## Quantum Nexus Forge v5.0.2

**Architect:** Shannon Bryan Kelly
**Implementation:** Claude AI (Anthropic)
**Date:** April 2026

---

## 1. Testing Philosophy

Every feature must be verifiable before it is considered done. Tests protect the multi-agent orchestration pipeline from regressions and ensure Azure OpenAI integration degrades gracefully to mock mode when credentials are unavailable.

---

## 2. Test Levels

### Unit Tests — `tests/test_engine.py`

| Test ID | What It Covers | Pass Criteria |
|---------|---------------|---------------|
| UT-001 | `QuantumNode` creation | Node has id, content, entropy, zone, state |
| UT-002 | `QuantumNode` zone assignment (GREEN) | entropy > 0.7 → zone == "GREEN" |
| UT-003 | `QuantumNode` zone assignment (YELLOW) | entropy 0.4–0.7 → zone == "YELLOW" |
| UT-004 | `QuantumNode` zone assignment (RED) | entropy < 0.4 → zone == "RED" |
| UT-005 | `A1FilingSystem.file_node()` GREEN | Node filed to green list |
| UT-006 | `A1FilingSystem.file_node()` YELLOW | Node filed to yellow list |
| UT-007 | `A1FilingSystem.file_node()` RED | Node filed to red list |
| UT-008 | `SymbolicProcessor.process_input()` | Returns dict with timestamp, type, entropy |
| UT-009 | `QuantumNexusEngine.orchestrate()` | Returns list of agent turns |
| UT-010 | `azure_adapter` mock mode | Returns non-empty string, no API call |
| UT-011 | `azure_adapter` agent name pass-through | Response text references agent context |
| UT-012 | `QuantumNexusEngine` metrics | total_nodes increments after processing |

**Run command:**
```bash
python -m pytest tests/ -v
```

**Current status:** 12/12 tests passing ✅

---

### Integration Tests — Manual

| Test ID | Scenario | Steps | Pass Criteria |
|---------|----------|-------|---------------|
| IT-001 | Flask server starts | `python app.py` | Browser opens, no errors in console |
| IT-002 | `/api/status` endpoint | GET http://localhost:5000/api/status | Returns JSON with `status`, `version`, `ai_mode` |
| IT-003 | `/api/v1/orchestrate` with mock | POST with `MOCK_AI=true` | Returns 5 agent turns, zone labels |
| IT-004 | `/api/v1/orchestrate` with live AI | POST with `MOCK_AI=false` | Returns 5 agent turns, non-template text |
| IT-005 | `/api/metrics` endpoint | GET http://localhost:5000/api/metrics | Returns full metrics JSON snapshot |
| IT-006 | `/api/process` endpoint | POST with `{"input": "test"}` | Returns entropy, concepts, response |
| IT-007 | Frontend chat UI | Open `index.html`, type message | Sends to `/api/v1/orchestrate`, renders all 5 agents |
| IT-008 | Dashboard UI | Open `dashboard.html` | Metatron's Cube animates, metrics display |

---

### Evaluation Pipeline — `evaluation/run_eval.py`

| Metric | Target | Current Score |
|--------|--------|---------------|
| Relevance | ≥ 4.5 / 5.0 | **4.88** ✅ |
| Coherence | ≥ 4.0 / 5.0 | **4.74** ✅ |
| Groundedness | ≥ 3.0 / 5.0 | **3.45** ✅ |
| **Overall** | **≥ 4.0 / 5.0** | **4.35** ✅ |

- 20 prompts covering all 5 agents and core system behaviors
- Scores stored in `evaluation/eval_results.json`
- Evaluation runs against live Azure OpenAI when `MOCK_AI=false`

**Run command:**
```bash
python evaluation/run_eval.py
```

---

### CI Pipeline — GitHub Actions

**File:** `.github/workflows/python-app.yml`

| Stage | What Runs | Trigger |
|-------|-----------|---------|
| Install | `pip install -r requirements.txt` | Every push to master |
| Unit tests | `pytest tests/` | Every push to master |
| Lint (optional) | `flake8 app.py` | Every push to master |

CI always runs in mock mode (`MOCK_AI=true`). Azure credentials are never stored in GitHub.

---

## 3. Test Data

### Sample Prompts for Manual Testing

```
"What is the nature of consciousness?"
"How do I build resilience as a founder?"
"Explain quantum entanglement simply."
"What patterns do you see in my thinking?"
"Help me organize my next sprint."
```

### Agent Coverage Matrix

| Agent | Tested by Unit | Tested by Eval | Tested by Integration |
|-------|---------------|----------------|----------------------|
| Shannon-Sentinel | UT-009 | ✅ | IT-003 |
| Mirror-Pool | UT-009 | ✅ | IT-003 |
| Nexus-Node | UT-009 | ✅ | IT-003 |
| Omega-1 | UT-009 | ✅ | IT-003 |
| A1-Forge | UT-005, UT-006, UT-007 | ✅ | IT-003 |

---

## 4. Environments

| Environment | AI Mode | Azure Credentials | Purpose |
|-------------|---------|-------------------|---------|
| Local Dev | Mock (`MOCK_AI=true`) | Not required | Fast iteration |
| Local Live | Live (`MOCK_AI=false`) | Required in `.env` | Pre-deploy validation |
| CI (GitHub Actions) | Mock | Not present | Automated regression |
| Production | Live | Required | Real user queries |

---

## 5. Regression Policy

- Any new endpoint or agent behavior requires a unit test before merge
- Evaluation score must not drop below 4.0/5.0 overall after any change
- CI must pass before any commit is considered deployable
- Thread safety changes require manual concurrent load testing

---

## 6. Known Gaps

| Gap | Risk | Mitigation |
|-----|------|------------|
| No load / stress tests | Concurrent users may hit race conditions | `threading.Lock()` on shared state (QNF-022) |
| No Cosmos DB integration tests | Persistence not yet wired | Planned in QNF-021 |
| No CORS restriction test | Non-local origins could call API | Planned in QNF-023 |
| No end-to-end browser automation | UI regressions caught manually only | Future: Playwright or Selenium |

---

## Definition of Test Done

A test is DONE when:
- [ ] Test written and passes locally
- [ ] Test covers both happy path and failure case
- [ ] CI pipeline passes with new test included
- [ ] No existing tests broken by new code
