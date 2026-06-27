"""Main orchestrator for the healthcare agent pipeline."""

from typing import Dict

from utils.agent.context_agent import ContextAgent
from utils.agent.emergency_agent import EmergencyAgent
from utils.agent.entity_agent import EntityAgent
from utils.agent.escalation_agent import EscalationAgent
from utils.agent.formatter_agent import FormatterAgent
from utils.agent.intent_agent import IntentAgent
from utils.agent.knowledge_agent import KnowledgeAgent
from utils.agent.memory_agent import MemoryAgent
from utils.agent.missing_info_agent import MissingInfoAgent
from utils.agent.reasoning_agent import ReasoningAgent
from utils.agent.recommendation_agent import RecommendationAgent
from utils.agent.risk_agent import RiskAgent
from utils.agent.symptom_agent import SymptomAgent
from utils.agent.validation_agent import ValidationAgent
from utils.agent.workflow import AgentWorkflow
from utils.health_utils import HEALTHCARE_ONLY_RESPONSE


class HealthcareAgent:
    """Coordinate the multi-step healthcare agent workflow."""

    def __init__(self) -> None:
        self.intent_agent = IntentAgent()
        self.validation_agent = ValidationAgent()
        self.context_agent = ContextAgent()
        self.memory_agent = MemoryAgent()
        self.emergency_agent = EmergencyAgent()
        self.symptom_agent = SymptomAgent()
        self.entity_agent = EntityAgent()
        self.missing_info_agent = MissingInfoAgent()
        self.risk_agent = RiskAgent()
        self.knowledge_agent = KnowledgeAgent()
        self.reasoning_agent = ReasoningAgent()
        self.recommendation_agent = RecommendationAgent()
        self.escalation_agent = EscalationAgent()
        self.formatter_agent = FormatterAgent()

    def process(self, user_input: str) -> str:
        workflow = AgentWorkflow(user_input=user_input)

        workflow.intent = self.intent_agent.process(user_input)

        validation = self.validation_agent.process(user_input)
        workflow.validation = validation
        if not validation.get("is_valid", False):
            return validation.get("response", HEALTHCARE_ONLY_RESPONSE)

        context = self.context_agent.process(user_input, [])
        workflow.context = context

        emergency = self.emergency_agent.process(user_input)
        workflow.emergency = emergency
        if emergency.get("is_emergency", False):
            return emergency.get("response", "")

        symptoms = self.symptom_agent.process(user_input)
        workflow.symptoms = symptoms

        entities = self.entity_agent.process(user_input)
        workflow.entities = entities

        missing_info = self.missing_info_agent.process(user_input, symptoms.get("symptoms", []), "Low")
        workflow.missing_info = missing_info

        risk = self.risk_agent.process(symptoms.get("symptoms", []), user_input)
        workflow.risk = risk

        knowledge = self.knowledge_agent.process(user_input, workflow.intent)
        workflow.knowledge = knowledge

        reasoning = self.reasoning_agent.process(workflow.to_dict())
        workflow.reasoning = reasoning

        recommendations = self.recommendation_agent.process(risk.get("risk_level", "Low"), symptoms.get("symptoms", []), user_input)
        workflow.recommendations = recommendations

        escalation = self.escalation_agent.process(risk.get("risk_level", "Low"), user_input)
        workflow.escalation = escalation

        memory = self.memory_agent.process(user_input, "")
        workflow.memory = memory

        workflow.final_response = self.formatter_agent.process(workflow.to_dict())
        return workflow.final_response
