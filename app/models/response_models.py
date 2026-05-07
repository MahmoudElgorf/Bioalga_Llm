from pydantic import BaseModel
from typing import Optional, List, Dict, Any
from datetime import datetime

class ChatResponse(BaseModel):
    """Chat response model"""
    response: str
    is_algae_related: bool
    recommendations: List[str] = []
    algae_type: str
    timestamp: datetime = datetime.now()
    confidence_boost: Optional[float] = None

class EnhanceResultResponse(BaseModel):
    """Enhanced classification result response"""
    algae_type: str
    scientific_name: str
    arabic_name: str = ""
    confidence: float
    is_toxic: bool
    toxicity_level: str
    toxicity_warning: str
    scientific_warning: str
    potential_toxins: List[str]
    health_risks: str
    environmental_notes: str
    treatment_methods: List[str] = []
    commercial_viability: Dict[str, Any]
    co2_sequestration_kg_per_kg: float
    habitat: str
    recommended_actions: List[str]
    safety_instructions: List[str]
    emergency_info: Optional[Dict[str, str]] = None
    enhanced_at: datetime = datetime.now()

class AlgaeInfoResponse(BaseModel):
    """Algae information response"""
    algae_type: str
    info: Dict[str, Any]
    sources: Optional[List[str]] = None

class HealthResponse(BaseModel):
    """Health check response"""
    status: str
    version: str
    timestamp: datetime
    openai_available: bool