"""Conversation memory agent."""

from typing import Dict, List


class MemoryAgent:
    """Maintain lightweight healthcare conversation context."""

    def __init__(self):
        self.history: List[Dict[str, str]] = []

    def process(self, user_input: str, response: str) -> Dict[str, object]:
        self.history.append({"user": user_input, "response": response})
        return {
            "memory_summary": self.history[-3:],
            "context_available": len(self.history) > 0,
        }
