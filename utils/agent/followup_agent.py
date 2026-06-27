"""Follow-up question agent."""

from typing import Dict, List


class FollowupAgent:
    """Ask clarifying questions when the user information is incomplete."""

    def process(self, user_input: str, symptoms: List[str], risk_level: str) -> Dict[str, object]:
        questions = []
        if not any(symptom in (user_input or "").lower() for symptom in ["fever", "cough", "headache", "pain"]):
            questions.append("What symptoms are you experiencing?")
        if risk_level in ["High Risk", "Emergency"]:
            questions.append("How long have these symptoms been present?")
            questions.append("Do you have any breathing difficulty or chest pain?")
        else:
            questions.append("How long have you been experiencing these symptoms?")
        return {"questions": questions, "needs_followup": bool(questions)}
