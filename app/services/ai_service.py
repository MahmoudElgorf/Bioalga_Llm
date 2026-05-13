from openai import OpenAI, OpenAIError
from app.core.config import settings
from typing import List, Dict, Any, Optional
import logging

logger = logging.getLogger(__name__)

class AIService:
    """Service for OpenAI API interaction"""
    
    def __init__(self):
        self.client = OpenAI(api_key=settings.openai_api_key)
        self.model = settings.openai_model
        self.temperature = settings.openai_temperature
        self.max_tokens = settings.openai_max_tokens
    
    def chat_with_messages(self, messages: List[Dict[str, str]]) -> Dict[str, Any]:
        """Non-streaming: Send messages to OpenAI and get response"""
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=self.temperature,
                max_tokens=self.max_tokens,
                top_p=0.9
            )
            
            return {
                "response": response.choices[0].message.content,
                "tokens_used": response.usage.total_tokens if response.usage else 0,
                "confidence_boost": None
            }
            
        except OpenAIError as e:
            logger.error(f"OpenAI API error: {str(e)}")
            raise Exception(f"AI service error: {str(e)}")
    
    async def chat_with_stream(self, messages: List[Dict[str, str]]):
        """Streaming: Send messages to OpenAI and return stream"""
        try:
            stream = await self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=self.temperature,
                max_tokens=self.max_tokens,
                stream=True,
            )
            return stream
            
        except OpenAIError as e:
            logger.error(f"OpenAI API stream error: {str(e)}")
            raise Exception(f"AI service stream error: {str(e)}")
    
    def enhance_classification_text(self, algae_type: str, raw_text: str) -> str:
        """Enhance raw classification text using AI"""
        prompt = f"""You are an algae classification expert. 

Algae type identified: {algae_type}

Raw classification data: {raw_text}

Please provide a clear, structured, and scientifically accurate summary including:
1. Scientific name and classification
2. Toxicity status and warnings if applicable
3. Key characteristics
4. Commercial relevance

Keep response detailed but concise."""

        messages = [
            {"role": "system", "content": "You are an algae taxonomy and toxicity expert. Provide accurate, detailed responses."},
            {"role": "user", "content": prompt}
        ]
        
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=0.3,
                max_tokens=600
            )
            return response.choices[0].message.content
        except Exception as e:
            logger.error(f"Enhancement error: {str(e)}")
            return raw_text