"""Formatter agent for structured responses."""

from typing import Dict


class FormatterAgent:
    """Format the final answer into a structured AI-agent report."""

    def process(self, workflow: Dict[str, object]) -> str:
        intent = workflow.get("intent", {}).get("intent", "Unknown")
        risk_level = workflow.get("risk", {}).get("risk_level", "Low")
        symptoms = workflow.get("symptoms", {}).get("symptoms", ["General health concern"])
        recommendations = workflow.get("recommendations", {}).get("recommendations", [])
        missing_info = workflow.get("missing_info", {}).get("questions", [])
        escalation = workflow.get("escalation", {}).get("level", "home-care")
        emergency = workflow.get("emergency", {}).get("is_emergency", False)
        reasoning = workflow.get("reasoning", {}).get("summary", "")
        entities = workflow.get("entities", {})
        knowledge = workflow.get("knowledge", {})

        if emergency:
            return """══════════════════════════════════════

🩺 Health Care First AI

══════════════════════════════════════

Patient Intent
- {intent}

Healthcare Validation
- Passed

Conversation Context
- Emergency workflow engaged.

Symptoms Identified
- {symptoms}

Medical Entities
- {entities}

Emergency Screening
- Emergency detected. Seek immediate medical assistance.

Missing Information
- None required for emergency escalation.

Risk Assessment
- Emergency

Reasoning Summary
- {reasoning}

Possible Educational Causes
- Urgent medical evaluation is required.

Recommendations
- Follow emergency guidance immediately.

Lifestyle Advice
- Avoid exertion and stay calm.

Escalation Decision
- Emergency services should be contacted immediately.

Follow-up Questions
- None.

Medical Disclaimer
- Educational guidance only; not a diagnosis.

══════════════════════════════════════
""".format(intent=intent, symptoms=", ".join(symptoms), entities=self._format_entities(entities), reasoning=reasoning)

        return """══════════════════════════════════════

🩺 Health Care First AI

══════════════════════════════════════

Patient Intent
- {intent}

Healthcare Validation
- Passed

Conversation Context
- {context}

Symptoms Identified
- {symptoms}

Medical Entities
- {entities}

Emergency Screening
- No immediate emergency detected.

Missing Information
- {missing_info}

Risk Level
- {risk_level}

Reasoning Summary
- {reasoning}

Possible Educational Causes
- {knowledge}

Recommendations
- {recommendations}

Lifestyle Advice
- Rest, hydration, balanced nutrition, and monitoring symptoms are appropriate general steps.

Escalation Decision
- {escalation}

Follow-up Questions
- {followup}

Medical Disclaimer
- Educational guidance only; not a diagnosis or prescription.

══════════════════════════════════════
""".format(
            intent=intent,
            context=workflow.get("context", {}).get("context", "No previous context"),
            symptoms=", ".join(symptoms),
            entities=self._format_entities(entities),
            missing_info="\n- ".join(missing_info) if missing_info else "- No additional information is required.",
            risk_level=risk_level,
            reasoning=reasoning,
            knowledge=knowledge.get("summary", "Educational health information available.") if isinstance(knowledge, dict) else str(knowledge),
            recommendations="\n- ".join(recommendations) if recommendations else "- Follow general wellness guidance.",
            escalation=escalation,
            followup="\n- ".join(missing_info) if missing_info else "- No additional questions needed.",
        )

    def _format_entities(self, entities: Dict[str, object]) -> str:
        if not entities:
            return "None identified"
        formatted = []
        for key, values in entities.items():
            if values:
                formatted.append(f"{key}: {', '.join(values)}")
        return "; ".join(formatted) if formatted else "None identified"
