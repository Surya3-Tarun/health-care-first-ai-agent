"""Validation agent for healthcare-only requests."""

from typing import Dict

from utils.health_utils import HEALTHCARE_ONLY_RESPONSE, is_healthcare_question


class ValidationAgent:
    """Reject requests that are unrelated to healthcare."""

    def process(self, user_input: str) -> Dict[str, object]:
        is_valid, reason = is_healthcare_question(user_input or "")
        if not is_valid:
            return {
                "is_valid": False,
                "reason": reason,
                "response": HEALTHCARE_ONLY_RESPONSE,
            }
        return {"is_valid": True, "reason": reason, "response": None}
