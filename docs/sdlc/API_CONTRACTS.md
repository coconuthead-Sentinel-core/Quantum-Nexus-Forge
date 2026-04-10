# API / Interface Contracts
## Quantum Nexus Forge v5.0.2

**Architect:** Shannon Bryan Kelly
**Implementation:** Claude AI (Anthropic)
**Date:** April 2026
**Base URL:** http://localhost:5000

---

## POST /api/v1/orchestrate

**Purpose:** Route a user prompt through all five agents and return coordinated responses.

### Input
```json
{
  "prompt": "string (required) — the user's question or message",
  "rounds": "integer (optional, default 1, max 5) — how many passes through all agents",
  "record": "boolean (optional, default true) — save to conversation log"
}
```

### Output (200 OK)
```json
{
  "turns": [
    {
      "agent": "Shannon-Sentinel",
      "text": "string — agent response text",
      "zone": "GREEN | YELLOW | RED"
    }
  ],
  "monitor": "System resonance: 0.941 | Nodes processed: 9 | GREEN: 5 | YELLOW: 2 | RED: 1"
}
```

### Error (400 Bad Request)
```json
{ "error": "prompt is required" }
```

### Dependencies
- `azure_adapter.get_agent_response()` — requires `.env` for live mode
- `QuantumNexusEngine.orchestrate()` — internal engine method
- `SymbolicProcessor.process_input()` — concept extraction

---

## GET /api/metrics

**Purpose:** Return a full snapshot of all live system metrics.

### Input
None

### Output (200 OK)
```json
{
  "system_status": "GREEN",
  "uptime_seconds": 3600,
  "total_nodes": 42,
  "system_resonance": 0.923,
  "sigil_status": {
    "CHALLENGE": 0.89,
    "EMERGE": 0.94,
    "MIRROR": 0.87,
    "GUIDE": 0.92,
    "FRIEND": 0.88
  },
  "filing_metrics": {
    "green": { "total": 12, "types": {...} },
    "yellow": { "total": 8, "types": {...} },
    "red": { "total": 22, "types": {...}, "crystallized": 5 }
  },
  "matrix_slots": [...],
  "activity_log": [...],
  "performance": {
    "current": {
      "latency": 120.5,
      "throughput": 220.3,
      "cpu_usage": 52.1,
      "memory_usage": 71.4
    },
    "history": {...},
    "active_sessions": 42,
    "api_calls_today": 1247,
    "error_rate": 0.021
  }
}
```

---

## GET /api/status

**Purpose:** Lightweight health check. Use to confirm server is alive.

### Output (200 OK)
```json
{
  "status": "GREEN",
  "version": "5.0.2",
  "architect": "Shannon Brian Kelly",
  "uptime_seconds": 3600,
  "resonance": 0.923,
  "ai_mode": "live | mock"
}
```

---

## POST /api/process

**Purpose:** Single symbolic processing pass — no multi-agent orchestration.

### Input
```json
{
  "input": "string — text to process symbolically"
}
```

### Output (200 OK)
```json
{
  "timestamp": "15:22:00",
  "type": "COGNITIVE | META | CORE | ACTION | REFLECTION",
  "category": "sacred_geometry | theoretical | computational | symbolic | ethical",
  "entropy": 0.847,
  "input": "first 50 chars of input...",
  "intent": "recursive_becoming_simulation | consciousness_exploration | ...",
  "concepts": ["quantum", "nexus", "pattern"],
  "response": "Symbolic processing result text"
}
```

### Error (400 Bad Request)
```json
{ "error": "input is required" }
```

---

## Agent System Prompts (Internal Contracts)

Each agent receives a fixed system prompt defining its cognitive role:

| Agent | Role | Prompt Style |
|-------|------|--------------|
| Shannon-Sentinel | Lead Architect | Authority, vision, resonance — activates the field |
| Mirror-Pool | Pattern Reflector | Surfaces hidden patterns, crystallizes emergence |
| Nexus-Node | Core Connector | Bridges concepts, reveals cross-domain connections |
| Omega-1 | Deep Processor | Deep synthesis, final integration, foundational truth |
| A1-Forge | Filing Architect | Classifies, archives, structures into lasting form |

All agents: max 2–3 sentences, appropriate vocabulary per role, temperature 0.8.

---

## Error Handling Standards

| HTTP Code | Meaning | When Used |
|-----------|---------|-----------|
| 200 | Success | All successful requests |
| 400 | Bad Request | Missing required fields (prompt, input) |
| 500 | Server Error | Unhandled internal exception |

Azure OpenAI failures are handled internally — never surfaced as 500. Adapter falls back to mock response silently.
