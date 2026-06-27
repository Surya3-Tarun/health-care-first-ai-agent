"""Workflow data structures for the healthcare agent pipeline."""

from dataclasses import dataclass, field
from typing import Any, Dict, Optional


@dataclass
class AgentWorkflow:
    """Simple container for the agent pipeline state."""

    user_input: str = ""
    intent: Optional[Dict[str, Any]] = None
    validation: Optional[Dict[str, Any]] = None
    emergency: Optional[Dict[str, Any]] = None
    symptoms: Optional[Dict[str, Any]] = None
    risk: Optional[Dict[str, Any]] = None
    medical_info: Optional[Dict[str, Any]] = None
    followup: Optional[Dict[str, Any]] = None
    recommendations: Optional[Dict[str, Any]] = None
    memory: Optional[Dict[str, Any]] = None
    final_response: str = ""
    context: Optional[Dict[str, Any]] = None
    entities: Optional[Dict[str, Any]] = None
    knowledge: Optional[Dict[str, Any]] = None
    reasoning: Optional[Dict[str, Any]] = None
    escalation: Optional[Dict[str, Any]] = None
    missing_info: Optional[Dict[str, Any]] = None
    metadata: Dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "user_input": self.user_input,
            "intent": self.intent,
            "validation": self.validation,
            "emergency": self.emergency,
            "symptoms": self.symptoms,
            "risk": self.risk,
            "medical_info": self.medical_info,
            "followup": self.followup,
            "recommendations": self.recommendations,
            "memory": self.memory,
            "context": self.context,
            "entities": self.entities,
            "knowledge": self.knowledge,
            "reasoning": self.reasoning,
            "escalation": self.escalation,
            "missing_info": self.missing_info,
            "final_response": self.final_response,
            "metadata": self.metadata,
        }
