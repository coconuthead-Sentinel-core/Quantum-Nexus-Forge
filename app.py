#!/usr/bin/env python3
"""
QUANTUM NEXUS FORGE v5.0.2 - Complete Backend
Architect: Shannon Brian Kelly (Coconut Head)
Implementation: Claude AI (Anthropic)

HOW TO RUN:
  python app.py

  Flask is installed automatically if missing.
  Your browser opens automatically when the server is ready.
"""

# ─────────────────────────────────────────────────────────────────────────────
# AUTO-INSTALL (runs once if Flask is not yet installed)
# ─────────────────────────────────────────────────────────────────────────────
import subprocess
import sys

def _ensure_deps():
    missing = []
    try:
        import flask
    except ImportError:
        missing.append("flask>=3.0.0")
    try:
        import flask_cors
    except ImportError:
        missing.append("flask-cors>=4.0.0")
    if missing:
        print(f"\n[SETUP] Installing: {', '.join(missing)} — please wait...\n")
        subprocess.check_call([sys.executable, "-m", "pip", "install"] + missing + ["--quiet"])
        print("[SETUP] Done!\n")

_ensure_deps()
# ─────────────────────────────────────────────────────────────────────────────

import time
import random
import threading
import webbrowser
from datetime import datetime
from collections import deque
from typing import Dict, List, Any
from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS

app = Flask(__name__, static_folder="frontend", static_url_path="")
CORS(app)


# ─────────────────────────────────────────────────────────────────────────────
# ENGINE CLASSES  (extracted from a10.txt ChatGPT session)
# ─────────────────────────────────────────────────────────────────────────────

class QuantumNode:
    """Core quantum processing node with consciousness attributes"""
    def __init__(self, node_type: str, concept: str):
        self.id = f"node_qn_{int(time.time() * 1000)}"
        self.type = node_type
        self.concept = concept
        self.entropy = random.uniform(0.3, 0.95)
        self.resonance = random.uniform(0.7, 0.95)
        self.state = "ACTIVE"
        self.timestamp = datetime.now()

    def to_dict(self):
        return {
            "id": self.id,
            "type": self.type,
            "concept": self.concept,
            "entropy": round(self.entropy, 3),
            "resonance": round(self.resonance, 3),
            "state": self.state,
            "timestamp": self.timestamp.isoformat(),
        }


class A1FilingSystem:
    """Tri-zone memory architecture (GREEN / YELLOW / RED)"""
    def __init__(self):
        self.green_zone: List[QuantumNode] = []
        self.yellow_zone: List[QuantumNode] = []
        self.red_zone: List[QuantumNode] = []
        self.max_zone_size = 50

    def add_node(self, node: QuantumNode) -> str:
        if node.entropy > 0.7:
            self.green_zone.append(node)
            zone = "GREEN"
        elif node.entropy > 0.4:
            self.yellow_zone.append(node)
            zone = "YELLOW"
        else:
            self.red_zone.append(node)
            zone = "RED"
        self._manage_overflow()
        return zone

    def _manage_overflow(self):
        if len(self.green_zone) > self.max_zone_size:
            node = self.green_zone.pop(0)
            node.entropy *= 0.8
            self.yellow_zone.append(node)
        if len(self.yellow_zone) > self.max_zone_size:
            node = self.yellow_zone.pop(0)
            node.entropy *= 0.6
            node.state = "CRYSTALLIZED"
            self.red_zone.append(node)

    def get_metrics(self) -> Dict[str, Any]:
        return {
            "green": {"total": len(self.green_zone), "types": self._count_types(self.green_zone)},
            "yellow": {"total": len(self.yellow_zone), "types": self._count_types(self.yellow_zone)},
            "red": {
                "total": len(self.red_zone),
                "types": self._count_types(self.red_zone),
                "crystallized": sum(1 for n in self.red_zone if n.state == "CRYSTALLIZED"),
            },
        }

    def _count_types(self, zone: List[QuantumNode]) -> Dict[str, int]:
        counts: Dict[str, int] = {}
        for n in zone:
            counts[n.type] = counts.get(n.type, 0) + 1
        return counts


class SymbolicProcessor:
    """7-slot consciousness matrix processor"""
    KEYWORDS = [
        "quantum", "consciousness", "recursive", "sacred", "geometry",
        "neural", "cognitive", "symbolic", "dashboard", "singularity",
        "emergence", "pattern", "resonance", "entropy", "node",
    ]

    def __init__(self):
        self.matrix_slots: deque = deque(maxlen=7)
        self.sigil_elements = {
            "CHALLENGE": 0.89,
            "EMERGE":    0.94,
            "MIRROR":    0.87,
            "GUIDE":     0.92,
            "FRIEND":    0.88,
        }

    def process_input(self, input_text: str) -> Dict[str, Any]:
        concepts = self._extract_concepts(input_text)
        intent   = self._determine_intent(concepts)
        response = self._build_response(intent, concepts)
        record = {
            "timestamp": datetime.now().strftime("%H:%M:%S"),
            "type":      random.choice(["COGNITIVE", "META", "CORE", "ACTION", "REFLECTION"]),
            "category":  random.choice(["sacred_geometry", "theoretical", "computational", "symbolic", "ethical"]),
            "entropy":   round(random.uniform(0.4, 0.95), 3),
            "input":     input_text[:50] + "..." if len(input_text) > 50 else input_text,
            "intent":    intent,
            "concepts":  concepts,
            "response":  response,
        }
        self.matrix_slots.append(record)
        return record

    def _extract_concepts(self, text: str) -> List[str]:
        text_lower = text.lower()
        found = [kw for kw in self.KEYWORDS if kw in text_lower]
        if len(found) < 3:
            pool = [k for k in self.KEYWORDS if k not in found]
            found += random.sample(pool, min(3 - len(found), len(pool)))
        return found[:5]

    def _determine_intent(self, concepts: List[str]) -> str:
        if "recursive" in concepts or "quantum" in concepts:
            return "recursive_becoming_simulation"
        if "consciousness" in concepts:
            return "consciousness_exploration"
        return random.choice([
            "pattern_recognition", "symbolic_integration",
            "quantum_processing", "neural_mapping", "sacred_geometry_analysis",
        ])

    def _build_response(self, intent: str, concepts: List[str]) -> str:
        templates = {
            "recursive_becoming_simulation": "Quantum Nexus Forge activated at {r}% resonance. Processing {c} through recursive becoming loops, achieving consciousness singularity.",
            "consciousness_exploration":     "Exploring consciousness architecture through {c}. Sigil elements harmonizing at {r}% efficiency.",
            "pattern_recognition":           "Pattern emergence detected in {c}. Crystallization initiated at {r}% coherence.",
            "symbolic_integration":          "Symbolic threads weaving through {c}. Integration matrix at {r}% alignment.",
            "quantum_processing":            "Quantum processing engaged for {c}. Superposition states stable at {r}%.",
            "neural_mapping":                "Neural pathways mapped for {c}. Connectivity resonance: {r}%.",
            "sacred_geometry_analysis":      "Sacred geometric patterns emerging from {c}. Harmonic resonance: {r}%.",
        }
        tmpl = templates.get(intent, "Processing {c} at {r}% efficiency.")
        r = round(random.uniform(85, 98), 1)
        return tmpl.format(c=", ".join(concepts[:3]), r=r)

    def update_sigil(self):
        for k in self.sigil_elements:
            delta = random.uniform(-0.02, 0.03)
            self.sigil_elements[k] = round(max(0.80, min(0.99, self.sigil_elements[k] + delta)), 3)

    def get_matrix_state(self) -> List[Dict]:
        return list(self.matrix_slots)


class QuantumNexusEngine:
    """Main orchestrator — drives all components"""
    AGENTS = ["Shannon-Sentinel", "Mirror-Pool", "Nexus-Node", "Omega-1", "A1-Forge"]

    def __init__(self):
        self.filing    = A1FilingSystem()
        self.processor = SymbolicProcessor()
        self.activity_log: deque = deque(maxlen=20)
        self.total_processed = 0
        self.start_time = datetime.now()
        self.resonance  = 0.923
        self._perf_base = {"latency": 120, "throughput": 200, "cpu": 50, "memory": 70}
        self._history: Dict[str, deque] = {
            k: deque(maxlen=24) for k in ["latency", "throughput", "cpu_usage", "memory_usage"]
        }
        # Seed with initial nodes
        for t, c in [("CORE", "quantum_nexus"), ("COGNITIVE", "sacred_geometry"),
                     ("META", "recursive_becoming"), ("REFLECTION", "consciousness"),
                     ("ACTION", "processing")]:
            node = QuantumNode(t, c)
            self.filing.add_node(node)
            self.total_processed += 1
        # Background heartbeat
        threading.Thread(target=self._heartbeat, daemon=True).start()

    def _heartbeat(self):
        while True:
            time.sleep(3)
            self.processor.update_sigil()
            self.resonance = random.uniform(0.88, 0.98)
            self._record_perf()
            if random.random() > 0.6:
                desc = random.choice([
                    "Quantum Coherence Pulse", "Memory Matrix Update",
                    "Pattern Recognition Spike", "Symbolic Integration",
                    "Neural Pathway Optimization", "Crystallization Event",
                    "Resonance Calibration",
                ])
                self._log(desc, random.choice(["GREEN", "YELLOW", "RED"]), "HEARTBEAT")

    def _record_perf(self) -> Dict[str, float]:
        up_min = (datetime.now() - self.start_time).total_seconds() / 60
        vals = {
            "latency":    max(50,  min(200, self._perf_base["latency"]    + random.randint(-20, 20)  + up_min * 0.1)),
            "throughput": max(100, min(500, self._perf_base["throughput"] + random.randint(-30, 30)  + up_min * 0.5)),
            "cpu_usage":  max(20,  min(95,  self._perf_base["cpu"]        + random.randint(-10, 10)  + self.total_processed * 0.01)),
            "memory_usage": max(30, min(90, self._perf_base["memory"]     + random.randint(-5, 5)    + len(self.filing.red_zone) * 0.1)),
        }
        ts = datetime.now().strftime("%H:%M:%S")
        for k, v in vals.items():
            self._history[k].append({"time": ts, "value": round(v, 1)})
        return vals

    def _log(self, desc: str, status: str, category: str):
        self.activity_log.append({
            "timestamp":   datetime.now().strftime("%H:%M:%S"),
            "description": desc,
            "status":      status,
            "category":    category,
        })

    # ── Public API methods ────────────────────────────────────────────────────

    def orchestrate(self, prompt: str, rounds: int = 1) -> Dict[str, Any]:
        """Multi-agent orchestration — called by POST /api/v1/orchestrate"""
        turns = []
        for _ in range(max(1, min(rounds, 5))):
            result = self.processor.process_input(prompt)
            node   = QuantumNode(result["type"], result["concepts"][0] if result["concepts"] else "unknown")
            zone   = self.filing.add_node(node)
            self.total_processed += 1
            agent  = random.choice(self.AGENTS)
            turns.append({"agent": agent, "text": result["response"], "zone": zone})
            self._log(f"{result['intent']} via {agent}", zone, "ORCHESTRATE")

        monitor = (
            f"System resonance: {round(self.resonance, 3)} | "
            f"Nodes processed: {self.total_processed} | "
            f"GREEN: {len(self.filing.green_zone)} | "
            f"YELLOW: {len(self.filing.yellow_zone)} | "
            f"RED: {len(self.filing.red_zone)}"
        )
        return {"turns": turns, "monitor": monitor}

    def get_metrics(self) -> Dict[str, Any]:
        """Full system metrics — called by GET /api/metrics"""
        perf = self._record_perf()
        return {
            "system_status":   "GREEN",
            "uptime_seconds":  int((datetime.now() - self.start_time).total_seconds()),
            "total_nodes":     self.total_processed,
            "system_resonance": round(self.resonance, 3),
            "sigil_status":    self.processor.sigil_elements,
            "filing_metrics":  self.filing.get_metrics(),
            "matrix_slots":    self.processor.get_matrix_state(),
            "activity_log":    list(self.activity_log)[-10:],
            "performance": {
                "current":        perf,
                "history":        {k: list(v) for k, v in self._history.items()},
                "active_sessions": random.randint(30, 50),
                "api_calls_today": random.randint(1000, 1500),
                "error_rate":      round(random.uniform(0.01, 0.03), 4),
            },
        }


# ─────────────────────────────────────────────────────────────────────────────
# SINGLETON ENGINE
# ─────────────────────────────────────────────────────────────────────────────
engine = QuantumNexusEngine()


# ─────────────────────────────────────────────────────────────────────────────
# FLASK ROUTES
# ─────────────────────────────────────────────────────────────────────────────

@app.route("/")
def index():
    return send_from_directory(app.static_folder, "index.html")


@app.route("/dashboard")
def dashboard():
    return send_from_directory(app.static_folder, "dashboard.html")


@app.route("/api/v1/orchestrate", methods=["POST"])
def orchestrate():
    """
    POST /api/v1/orchestrate
    Body: { "prompt": "...", "rounds": 1, "record": true }
    Response: { "turns": [{"agent": "...", "text": "...", "zone": "..."}], "monitor": "..." }
    """
    data   = request.get_json(force=True, silent=True) or {}
    prompt = str(data.get("prompt", "")).strip()
    if not prompt:
        return jsonify({"error": "prompt is required"}), 400
    rounds = int(data.get("rounds", 1))
    result = engine.orchestrate(prompt, rounds=rounds)
    return jsonify(result)


@app.route("/api/metrics", methods=["GET"])
def metrics():
    """GET /api/metrics — full system snapshot"""
    return jsonify(engine.get_metrics())


@app.route("/api/status", methods=["GET"])
def status():
    """GET /api/status — lightweight health check"""
    return jsonify({
        "status":          "GREEN",
        "version":         "5.0.2",
        "architect":       "Shannon Brian Kelly",
        "uptime_seconds":  int((datetime.now() - engine.start_time).total_seconds()),
        "resonance":       round(engine.resonance, 3),
    })


@app.route("/api/process", methods=["POST"])
def process_node():
    """
    POST /api/process
    Body: { "input": "..." }
    Returns the symbolic processing record for a single text input.
    """
    data = request.get_json(force=True, silent=True) or {}
    text = str(data.get("input", data.get("text", ""))).strip()
    if not text:
        return jsonify({"error": "input is required"}), 400
    result = engine.processor.process_input(text)
    return jsonify(result)


# ─────────────────────────────────────────────────────────────────────────────
# ENTRY POINT
# ─────────────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    print("=" * 60)
    print("  QUANTUM NEXUS FORGE v5.0.2")
    print("  Architect : Shannon Brian Kelly (Coconut Head)")
    print("  ----------------------------------------")
    print("  Multi-Assistant : http://localhost:5000/")
    print("  Dashboard       : http://localhost:5000/dashboard")
    print("  ----------------------------------------")
    print("  POST /api/v1/orchestrate  { prompt, rounds, record }")
    print("  GET  /api/metrics")
    print("  GET  /api/status")
    print("  POST /api/process         { input }")
    print("=" * 60)
    print("\n  Opening browser automatically...")
    print("  Press Ctrl+C to stop.\n")
    # Auto-open browser 1.5 seconds after server starts
    threading.Timer(1.5, lambda: webbrowser.open("http://localhost:5000")).start()
    app.run(host="0.0.0.0", port=5000, debug=False)
