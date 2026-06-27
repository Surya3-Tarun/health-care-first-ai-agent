"""Context memory agent for healthcare conversations."""

from typing import Dict, List, Optional


class ContextAgent:
    """Read previous conversation context and carry it forward."""

    def process(self, user_input: str, conversation_history: Optional[List[Dict]] = None) -> Dict[str, object]:
        history = conversation_history or []
        recent_messages = [msg.get("content", "") for msg in history[-4:] if isinstance(msg, dict)]
        context = " ".join(filter(None, recent_messages))
        return {
            "context": context,
            "context_available": bool(context),
            "current_input": user_input,
        }
