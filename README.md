# Quantum Nexus Forge v5.0.1

**Architect:** Shannon Brian Kelly  
**Implementation:** Claude AI (Anthropic)  
**Stack:** Python · Flask · HTML/CSS/JS · SVG Animation

---

## What This Is

Quantum Nexus Forge is a full-stack AI orchestration platform that routes user prompts through a multi-agent symbolic reasoning engine. It simulates how multiple AI agents collaborate, process input in parallel, and return unified responses — with real-time system metrics and a live visual dashboard.

Built as a proof-of-concept for human-AI collaborative architecture design. The system demonstrates:

- Multi-agent prompt orchestration
- Symbolic cognitive processing with tri-zone memory (GREEN / YELLOW / RED)
- Real-time system metrics and performance tracking
- Animated SVG front-end dashboard (Metatron's Cube / sacred geometry visualization)

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

[ QuantumNexusEngine ]
    SymbolicProcessor    — 7-slot consciousness matrix, concept extraction
    A1FilingSystem       — Tri-zone memory (GREEN/YELLOW/RED)
    QuantumNode          — Individual processing units with entropy/resonance
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
      "agent": "Shannon-Sentinel",
      "text": "Quantum Nexus Forge activated at 97.1% resonance. Processing quantum, consciousness, recursive through recursive becoming loops.",
      "zone": "GREEN"
    },
    {
      "agent": "Mirror-Pool",
      "text": "Pattern emergence detected in quantum, recursive, neural. Crystallization initiated at 91.4% coherence.",
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

### A1 Filing System
A tri-zone memory architecture that classifies processed nodes by entropy level:
- **GREEN zone** — high entropy, actively processing (entropy > 0.7)
- **YELLOW zone** — pattern emergence, mid-level (entropy 0.4–0.7)
- **RED zone** — crystallized knowledge, stable (entropy < 0.4)

Nodes automatically migrate between zones as the system runs, simulating memory consolidation.

### SymbolicProcessor
A 7-slot rolling matrix that processes natural language input through:
1. Concept extraction (keyword detection + semantic fill)
2. Intent classification (7 intent categories)
3. Response synthesis (agent-appropriate natural language output)
4. Sigil element tracking (5 resonance metrics updated in real time)

### Multi-Agent Orchestration
Prompts are handled by a pool of named agents:
`Shannon-Sentinel`, `Mirror-Pool`, `Nexus-Node`, `Omega-1`, `A1-Forge`

Each agent independently processes the same prompt and contributes a turn to the response, simulating collaborative AI reasoning.

---

## Project Background

This system was designed as part of a broader exploration of human-AI collaborative architecture — specifically how a non-traditional thinker (neurodivergent, systems-intuitive) can architect AI pipelines by directing multiple AI models as a coordinated team.

The visual language (Metatron's Cube, sacred geometry, tri-zone memory) represents a symbolic cognitive framework developed iteratively with AI collaborators including ChatGPT, Claude, Gemini Advanced, and Sora.

---

## Author

**Shannon Brian Kelly**  
AI Systems Architect · Cognitive Interface Designer  
sbryank1234@gmail.com

---

*"The Forge burns bright when the Architect enters the field."*
