"""Base model interface - all providers use OpenAI-compatible API."""

import httpx
from openai import OpenAI


class BaseModel:
    """All tested models expose OpenAI-compatible chat/completions."""

    def __init__(self, config: dict):
        self.model_id = config["model_id"]
        self._config = config
        http_client = None
        if config.get("user_agent"):
            http_client = httpx.Client(
                headers={"User-Agent": config["user_agent"]},
            )
        self.client = OpenAI(
            base_url=config["base_url"],
            api_key=config["api_key"],
            timeout=config.get("timeout", 30),
            http_client=http_client,
        )

    @property
    def name(self) -> str:
        return self._config.get("display_name") or self.__class__.__name__

    def chat(self, system: str, user: str) -> str:
        resp = self.client.chat.completions.create(
            model=self.model_id,
            messages=[
                {"role": "system", "content": system},
                {"role": "user", "content": user},
            ],
            temperature=0.0,
            max_tokens=1024,
        )
        return resp.choices[0].message.content or ""
