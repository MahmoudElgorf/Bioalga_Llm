from fastapi import APIRouter, HTTPException
from app.models.request_models import AlgaeInfoRequest
from app.models.response_models import AlgaeInfoResponse
from app.services.algae_service import AlgaeService
from app.models.algae_knowledge import get_algae_info

router = APIRouter(prefix="/algae", tags=["Algae Info"])

@router.post("/info", response_model=AlgaeInfoResponse)
def get_algae_info_endpoint(request: AlgaeInfoRequest):  # إزالة async
    """Get detailed information about an algae type"""
    
    info = get_algae_info(request.algae_type)
    
    response_data = {
        "algae_type": request.algae_type,
        "info": {
            "scientific_name": info.get("scientific_name"),
            "arabic_name": info.get("arabic_name", info.get("scientific_name")),
            "category": info.get("category", "Unknown"),
            "toxicity": {
                "level": info.get("toxicity_level", "unknown"),
                "toxins": info.get("potential_toxins", []),
                "health_effects": info.get("health_effects", "No data")
            },
            "ecology": {
                "habitat": info.get("habitat", "Various"),
                "environmental_impact": info.get("habitat", "Data pending")
            },
            "commercial": {
                "sellable": info.get("sellable", False),
                "applications": info.get("uses", ["Research"]),
                "note": info.get("commercial_note", "")
            },
            "co2_fixation_kg_per_kg": info.get("co2_per_kg", 1.83),
            "treatment_methods": info.get("treatment_methods", [])
        }
    }
    
    if request.include_sources:
        response_data["sources"] = [
            "WHO Guidelines for Cyanobacteria",
            "EPA Harmful Algal Bloom Database", 
            "AlgaeBase.org"
        ]
    
    return AlgaeInfoResponse(**response_data)

@router.get("/toxicity/{algae_type}")
def get_toxicity_level(algae_type: str):  # إزالة async
    """Get toxicity level of an algae type"""
    return {
        "algae_type": algae_type,
        "toxicity_level": AlgaeService.get_toxicity_level(algae_type),
        "is_toxic": AlgaeService.is_toxic(algae_type),
        "safety_instructions": AlgaeService.get_safety_instructions(algae_type)
    }