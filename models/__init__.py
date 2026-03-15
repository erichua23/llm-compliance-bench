from .base import BaseModel
from .kimi import KimiModel
from .glm import GLMModel
from .minimax import MiniMaxModel
from .qwen import QwenModel

MODEL_REGISTRY = {
    "kimi": KimiModel,
    "glm": GLMModel,
    "minimax": MiniMaxModel,
    "qwen": QwenModel,
}
