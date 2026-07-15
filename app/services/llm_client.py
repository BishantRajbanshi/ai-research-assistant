from abc import ABC, abstractmethod

import httpx

from app.core.config import settings

class LLMClient(ABC):
    @abstractmethod
    def generate(self, prompt: str) -> str:
        """Generate a response from the LLM given a prompt."""
        pass

class OllamaClient(LLMClient):
    async def generate(self , prompt: str) -> str:
        async with httpx.AsyncClient(timeout=120) as client:
            resp = await client.post(
                f"{settings.ollama_base_url}/api/generate",
                json={
                    "model": settings.ollama_model,
                    "prompt": prompt,
                    "stream": False
                },
            )
            resp.raise_for_status()
            data = resp.json()
            return data["response"]
        
class OpenAIClient(LLMClient):
    async def generate(self , prompt: str) -> str:
        from openai import AsyncOpenAI

        client = AsyncOpenAI(api_key=settings.openai_api_key)
        response = await client.chat.completions.create(
            model=settings.openai_model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2,
        )
        return response.choices[0].message.content.strip()
    
def get_llm_client() -> LLMClient:
    provider = settings.llm_provider.lower()
    if provider == "ollama":
        return OllamaClient()
    elif provider == "openai":
        return OpenAIClient()
    else:
        raise ValueError(f"Unsupported LLM provider: {settings.llm_provider}")