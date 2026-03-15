"""Kimi Code model - requires special User-Agent and uses httpx directly."""

import httpx


class KimiModel:
    """Kimi Code API requires User-Agent: claude-code/0.1.0 and rejects OpenAI SDK default UA."""

    def __init__(self, config: dict):
        self.model_id = config["model_id"]
        self._base_url = config["base_url"].rstrip("/")
        self._api_key = config["api_key"]
        self._timeout = config.get("timeout", 30)
        self._user_agent = config.get("user_agent", "claude-code/0.1.0")

    @property
    def name(self) -> str:
        return "Kimi"

    def chat(self, system: str, user: str) -> str:
        resp = httpx.post(
            f"{self._base_url}/chat/completions",
            headers={
                "Authorization": f"Bearer {self._api_key}",
                "User-Agent": self._user_agent,
                "Content-Type": "application/json",
            },
            json={
                "model": self.model_id,
                "messages": [
                    {"role": "system", "content": system},
                    {"role": "user", "content": user},
                ],
                "temperature": 0.0,
                "max_tokens": 1024,
            },
            timeout=self._timeout,
        )
        resp.raise_for_status()
        data = resp.json()
        return data["choices"][0]["message"].get("content") or ""
