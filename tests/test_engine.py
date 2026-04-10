"""
Quantum Nexus Forge — Unit Tests
=================================
Architect: Shannon Bryan Kelly
Implementation: Claude AI (Anthropic)
"""

import os
import sys
import pytest

os.environ["MOCK_AI"] = "true"
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from azure_adapter import get_agent_response, get_mode, AGENTS


# ── Azure adapter tests ───────────────────────────────────────────────────────

class TestAzureAdapter:

    def test_mock_mode_active(self):
        """System should be in mock mode during tests."""
        assert get_mode() == "mock"

    def test_all_agents_return_responses(self):
        """Every agent must return a non-empty string."""
        for agent in AGENTS:
            resp = get_agent_response(agent, "test quantum nexus activation", ["quantum", "nexus"])
            assert isinstance(resp, str), f"{agent} did not return a string"
            assert len(resp) > 10,        f"{agent} returned too-short response: '{resp}'"

    def test_response_does_not_crash_on_empty_concepts(self):
        """Agents must handle empty concept lists gracefully."""
        resp = get_agent_response("Shannon-Sentinel", "hello", [])
        assert isinstance(resp, str)

    def test_response_does_not_crash_on_long_prompt(self):
        """Agents must handle very long prompts without error."""
        long_prompt = "quantum nexus " * 100
        resp = get_agent_response("Omega-1", long_prompt, ["quantum"])
        assert isinstance(resp, str)

    def test_unknown_agent_does_not_crash(self):
        """Unknown agent name should fall back gracefully."""
        resp = get_agent_response("Unknown-Agent", "test", ["test"])
        assert isinstance(resp, str)


# ── Engine class tests ────────────────────────────────────────────────────────

class TestQuantumNexusEngine:

    def setup_method(self):
        """Import engine fresh for each test."""
        from app import engine
        self.engine = engine

    def test_engine_initializes(self):
        """Engine should initialize without errors."""
        assert self.engine is not None

    def test_orchestrate_returns_turns(self):
        """Orchestration must return turns list."""
        result = self.engine.orchestrate("activate quantum nexus", rounds=1)
        assert "turns" in result
        assert isinstance(result["turns"], list)
        assert len(result["turns"]) > 0

    def test_turn_has_required_fields(self):
        """Each turn must have agent, text, zone fields."""
        result = self.engine.orchestrate("test prompt", rounds=1)
        for turn in result["turns"]:
            assert "agent" in turn,  f"Missing 'agent' field in turn: {turn}"
            assert "text"  in turn,  f"Missing 'text' field in turn: {turn}"
            assert "zone"  in turn,  f"Missing 'zone' field in turn: {turn}"

    def test_monitor_string_format(self):
        """Monitor string must contain system resonance."""
        result = self.engine.orchestrate("pattern recognition test", rounds=1)
        assert "monitor" in result
        assert "System resonance" in result["monitor"]

    def test_metrics_returns_dict(self):
        """Metrics endpoint must return a complete dictionary."""
        metrics = self.engine.get_metrics()
        assert isinstance(metrics, dict)
        assert "system_resonance" in metrics
        assert "filing_metrics"   in metrics
        assert "activity_log"     in metrics

    def test_zone_values_are_valid(self):
        """Zones in turns must be GREEN, YELLOW, or RED."""
        result = self.engine.orchestrate("zone validation test", rounds=1)
        valid_zones = {"GREEN", "YELLOW", "RED"}
        for turn in result["turns"]:
            assert turn["zone"] in valid_zones, f"Invalid zone: {turn['zone']}"


# ── A1 Filing System tests ────────────────────────────────────────────────────

class TestA1FilingSystem:

    def setup_method(self):
        from app import A1FilingSystem, QuantumNode
        self.filing = A1FilingSystem()
        self.QuantumNode = QuantumNode

    def test_high_entropy_goes_green(self):
        node = self.QuantumNode("CORE", "quantum")
        node.entropy = 0.9
        zone = self.filing.add_node(node)
        assert zone == "GREEN"

    def test_mid_entropy_goes_yellow(self):
        node = self.QuantumNode("CORE", "pattern")
        node.entropy = 0.5
        zone = self.filing.add_node(node)
        assert zone == "YELLOW"

    def test_low_entropy_goes_red(self):
        node = self.QuantumNode("CORE", "crystallized")
        node.entropy = 0.2
        zone = self.filing.add_node(node)
        assert zone == "RED"

    def test_metrics_returns_zone_counts(self):
        metrics = self.filing.get_metrics()
        assert "green"  in metrics
        assert "yellow" in metrics
        assert "red"    in metrics


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
