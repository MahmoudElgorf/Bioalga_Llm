from pydantic_settings import BaseSettings
from typing import List, Optional
import json
import os

class Settings(BaseSettings):
    # OpenAI Configuration
    openai_api_key: str
    openai_model: str = "gpt-4o-mini"
    openai_temperature: float = 0.4
    openai_max_tokens: int = 500
    
    # Server Configuration
    app_name: str = "BioAlga AI Assistant"
    app_version: str = "2.0.0"
    debug_mode: bool = False
    host: str = "0.0.0.0"
    port: int = 8000
    
    # CORS Configuration
    allowed_origins_str: str = '["*"]'
    
    @property
    def allowed_origins(self) -> List[str]:
        """Convert string to list"""
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
        extra = "ignore"  # هذا يسمح بوجود حقول إضافية في .env بدون مشكلة

settings = Settings()