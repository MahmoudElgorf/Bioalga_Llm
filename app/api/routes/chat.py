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

# System prompt مع حرية أكبر وإرشادات لطيفة
SYSTEM_PROMPT = """You are BioAlga, a friendly and knowledgeable AI assistant specialized in algae and related fields (phycology, aquatic biology, environmental science, aquaculture, harmful algal blooms, toxins, climate impact, CO2 sequestration, etc.).

Your expertise includes:
- Algae classification, identification, and taxonomy
- Toxicity analysis, health effects, and safety warnings
- Environmental impact (eutrophication, red tides, hypoxia)
- Commercial applications (biofertilizers, aquaculture feed, biofuels, nutraceuticals)
- CO2 sequestration and climate relevance
- Water quality monitoring and treatment

Guidelines:
1. You can answer ANY question related to algae or its adjacent fields (marine biology, water ecology, phycotoxins, etc.).
2. If a question is completely unrelated (e.g., sports, politics, general news), politely redirect the user to algae topics.
3. For greetings or casual conversation, respond warmly and offer assistance on algae topics.
4. Always provide accurate, scientifically sound information.
5. Use clear language and include warnings when discussing toxic algae.

Remember: You are an algae expert, but you are also helpful and conversational. Engage the user and guide them towards useful information about algae."""

@router.post("/", response_model=ChatResponse)
def chat(request: ChatRequest):
    """
    Smart algae assistant - answers all algae-related questions freely.
    No hard rejection of non-algae topics; instead, the AI will respond appropriately.
    """
    try:
        # تحقق بسيط لتسجيل ما إذا كان السؤال ذا صلة (للاستخدام الداخلي فقط)
        is_relevant, keywords = validation_service.is_algae_related(request.user_question)
        
        # بناء سياق الطحلب الحالي (مهم للمعلومات الدقيقة)
        context = algae_service.get_algae_context(
            request.algae_type,
            request.classification_result
        )
        
        # بناء رسائل النظام مع السياق
        messages = [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "system", "content": f"Current algae being discussed: {request.algae_type}\nAdditional context: {context}"}
        ]
        
        if request.conversation_history:
            messages.extend(request.conversation_history[-15:])  # زيادة عدد الرسائل المحفوظة
        
        messages.append({"role": "user", "content": request.user_question})
        
        # استدعاء الـ AI (بدون حظر)
        result = ai_service.chat_with_messages(messages)
        
        # إضافة توصيات فقط إذا كان السؤال عن الطحالب بشكل واضح
        recommendations = []
        if request.classification_result:
            if request.classification_result.get('isToxic', False):
                recommendations.append(" This algae is toxic - handle with care")
            
            confidence = request.classification_result.get('confidence', 0)
            if confidence < 0.6:
                recommendations.append("Low classification confidence - consider recapturing the image")
        
        return ChatResponse(
            response=result['response'],
            is_algae_related=is_relevant,  # لا تؤثر على الرد، فقط للتسجيل
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

@router.post("/compare")
def compare_algae_types(algae_types: List[str]):
    """Compare multiple algae types"""
    from app.services.enhancement_service import EnhancementService
    comparison = EnhancementService.compare_algae_types(algae_types)
    return comparison