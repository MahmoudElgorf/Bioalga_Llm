from pydantic_settings import BaseSettings
from typing import List
import json
import os

class Settings(BaseSettings):
    # OpenAI
    openai_api_key: str
    openai_model: str = "gpt-4o-mini"
    openai_temperature: float = 0.4
    openai_max_tokens: int = 800
    
    # Streaming Settings
    stream_enabled: bool = True  # Enable/disable streaming responses
    stream_chunk_delay: float = 0.01  # Delay between chunks (seconds)
    
    # Server
    app_name: str = "BioAlga AI Assistant"
    app_version: str = "2.0.0"
    debug_mode: bool = False
    host: str = "0.0.0.0"
    port: int = 8000
    
    # CORS
    allowed_origins_str: str = '["*"]'
    
    @property
    def allowed_origins(self) -> List[str]:
        try:
            return json.loads(self.allowed_origins_str)
        except:
            return ["*"]
    
    # Rate Limiting
    rate_limit_enabled: bool = False
    rate_limit_requests: int = 60
    
    class Config:
        env_file = ".env"
        case_sensitive = False
        extra = "ignore"

settings = Settings()