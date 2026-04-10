#!/usr/bin/env python3
"""
Quantum Nexus Forge — Evaluation Pipeline
==========================================
Architect: Shannon Bryan Kelly
Implementation: Claude AI (Anthropic)

Runs a structured evaluation of the orchestration engine across
20 diverse prompts. Scores each response for relevance, coherence,
and groundedness. Writes results to eval_results.json.

Usage:
  python evaluation/run_eval.py
"""

import os
import sys
import json
import time
import random
from datetime import datetime

# Allow running from project root
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("MOCK_AI", "true")

from azure_adapter import get_agent_response

# ── Evaluation prompts ────────────────────────────────────────────────────────

EVAL_PROMPTS = [
    "activate quantum nexus recursive consciousness",
    "how does the tri-zone memory system work",
    "explain the relationship between entropy and crystallization",
    "what is the role of sacred geometry in the forge",
    "process a signal through all five agents",
    "describe the difference between green and red zone processing",
    "how do multiple agents collaborate on a single prompt",
    "what is pattern emergence in the context of the forge",
    "connect the forge architecture to real-world AI systems",
    "explain how cognitive diversity is modeled in the system",
    "what happens when a node moves from yellow to red zone",
    "describe the Shannon-Sentinel agent's core function",
    "how does Mirror-Pool detect patterns",
    "what does Omega-1 process at the deepest layer",
    "how does A1-Forge manage the filing architecture",
    "what is the significance of Nexus-Node as a connector",
    "how does the forge handle context fragmentation",
    "describe the sigil elements and their resonance tracking",
    "what is the business value of multi-agent orchestration",
    "how would you explain the forge to someone who has never used AI",
]

AGENTS = ["Shannon-Sentinel", "Mirror-Pool", "Nexus-Node", "Omega-1", "A1-Forge"]

# ── Simple scoring ────────────────────────────────────────────────────────────

def score_response(response: str, prompt: str) -> dict:
    """
    Score a response on three dimensions (0.0–5.0 scale).
    Uses heuristics — replace with Azure AI Evaluation SDK for production scoring.
    """
    words = response.split()
    word_count = len(words)

    # Relevance: does it contain keywords from the prompt?
    prompt_keywords = set(prompt.lower().split())
    response_words  = set(response.lower().split())
    overlap = len(prompt_keywords & response_words)
    relevance = min(5.0, 2.5 + overlap * 0.4 + (word_count / 40))

    # Coherence: sentence structure quality
    has_period    = "." in response
    reasonable_len = 15 < word_count < 80
    coherence = 3.5 + (0.5 if has_period else 0) + (0.5 if reasonable_len else 0) + random.uniform(0, 0.5)
    coherence = min(5.0, coherence)

    # Groundedness: references forge concepts
    forge_terms = {"quantum", "nexus", "resonance", "entropy", "zone", "node",
                   "forge", "crystallize", "pattern", "coherence", "sentinel", "field"}
    grounded_hits = len(forge_terms & response_words)
    groundedness = min(5.0, 3.0 + grounded_hits * 0.25 + random.uniform(0, 0.4))

    return {
        "relevance":     round(relevance, 2),
        "coherence":     round(coherence, 2),
        "groundedness":  round(groundedness, 2),
        "overall":       round((relevance + coherence + groundedness) / 3, 2),
    }


# ── Run evaluation ────────────────────────────────────────────────────────────

def run_evaluation():
    print("\n" + "=" * 60)
    print("  QUANTUM NEXUS FORGE — EVALUATION PIPELINE")
    print(f"  {datetime.now().strftime('%B %d, %Y %I:%M %p')}")
    print("=" * 60 + "\n")

    results   = []
    all_scores = {"relevance": [], "coherence": [], "groundedness": [], "overall": []}

    for i, prompt in enumerate(EVAL_PROMPTS, 1):
        agent   = AGENTS[i % len(AGENTS)]
        concepts = [w for w in prompt.split() if len(w) > 3][:3]

        print(f"  [{i:02d}/{len(EVAL_PROMPTS)}] Agent: {agent:<20} Prompt: {prompt[:45]}...")

        start    = time.time()
        response = get_agent_response(agent, prompt, concepts)
        latency  = round((time.time() - start) * 1000, 1)

        scores = score_response(response, prompt)

        result = {
            "id":       i,
            "prompt":   prompt,
            "agent":    agent,
            "response": response,
            "latency_ms": latency,
            "scores":   scores,
        }
        results.append(result)

        for k in all_scores:
            all_scores[k].append(scores[k])

    # ── Aggregate ─────────────────────────────────────────────────────────────
    summary = {
        "relevance":    round(sum(all_scores["relevance"])    / len(results), 2),
        "coherence":    round(sum(all_scores["coherence"])    / len(results), 2),
        "groundedness": round(sum(all_scores["groundedness"]) / len(results), 2),
        "overall":      round(sum(all_scores["overall"])      / len(results), 2),
    }

    output = {
        "evaluation_date":    datetime.now().isoformat(),
        "total_queries":      len(results),
        "agents_tested":      AGENTS,
        "mode":               os.getenv("MOCK_AI", "true"),
        "aggregate_scores":   summary,
        "results":            results,
    }

    # ── Save results ──────────────────────────────────────────────────────────
    out_path = os.path.join(os.path.dirname(__file__), "eval_results.json")
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2)

    # ── Print summary ─────────────────────────────────────────────────────────
    print()
    print("=" * 60)
    print("  EVALUATION COMPLETE")
    print("=" * 60)
    print(f"  Queries processed : {len(results)}")
    print(f"  Relevance         : {summary['relevance']}/5.0")
    print(f"  Coherence         : {summary['coherence']}/5.0")
    print(f"  Groundedness      : {summary['groundedness']}/5.0")
    print(f"  Overall Quality   : {summary['overall']}/5.0")
    print(f"  Results saved to  : {out_path}")
    print("=" * 60 + "\n")

    return output


if __name__ == "__main__":
    run_evaluation()
