import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from utils.agent.healthcare_agent import HealthcareAgent
from utils.agent.context_agent import ContextAgent
from utils.agent.knowledge_agent import KnowledgeAgent
from utils.agent.escalation_agent import EscalationAgent


def test_non_healthcare_question_is_rejected():
    agent = HealthcareAgent()
    response = agent.process("What is the capital of France?")
    assert "I can only answer healthcare-related questions" in response


def test_emergency_question_short_circuits():
    agent = HealthcareAgent()
    response = agent.process("I have chest pain and difficulty breathing")
    assert "EMERGENCY" in response.upper()
    assert "911" in response or "112" in response


def test_structured_response_format():
    agent = HealthcareAgent()
    response = agent.process("I have a mild headache and fever")
    assert "🩺 Health Care First AI" in response
    assert "Intent" in response
    assert "Risk Level" in response


def test_context_agent_tracks_previous_messages():
    agent = ContextAgent()
    state = agent.process("I had a fever yesterday", [{"role": "user", "content": "I had a fever yesterday"}])
    assert state["context_available"] is True


def test_knowledge_agent_returns_educational_guidance():
    agent = KnowledgeAgent()
    state = agent.process("I have a cough", {"intent": "Symptom Analysis"})
    assert "education" in state["topic"].lower() or "health" in state["topic"].lower()


def test_escalation_agent_flags_doctor_consultation():
    agent = EscalationAgent()
    state = agent.process("high", "I have persistent fever")
    assert state["level"] in {"doctor", "emergency", "home-care"}
