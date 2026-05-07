from pydantic import BaseModel, Field, field_validator
from typing import Optional, List, Dict, Any
from datetime import datetime

class ChatRequest(BaseModel):
    """Chat request model"""
    algae_type: str = Field(..., description="Type of algae", min_length=1, max_length=100)
    user_question: str = Field(..., description="User's question", min_length=1, max_length=500)
    classification_result: Optional[Dict[str, Any]] = None
    conversation_history: Optional[List[Dict[str, str]]] = None
    
    @field_validator('algae_type')
    @classmethod
    def validate_algae_type(cls, v: str) -> str:
        return v.strip()
    
    @field_validator('user_question')
    @classmethod
    def validate_question(cls, v: str) -> str:
        v = v.strip()
        if len(v) < 1:
            raise ValueError('Question cannot be empty')
        return v

class EnhanceResultRequest(BaseModel):
    """Enhance classification results request"""
    algae_type: str = Field(..., description="Type of algae")
    current_result: Dict[str, Any] = Field(..., description="Current classification result")
    custom_notes: Optional[str] = Field(None, max_length=500)

class AlgaeInfoRequest(BaseModel):
    """Get algae info request"""
    algae_type: str = Field(..., description="Type of algae")
    include_sources: bool = True

class FeedbackRequest(BaseModel):
    """User feedback request"""
    session_id: str
    question: str
    answer: str
    rating: int = Field(..., ge=1, le=5)
    helpful: bool
    comments: Optional[str] = Field(None, max_length=500)