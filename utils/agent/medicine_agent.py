"""Medical knowledge agent for safe educational guidance."""

from typing import Dict


class MedicineAgent:
    """Provide safe educational medical information."""

    def process(self, user_input: str, intent: str = "") -> Dict[str, object]:
        text = (user_input or "").lower()
        if "medicine" in text or "medication" in text or "drug" in text:
            return {
                "topic": "Medicine Information",
                "guidance": "I can provide general information about medicines, their common uses, and side effects, but I cannot prescribe dosages or recommend treatments.",
            }
        return {
            "topic": "General Health Education",
            "guidance": "I can provide educational information about symptoms, wellness, prevention, and healthy habits.",
        }
