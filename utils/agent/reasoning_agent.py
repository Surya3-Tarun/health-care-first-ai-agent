"""Reasoning agent that evaluates all prior agent outputs before forming conclusions."""

from typing import Dict, List


class ReasoningAgent:
    """Perform internal reasoning over the collected evidence."""

    def process(self, workflow: Dict[str, object]) -> Dict[str, object]:
        risk_level = workflow.get("risk", {}).get("risk_level", "Low")
        emergency = workflow.get("emergency", {}).get("is_emergency", False)
        missing_info = workflow.get("missing_info", {}).get("missing_information", False)
        symptoms = workflow.get("symptoms", {}).get("symptoms", [])
        intent = workflow.get("intent", {}).get("intent", "Medical Awareness")

        summary_parts = [
            f"Intent classified as {intent}.",
            f"Identified symptoms: {', '.join(symptoms) if symptoms else 'general concern'}.",
        ]
        if emergency:
            summary_parts.append("Emergency screening triggered an urgent pathway.")
        elif missing_info:
            summary_parts.append("Additional information is needed before final recommendations.")
        else:
            summary_parts.append("Sufficient context is available for safe educational guidance.")
        if risk_level in ["High", "Emergency"]:
            summary_parts.append("The risk level suggests closer medical oversight.")

        return {"summary": " ".join(summary_parts)}
