"""Emergency detection agent."""

from typing import Dict

from utils.emergency_detector import detect_emergency_condition


class EmergencyAgent:
    """Detect urgent cases and stop the workflow early."""

    def process(self, user_input: str) -> Dict[str, object]:
        is_emergency, condition_type, emergency_msg = detect_emergency_condition(user_input or "")
        if is_emergency:
            return {
                "is_emergency": True,
                "condition_type": condition_type,
                "response": emergency_msg,
            }
        return {"is_emergency": False, "condition_type": None, "response": None}
