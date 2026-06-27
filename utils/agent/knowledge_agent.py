"""Knowledge agent for educational healthcare information."""

from typing import Dict


class KnowledgeAgent:
    """Provide educational healthcare knowledge without diagnosing or prescribing."""

    def process(self, user_input: str, intent_data: Dict[str, object]) -> Dict[str, object]:
        text = (user_input or "").lower()
        topic = intent_data.get("intent", "Medical Awareness")
        if "fever" in text or "cough" in text:
            return {
                "topic": "Educational Health Information",
                "summary": "Common respiratory symptoms may be linked to infections, allergies, or environmental factors. Rest, hydration, and monitoring are sensible general steps.",
            }
        if "stress" in text or "anxiety" in text:
            return {
                "topic": "Mental Health Education",
                "summary": "Stress and anxiety can affect wellness, sleep, and daily functioning. Lifestyle habits and support can be helpful.",
            }
        return {
            "topic": f"{topic} Education",
            "summary": "I can provide safe educational information about symptoms, prevention, wellness, nutrition, and healthy habits.",
        }
