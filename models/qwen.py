from .base import BaseModel


class QwenModel(BaseModel):
    @property
    def name(self) -> str:
        return "Qwen"
