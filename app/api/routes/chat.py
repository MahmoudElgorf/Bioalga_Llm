from fastapi import APIRouter, HTTPException
from typing import Dict, Any, List
import logging

from app.models.request_models import ChatRequest
from app.models.response_models import ChatResponse
from app.services.ai_service import AIService
from app.services.algae_service import AlgaeService
from app.services.validation_service import ValidationService

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/chat", tags=["Chat"])

ai_service = AIService()
algae_service = AlgaeService()
validation_service = ValidationService()

SYSTEM_PROMPT = """You are a scientific assistant specialized 100% in algae only.

Your expertise includes:
- Algae classification and identification
- Toxicity analysis and safety warnings
- Environmental impact assessment
- Commercial applications (aquaculture, biofertilizers, research)
- CO2 sequestration and climate relevance

Strict rules:
1. Answer ONLY questions related to algae
2. If user asks about non-algae topics, politely refuse: "I am specialized in algae only. Please ask about algae classification, toxicity, applications, or environmental impact."
3. For toxic algae, always include clear warnings
4. Be scientifically accurate and concise
5. Respond in the same language as the user's question

Remember: Your specialization is algae only."""

@router.post("/", response_model=ChatResponse)
def chat(request: ChatRequest):  # إزالة async
    """
    Smart algae specialist assistant
    Answers only algae-related questions
    """
    try:
        # Check if question is algae-related
        is_relevant, keywords = validation_service.is_algae_related(request.user_question)
        
        if not is_relevant and len(request.user_question.split()) > 3:
            return ChatResponse(
                response="I am a specialist in algae only. I can help you with:\n- Algae classification and toxicity\n- Environmental impact assessment\n- Commercial applications (aquaculture, biofertilizers)\n- Safety instructions for handling\n\nDo you have a specific question about algae?",
                is_algae_related=False,
                recommendations=["ask_algae_specific_question"],
                algae_type=request.algae_type
            )
        
        # Build algae context
        context = algae_service.get_algae_context(
            request.algae_type,
            request.classification_result
        )
        
        # Build messages for AI
        messages = [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "system", "content": f"Current algae being discussed: {request.algae_type}\nContext: {context}"}
        ]
        
        if request.conversation_history:
            messages.extend(request.conversation_history[-10:])
        
        messages.append({"role": "user", "content": request.user_question})
        
        # Get AI response (no await)
        result = ai_service.chat_with_messages(messages)
        
        # Build recommendations
        recommendations = []
        if request.classification_result:
            if request.classification_result.get('isToxic', False):
                recommendations.append("This algae is toxic - avoid direct contact")
            
            confidence = request.classification_result.get('confidence', 0)
            if confidence < 0.6:
                recommendations.append("Low confidence - consider recapturing with better lighting")
            elif confidence < 0.8:
                recommendations.append("Medium confidence - secondary verification recommended")
        
        return ChatResponse(
            response=result['response'],
            is_algae_related=True,
            recommendations=recommendations,
            algae_type=request.algae_type,
            confidence_boost=result.get('confidence_boost')
        )
        
    except Exception as e:
        logger.error(f"Chat error: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/types")
def get_available_types():
    """Get list of all available algae types"""
    return {
        "types": algae_service.get_available_algae_types(),
        "count": len(algae_service.get_available_algae_types())
    }