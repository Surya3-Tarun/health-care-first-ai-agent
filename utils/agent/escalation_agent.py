"""Escalation decision agent."""

from typing import Dict


class EscalationAgent:
    """Determine whether the user should seek home care, medical review, or emergency care."""

    def process(self, risk_level: str, user_input: str = "") -> Dict[str, object]:
        risk = (risk_level or "Low").lower()
        text = (user_input or "").lower()
        if risk in {"emergency", "high"} or any(term in text for term in ["chest pain", "difficulty breathing", "unconscious", "seizure", "suicidal"]):
            return {"level": "emergency", "message": "Seek emergency services immediately."}
        if risk == "medium":
            return {"level": "doctor", "message": "Book a medical consultation if symptoms persist or worsen."}
        return {"level": "home-care", "message": "Home care and monitoring are appropriate for now."}
