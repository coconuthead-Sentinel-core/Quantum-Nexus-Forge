# System Design Document
## Quantum Nexus Forge v5.0.2

**Architect:** Shannon Bryan Kelly
**Implementation:** Claude AI (Anthropic)
**Date:** April 2026

---

## 1. Architecture Overview

```
[ User / Browser ]
       |
       | HTTP requests
       ↓
[ Flask Web Server — app.py — localhost:5000 ]
       |
       ├── GET  /                    → frontend/index.html (chat UI)
       ├── GET  /dashboard           → frontend/dashboard.html (Metatron's Cube)
       ├── POST /api/v1/orchestrate  → QuantumNexusEngine.orchestrate()
       ├── GET  /api/metrics         → QuantumNexusEngine.get_metrics()
       ├── GET  /api/status          → Health + Azure mode check
       └── POST /api/process         → SymbolicProcessor.process_input()
                |
                ↓
[ QuantumNexusEngine ]
       |
       ├── SymbolicProcessor      — 7-slot rolling matrix, concept extraction
       ├── A1FilingSystem         — Tri-zone memory (GREEN/YELLOW/RED)
       ├── Background Heartbeat   — Updates metrics every 3 seconds
       └── azure_adapter.py       — Routes to Azure OpenAI or mock fallback
                |
                ↓
[ Azure OpenAI — GPT-5.4-nano ]
  https://sbryank1234-0009-resource.cognitiveservices.azure.com/
```

---

## 2. Module Boundaries

| Module | File | Responsibility |
|--------|------|----------------|
| Web server | `app.py` | Flask routing, request handling, server startup |
| AI adapter | `azure_adapter.py` | Azure OpenAI calls, mock fallback, agent system prompts |
| Frontend chat | `frontend/index.html` | Multi-assistant chat UI |
| Frontend dashboard | `frontend/dashboard.html` | Animated SVG metrics display |
| Evaluation | `evaluation/run_eval.py` | 20-prompt scoring pipeline |
| Tests | `tests/test_engine.py` | Unit test suite |
| CI | `.github/workflows/python-app.yml` | Automated build and test |
| Config | `.env` | Live credentials (never committed to git) |
| Config template | `.env.example` | Safe reference for developers |

---

## 3. Key Data Structures

### Agent Turn
```json
{
  "agent": "Shannon-Sentinel",
  "text": "The Quantum Nexus Forge activated at 97.1% resonance...",
  "zone": "GREEN"
}
```

### Orchestration Response
```json
{
  "turns": [ ...agent turns... ],
  "monitor": "System resonance: 0.941 | Nodes processed: 9 | GREEN: 5 | YELLOW: 2 | RED: 1"
}
```

### Metrics Response
```json
{
  "system_status": "GREEN",
  "uptime_seconds": 3600,
  "total_nodes": 42,
  "system_resonance": 0.923,
  "sigil_status": { "CHALLENGE": 0.89, "EMERGE": 0.94, ... },
  "filing_metrics": { "green": {...}, "yellow": {...}, "red": {...} },
  "activity_log": [...],
  "performance": { "current": {...}, "history": {...} }
}
```

### QuantumNode
```python
{
  "id": "node_qn_1712345678901",
  "type": "COGNITIVE",
  "concept": "quantum_nexus",
  "entropy": 0.847,
  "resonance": 0.923,
  "state": "ACTIVE",
  "timestamp": "2026-04-10T15:22:00"
}
```

---

## 4. Workflows

### Prompt Orchestration Flow
```
1. User submits prompt via POST /api/v1/orchestrate
2. QuantumNexusEngine.orchestrate() receives prompt
3. SymbolicProcessor.process_input() extracts concepts + intent
4. For each agent (Shannon-Sentinel, Mirror-Pool, Nexus-Node, Omega-1, A1-Forge):
   a. azure_adapter.get_agent_response() called
   b. If MOCK_AI=false: Azure OpenAI GPT-5.4-nano called with agent system prompt
   c. If MOCK_AI=true: template response returned
   d. QuantumNode created, filed into A1FilingSystem (GREEN/YELLOW/RED)
5. All turns collected, monitor string built
6. JSON response returned to browser
7. Chat UI displays each agent's response
```

### Background Heartbeat Flow
```
Every 3 seconds (background thread):
  - Update sigil elements (CHALLENGE, EMERGE, MIRROR, GUIDE, FRIEND)
  - Adjust neural balance (left/right brain)
  - Record performance metrics (latency, throughput, CPU, memory)
  - Randomly add activity log entry
```

---

## 5. Failure Modes

| Failure | Detection | Recovery |
|---------|-----------|----------|
| Azure OpenAI unreachable | Exception in `_live_response()` | Falls back to mock template automatically |
| Missing `.env` file | `MOCK_MODE = True` on startup | Runs in mock mode — no crash |
| Wrong deployment name | `DeploymentNotFound` 404 error | Caught, falls back to mock |
| Port 5000 in use | `OSError` on `app.run()` | User must free port or change port in `.env` |
| Missing Flask | `ImportError` | `_ensure_deps()` auto-installs on startup |

---

## 6. Security Design

- API keys stored only in `.env` (local, never committed)
- `.env` listed in `.gitignore` — verified excluded from all commits
- `CORS` enabled for local development — restrict origins in production
- No authentication on endpoints currently — acceptable for local use
- Azure Key Vault integration: planned for production deployment
