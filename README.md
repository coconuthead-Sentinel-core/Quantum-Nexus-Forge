# Quantum Nexus Forge v5.0.1

**Architect:** Shannon Bryan Kelly  
**Implementation:** Claude AI (Anthropic)  
**Stack:** Python · Flask · HTML/CSS/JS · SVG Animation

---

## What This Is

Quantum Nexus Forge is a full-stack AI orchestration platform that routes user prompts through a multi-agent symbolic reasoning engine. It simulates how multiple AI agents collaborate, process input in parallel, and return unified responses — with real-time system metrics and a live visual dashboard.

Built as a proof-of-concept for human-AI collaborative architecture design. The system demonstrates:

- Multi-agent prompt orchestration
- Symbolic cognitive processing with tri-zone memory (GREEN / YELLOW / RED)
- Real-time system metrics and performance tracking
- Animated SVG front-end dashboard (hexagonal lattice visualization)

---

## Architecture

```
[ Browser Frontend ]
    index.html          — Multi-assistant chat UI
    dashboard.html      — Animated visual system display

        ↕  HTTP (fetch API)

[ Flask Backend — app.py ]
    POST /api/v1/orchestrate   — Multi-agent prompt routing
    GET  /api/metrics          — Live system snapshot
    GET  /api/status           — Health check
    POST /api/process          — Single-node symbolic processing

        ↕  Internal engine

[ MultiAgentOrchestrator ]
    InputAnalyzer        — Concept extraction and intent classification
    TieredMemoryStore    — Tri-zone memory (HIGH/MEDIUM/LOW priority)
    ProcessingNode       — Individual processing units with entropy tracking
    Background Heartbeat — Live system updates every 3 seconds
```

---

## Live Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/api/v1/orchestrate` | Send a prompt, receive multi-agent responses |
| `GET`  | `/api/metrics` | Full system snapshot (nodes, zones, performance) |
| `GET`  | `/api/status` | Lightweight health check |
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
      "agent": "ArchitectAgent",
      "text": "Quantum Nexus Forge activated at 97.1% coherence. Processing quantum, recursive, neural through analysis pipeline.",
      "zone": "HIGH"
    },
    {
      "agent": "PatternAnalysisAgent",
      "text": "Pattern emergence detected in quantum, recursive, neural. Archiving initiated at 91.4% coherence.",
      "zone": "MEDIUM"
    }
  ],
  "monitor": "System coherence: 0.941 | Nodes processed: 9 | HIGH: 5 | MEDIUM: 2 | LOW: 1"
}
```

---

## How to Run

**Requirements:** Python 3.10+

```bash
# 1. Clone the repo
git clone https://github.com/YOUR_USERNAME/quantum-nexus-forge.git
cd quantum-nexus-forge

# 2. Install dependencies
pip install -r requirements.txt

# 3. Start the server
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
- **HIGH zone** — high entropy, actively processing (entropy > 0.7)
- **MEDIUM zone** — pattern emergence, mid-level (entropy 0.4–0.7)
- **LOW zone** — archived knowledge, stable (entropy < 0.4)

Nodes automatically migrate between zones as the system runs, simulating memory consolidation.

### InputAnalyzer
A rolling matrix that processes natural language input through:
1. Concept extraction (keyword detection + semantic fill)
2. Intent classification (7 intent categories)
3. Response synthesis (agent-appropriate natural language output)
4. System metrics tracking (updated in real time)

### Multi-Agent Orchestration
Prompts are handled by a pool of specialized agents:
`ArchitectAgent`, `PatternAnalysisAgent`, `ConnectorAgent`, `SynthesisAgent`, `ClassificationAgent`

Each agent independently processes the same prompt and contributes a turn to the response, simulating collaborative AI reasoning.

---

## Project Background

This system was designed as part of a broader exploration of human-AI collaborative architecture — specifically how a non-traditional thinker (neurodivergent, systems-intuitive) can architect AI pipelines by directing multiple AI models as a coordinated team.

The visual language (hexagonal lattice, tri-zone memory) represents a symbolic cognitive framework developed iteratively with AI collaborators including ChatGPT, Claude, Gemini Advanced, and Sora.

---

## Author

**Shannon Bryan Kelly**  
AI Systems Architect · Cognitive Interface Designer  
sbryank1234@gmail.com
