"""Symptom extraction agent."""

import re
from typing import Dict, List


class SymptomAgent:
    """Extract symptoms from the user's message."""

    def process(self, user_input: str) -> Dict[str, object]:
        text = (user_input or "").lower()
        symptoms = []
        symptom_keywords = [
            "fever", "cough", "cold", "headache", "vomiting", "nausea", "fatigue",
            "body pain", "dizziness", "rash", "chest pain", "stomach pain",
            "shortness of breath", "back pain", "joint pain", "diarrhea",
            "constipation", "sore throat", "breathing difficulty"
        ]

        for keyword in symptom_keywords:
            if keyword in text:
                symptoms.append(keyword)

        if not symptoms:
            symptoms = ["general health concern"]

        return {"symptoms": symptoms, "count": len(symptoms)}
