# Quantum Nexus Forge

**Architect:** Shannon Bryan Kelly  
**Implementation:** Claude AI (Anthropic)  
**Stack:** Python, Flask, HTML/CSS/JS, SVG animation  
**Current documented version:** v5.0.2

---

## What This Is

Canonical public name: **Quantum Nexus Forge**.
Use `Quantum Nexus` only when the platform context is explicit.
Do not use plain `Nexus` as a standalone synonym for this project.

Quantum Nexus Forge is a full-stack AI orchestration platform that routes user prompts through a multi-agent symbolic reasoning engine. It simulates how multiple AI agents collaborate, process input in parallel, and return unified responses with real-time system metrics and a live visual dashboard.

Built as a proof-of-concept for human-AI collaborative architecture design. The system demonstrates:

- Multi-agent prompt orchestration
- Symbolic cognitive processing with tri-zone memory (GREEN / YELLOW / RED)
- Real-time system metrics and performance tracking
- Animated SVG front-end dashboard (hexagonal lattice visualization)

## Current Status

- The repository contains a working Flask backend, static frontend, and mock AI path for local demonstration.
- Mock mode is available for local development and portfolio review.
- Live Azure mode remains config-driven and still depends on correct Azure endpoint, key, and deployment setup.
- Local automated validation is green: `pytest -q` passed with `15 passed` on `2026-04-24`.
- The most accurate description of this repository today is proof-of-concept / MVP, not verified market-ready cloud deployment.

---

## Architecture

```text
[ Browser Frontend ]
    index.html          - Multi-assistant chat UI
    dashboard.html      - Animated visual system display

        <-> HTTP (fetch API)

[ Flask Backend - app.py ]
    POST /api/v1/orchestrate   - Multi-agent prompt routing
    GET  /api/metrics          - Live system snapshot
    GET  /api/status           - Health check
    POST /api/process          - Single-node symbolic processing

        <-> Internal engine

[ QuantumNexusEngine ]
    InputAnalyzer        - Concept extraction and intent classification
    TieredMemoryStore    - Tri-zone memory (HIGH/MEDIUM/LOW priority)
    ProcessingNode       - Individual processing units with entropy tracking
    Background Heartbeat - Live system updates every 3 seconds
```

Implementation note: the current code is centered on `QuantumNexusEngine`, `SymbolicProcessor`, `A1FilingSystem`, and `QuantumNode` in `app.py`. The architecture block above is conceptual and not a 1:1 class map.

---

## Live Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `POST` | `/api/v1/orchestrate` | Send a prompt and receive multi-agent responses |
| `GET` | `/api/metrics` | Full system snapshot (nodes, zones, performance) |
| `GET` | `/api/status` | Lightweight health check |
| `POST` | `/api/process` | Single symbolic processing pass |

### Example Request

```bash
curl -X POST http://localhost:5000/api/v1/orchestrate \
  -H "Content-Type: application/json" \
  -d '{"prompt": "activate quantum nexus recursive consciousness", "rounds": 2}'
```

### Example Response

```json
{
  "turns": [
    {
      "agent": "Shannon-Sentinel",
      "text": "Quantum Nexus Forge activated at 97.1% resonance. Processing quantum, recursive, consciousness through recursive becoming loops.",
      "zone": "GREEN"
    },
    {
      "agent": "Mirror-Pool",
      "text": "Pattern emergence detected in quantum, recursive, consciousness. Reflection coherence holds at 91.4%.",
      "zone": "YELLOW"
    }
  ],
  "monitor": "System resonance: 0.941 | Nodes processed: 9 | GREEN: 5 | YELLOW: 2 | RED: 1"
}
```

---

## How to Run

**Requirements:** Python 3.10+

```bash
git clone https://github.com/YOUR_USERNAME/quantum-nexus-forge.git
cd quantum-nexus-forge
pip install -r requirements.txt
python app.py
```

Then open your browser:

- **Multi-Assistant UI:** http://localhost:5000/
- **Visual Dashboard:** http://localhost:5000/dashboard
- **System Status:** http://localhost:5000/api/status

---

## Key Components

### TieredMemoryStore

A tri-zone memory architecture that classifies processed nodes by entropy level:

- **HIGH zone** - high entropy, actively processing (entropy > 0.7)
- **MEDIUM zone** - pattern emergence, mid-level (entropy 0.4-0.7)
- **LOW zone** - archived knowledge, stable (entropy < 0.4)

Nodes automatically migrate between zones as the system runs, simulating memory consolidation.

### InputAnalyzer

A rolling matrix that processes natural language input through:

1. Concept extraction (keyword detection plus semantic fill)
2. Intent classification (7 intent categories)
3. Response synthesis (agent-appropriate natural language output)
4. System metrics tracking (updated in real time)

### Multi-Agent Orchestration

Prompts are handled by a pool of specialized agents:
`ArchitectAgent`, `PatternAnalysisAgent`, `ConnectorAgent`, `SynthesisAgent`, `ClassificationAgent`

Each agent independently processes the same prompt and contributes a turn to the response, simulating collaborative AI reasoning.

---

## Project Background

This system was designed as part of a broader exploration of human-AI collaborative architecture, specifically how a non-traditional thinker can architect AI pipelines by directing multiple AI models as a coordinated team.

The visual language (hexagonal lattice, tri-zone memory) represents a symbolic cognitive framework developed iteratively with AI collaborators including ChatGPT, Claude, Gemini Advanced, and Sora.

---

## Author

**Shannon Bryan Kelly**  
AI Systems Architect and Cognitive Interface Designer  
sbryank1234@gmail.com
