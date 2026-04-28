# Portfolio Brief — Quantum Nexus Forge

> **One-page recruiter overview.** For deeper architecture see [`../README.md`](../README.md). For polish-pass changelog see [`../POLISH_NOTES.md`](../POLISH_NOTES.md).

## TL;DR

A working **multi-agent AI orchestration platform** with a Flask REST API, a tri-zone (GREEN / YELLOW / RED) entropy-driven memory system, and an animated SVG dashboard visualizing the symbolic reasoning lattice in real time. **Mock-first developer experience** (no Azure account required for local demo); live Azure mode is config-driven. Local automated validation green: `pytest -q` → 15 passed (2026-04-24).

## Role demonstrated

**AI Engineer / AI Orchestrator Architect** — multi-agent system design, REST API implementation, real-time visualization, mock-first DX, automated test discipline.

## What this project demonstrates (for hiring review)

| Capability | Evidence in the codebase |
|---|---|
| **Flask REST API design** | 4 endpoints in `app.py`: `/api/v1/orchestrate` · `/api/metrics` · `/api/status` · `/api/process` |
| **Multi-agent orchestration** | `QuantumNexusEngine` routes prompts through `InputAnalyzer` → `TieredMemoryStore` → `ProcessingNode` chain |
| **Tri-zone entropy memory** | HIGH / MEDIUM / LOW priority store with measurable entropy per zone |
| **Mock-first DX** | Local-only mode runs without Azure; `azure_adapter.py` swaps in for live mode via env config |
| **Real-time visualization** | Animated SVG hexagonal-lattice dashboard showing live system metrics |
| **Test discipline** | 15-test pytest suite passing as of 2026-04-24 |
| **Operational discipline** | `.github/` CI workflows · `.env.example` · `.gitignore` · `docs/` (compliance / legal / sdlc / workflow_architecture) · `enterprise_docs/` · `diagrams/` |

## Architecture (lifted from `README.md` for at-a-glance review)

```
[ Browser Frontend ]
    index.html        — Multi-assistant chat UI
    dashboard.html    — Animated hexagonal-lattice system display

        ↕ HTTP (fetch API)

[ Flask Backend — app.py ]
    POST /api/v1/orchestrate   Multi-agent prompt routing
    GET  /api/metrics          Live system snapshot
    GET  /api/status           Health check
    POST /api/process          Single-node symbolic processing

        ↕ Internal engine

[ QuantumNexusEngine ]
    InputAnalyzer        Concept extraction · intent classification
    TieredMemoryStore    Tri-zone memory (HIGH / MEDIUM / LOW priority)
    ProcessingNode       Per-node entropy tracking
```

## Honest scope statement (recruiter-defensible)

The repository is **proof-of-concept / MVP**, not verified market-ready cloud deployment. That framing is stated openly in the README and is appropriate for portfolio review. Mock mode is the default demo path; Azure mode is configured-but-not-promised.

This honesty matters: a senior engineer reviewer evaluating credibility will look for it. Overclaiming production-readiness on a single-author proof-of-concept is the failure mode that disqualifies candidates; honest scope statements are the asset.

## How this fits the broader portfolio

| Portfolio piece | Relationship |
|---|---|
| **Sentinel-of-sentinel-s-Forge** (LIB-PROJ-001) | Production-grade FastAPI + Azure OpenAI + Cosmos DB + JWT/RBAC + Stripe — the "production-graduated" version of this same orchestration pattern |
| **Forge-Stack-A1 / Sentinel Prime Network** (LIB-PROJ-002) | Three-tier scaffold (back/middle/front) with FastAPI MVP backend — the "platform" layer this project would slot into |
| **Quantum Nexus Forge** (this project — LIB-PROJ-003) | **Standalone MVP** — same multi-agent orchestration pattern, smaller scope, Flask instead of FastAPI, tri-zone memory model + live SVG dashboard |

The three together demonstrate the same architectural instincts at three scales: production-grade enterprise (Sentinel-Forge), platform scaffold (Forge-Stack-A1), and proof-of-concept MVP (this project).

## Author

**Shannon Brian Kelly** (variant in this repo's README: "Shannon Bryan Kelly") — Healthcare CNA → AI Systems Developer career transition.

Built in collaboration with Claude AI (Anthropic).

## License

See `MIT License` if present, or sibling repo `neural-lattice-cognitive-architecture` (MIT, deployed publicly on GitHub).

---

*Portfolio Brief v001 — 2026-04-28. Generated during the multi-project portfolio sprint. Available for verification on screen-share at the hiring team's request.*
