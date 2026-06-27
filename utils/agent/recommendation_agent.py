"""Recommendation agent for safe healthcare guidance."""

from typing import Dict


class RecommendationAgent:
    """Generate safe recommendations without prescribing medications or diagnoses."""

    def process(self, risk_level: str, symptoms: list, user_input: str = "") -> Dict[str, object]:
        text = (user_input or "").lower()
        recommendations = []
        if risk_level == "Emergency":
            recommendations.extend([
                "Contact emergency medical services immediately.",
                "Do not delay and seek urgent care.",
            ])
        else:
            recommendations.extend([
                "Get adequate rest and hydration.",
                "Maintain a balanced diet and avoid overexertion.",
                "Monitor symptoms closely.",
            ])
            if any(term in text for term in ["fever", "cold", "cough"]):
                recommendations.append("Consider rest and fluids while monitoring symptoms.")
            if any(term in text for term in ["stress", "anxiety", "sleep"]):
                recommendations.append("Practice relaxation techniques and maintain a regular sleep routine.")

        if risk_level in ["High Risk", "Medium Risk"]:
            recommendations.append("Consult a healthcare professional if symptoms persist or worsen.")

        return {"recommendations": recommendations}
