"""Intent classification for healthcare conversations."""

import re
from typing import Dict


class IntentAgent:
    """Classify the user's healthcare intent."""

    def process(self, user_input: str) -> Dict[str, str]:
        text = (user_input or "").strip().lower()
        patterns = [
            (r"symptom|symptoms|pain|fever|cough|headache|nausea|vomiting", "Symptom Query"),
            (r"disease|condition|illness|infection", "Disease Information"),
            (r"medicine|medication|drug|tablet|capsule|prescription", "Medicine Information"),
            (r"fitness|exercise|workout|gym|walk|running|yoga", "Fitness"),
            (r"nutrition|diet|food|vitamin|protein|water|hydration", "Nutrition"),
            (r"mental health|stress|anxiety|depression|sleep", "Mental Health"),
            (r"first aid|injury|burn|bleeding|wound", "First Aid"),
            (r"bmi|body mass index|weight|height", "BMI"),
            (r"lifestyle|healthy living|habits", "Lifestyle"),
            (r"preventive|vaccination|checkup|screening", "Preventive Care"),
            (r"education|awareness|explain|what is", "Health Education"),
        ]

        for pattern, intent in patterns:
            if re.search(pattern, text):
                return {"intent": intent, "confidence": "high"}

        if text:
            return {"intent": "Medical Awareness", "confidence": "medium"}

        return {"intent": "Medical Awareness", "confidence": "low"}
