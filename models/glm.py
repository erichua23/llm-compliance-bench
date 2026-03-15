from .base import BaseModel


class GLMModel(BaseModel):
    @property
    def name(self) -> str:
        return "GLM"
