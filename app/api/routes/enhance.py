from fastapi import APIRouter, HTTPException
from typing import Dict, Any

from app.models.request_models import EnhanceResultRequest
from app.models.response_models import EnhanceResultResponse
from app.services.enhancement_service import EnhancementService
from app.models.algae_knowledge import get_algae_info

router = APIRouter(prefix="/enhance", tags=["Enhancement"])
enhancement_service = EnhancementService()

@router.post("/results", response_model=EnhanceResultResponse)
def enhance_results(request: EnhanceResultRequest):  # إزالة async
    """Enhance and structure classification results"""
    try:
        enhanced = enhancement_service.enhance_classification_result(
            request.algae_type,
            request.current_result
        )
        
        if request.custom_notes:
            enhanced["user_notes"] = request.custom_notes
        
        return EnhanceResultResponse(**enhanced)
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/summary")
def generate_summary(request: EnhanceResultRequest):  # إزالة async
    """Generate text summary of enhanced results"""
    try:
        enhanced = enhancement_service.enhance_classification_result(
            request.algae_type,
            request.current_result
        )
        summary = enhancement_service.generate_summary(enhanced)
        
        return {
            "summary": summary,
            "algae_type": request.algae_type
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/toxicity/{algae_type}")
def get_toxicity_summary(algae_type: str):  # إزالة async
    """Quick toxicity summary for an algae type"""
    info = get_algae_info(algae_type)
    
    return {
        "algae_type": algae_type,
        "scientific_name": info.get('scientific_name'),
        "is_toxic": info.get('is_toxic', False),
        "toxicity_level": info.get('toxicity_level', 'unknown'),
        "toxicity_warning": info.get('toxicity_warning', 'No data'),
        "potential_toxins": info.get('potential_toxins', []),
        "sellable": info.get('sellable', 'Unknown')
    }