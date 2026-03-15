"""MiniMax model - strips <think> tags from responses."""

import re
from .base import BaseModel


class MiniMaxModel(BaseModel):
    @property
    def name(self) -> str:
        return "MiniMax"

    def chat(self, system: str, user: str) -> str:
        raw = super().chat(system, user)
        # MiniMax M2.5 wraps reasoning in <think>...</think>, strip it
        return re.sub(r"<think>.*?</think>\s*", "", raw, flags=re.DOTALL).strip()
