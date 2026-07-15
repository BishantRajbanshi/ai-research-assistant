from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    llm_provider: str = "ollama"
    ollama_base_url: str = "http://localhost:11434"
    ollama_model: str = "llama2"

    openai_api_key: str = ""
    openai_model: str = "gpt-4"

    docs_dir: str = "docs"
    top_k: int = 2

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()