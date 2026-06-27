"""Risk assessment agent."""

from typing import Dict


class RiskAgent:
    """Estimate the general risk level without making diagnoses."""

    def process(self, symptoms: list, user_input: str = "") -> Dict[str, str]:
        text = (user_input or " ").lower()
        if any(term in text for term in ["chest pain", "difficulty breathing", "unconscious", "stroke", "severe bleeding", "suicidal"]):
            return {"risk_level": "Emergency", "reason": "Urgent symptoms detected"}
        if any(term in text for term in ["high fever", "severe pain", "persistent cough", "shortness of breath"]):
            return {"risk_level": "High Risk", "reason": "Concerning symptoms present"}
        if any(term in text for term in ["fever", "headache", "cough", "fatigue", "dizziness"]):
            return {"risk_level": "Medium Risk", "reason": "Some symptoms present"}
        return {"risk_level": "Low Risk", "reason": "No urgent indicators detected"}
