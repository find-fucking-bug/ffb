from pydantic_settings import BaseSettings


class Config(BaseSettings):
    OLLAMA_API_URL: str = "http://localhost:11434"

    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Config()
