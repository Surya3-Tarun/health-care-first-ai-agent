"""Missing information agent for follow-up questions."""

from typing import Dict, List


class MissingInfoAgent:
    """Detect missing health details before recommendations."""

    def process(self, user_input: str, symptoms: List[str], risk_level: str) -> Dict[str, object]:
        text = (user_input or "").lower()
        questions = []
        if not symptoms or len(symptoms) == 0:
            questions.append("What symptoms are you experiencing?")
        if risk_level in ["High", "Emergency"]:
            questions.append("How long have the symptoms been present?")
        if "fever" in text and "temperature" not in text:
            questions.append("What is your temperature?")
        if "breath" in text and "difficulty" not in text:
            questions.append("Do you have breathing difficulty?")
        return {"missing_information": bool(questions), "questions": questions}
