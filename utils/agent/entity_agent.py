"""Medical entity extraction agent."""

from typing import Dict, List


class EntityAgent:
    """Extract medical entities from user input."""

    def process(self, user_input: str) -> Dict[str, List[str]]:
        text = (user_input or "").lower()
        entities = {
            "diseases": [],
            "symptoms": [],
            "medicines": [],
            "body_organs": [],
            "tests": [],
            "departments": [],
        }

        symptom_keywords = ["fever", "cough", "headache", "pain", "nausea", "vomiting", "fatigue", "dizziness", "rash"]
        disease_keywords = ["diabetes", "hypertension", "asthma", "infection", "flu", "allergy"]
        medicine_keywords = ["medicine", "medication", "tablet", "capsule", "syrup"]
        organ_keywords = ["heart", "lung", "stomach", "kidney", "liver", "brain"]
        test_keywords = ["blood test", "scan", "xray", "mri", "ecg"]
        department_keywords = ["cardiology", "neurology", "dermatology", "psychiatry"]

        for keyword in symptom_keywords:
            if keyword in text:
                entities["symptoms"].append(keyword)
        for keyword in disease_keywords:
            if keyword in text:
                entities["diseases"].append(keyword)
        for keyword in medicine_keywords:
            if keyword in text:
                entities["medicines"].append(keyword)
        for keyword in organ_keywords:
            if keyword in text:
                entities["body_organs"].append(keyword)
        for keyword in test_keywords:
            if keyword in text:
                entities["tests"].append(keyword)
        for keyword in department_keywords:
            if keyword in text:
                entities["departments"].append(keyword)

        return entities
