from typing import Dict, Any, List, Optional
from app.models.algae_knowledge import get_algae_info, ALGAE_TYPES, is_toxic_type, get_toxicity_level

class AlgaeService:
    """Core service for algae business logic"""
    
    @staticmethod
    def get_algae_context(algae_type: str, classification_result: Optional[Dict] = None) -> str:
        """Build scientific context string about the algae"""
        info = get_algae_info(algae_type)
        
        context_parts = [
            f"Scientific Name: {info.get('scientific_name', 'Unknown')}",
            f"Category: {info.get('category', 'Unknown')}",
            f"Toxicity Level: {info.get('toxicity_level', 'unknown').upper()}",
            f"Toxicity Warning: {info.get('toxicity_warning', 'No warning available')}",
            f"Scientific Warning: {info.get('scientific_warning', 'Consult expert')}",
        ]
        
        if info.get('potential_toxins'):
            context_parts.append(f"Known Toxins: {', '.join(info['potential_toxins'])}")
        
        context_parts.append(f"CO2 Sequestration: {info.get('co2_per_kg', 1.83)} kg CO2 per kg dry biomass")
        context_parts.append(f"Commercial Viability: {info.get('sellable', 'Unknown')}")
        
        if info.get('benefits'):
            context_parts.append(f"Benefits: {'; '.join(info['benefits'][:2])}")
        
        if info.get('uses'):
            context_parts.append(f"Applications: {'; '.join(info['uses'][:2])}")
        
        if classification_result:
            confidence = classification_result.get('confidence', 0)
            context_parts.append(f"Classification Confidence: {confidence*100:.1f}%")
            
            if classification_result.get('isToxic'):
                context_parts.append("TOXICITY DETECTED: Handle with extreme caution")
        
        return "\n".join(context_parts)
    
    @staticmethod
    def get_available_algae_types() -> List[str]:
        """Get list of all available algae types in knowledge base"""
        return ALGAE_TYPES.copy()
    
    @staticmethod
    def get_toxicity_level(algae_type: str) -> str:
        """Get toxicity level string"""
        return get_toxicity_level(algae_type)
    
    @staticmethod
    def is_toxic(algae_type: str) -> bool:
        """Check if algae type is toxic"""
        return is_toxic_type(algae_type)
    
    @staticmethod
    def get_safety_instructions(algae_type: str) -> List[str]:
        """Get safety instructions for handling"""
        info = get_algae_info(algae_type)
        is_toxic = info.get('is_toxic', False)
        toxicity_level = info.get('toxicity_level', 'unknown')
        
        base_instructions = [
            "Wear gloves and protective eyewear when handling",
            "Wash hands thoroughly after contact",
            "Do not consume without laboratory analysis",
            "Contact poison control if ingested"
        ]
        
        if is_toxic or toxicity_level in ['severe', 'high']:
            return [
                "SEVERE WARNING: This algae is highly toxic",
                "Avoid all direct contact",
                "Handle only in controlled laboratory environment",
                "If exposed, seek immediate medical attention",
                "Do not allow contact with drinking water sources"
            ] + base_instructions
        elif toxicity_level == 'variable':
            return [
                "CAUTION: Toxicity varies by strain",
                "Laboratory analysis required before handling",
                "Assume toxic until proven otherwise"
            ] + base_instructions
        else:
            return base_instructions
    
    @staticmethod
    def get_commercial_potential(algae_type: str) -> Dict[str, Any]:
        """Get commercial potential analysis"""
        info = get_algae_info(algae_type)
        
        return {
            "sellable": info.get('sellable', 'Unknown'),
            "applications": info.get('uses', []),
            "benefits": info.get('benefits', []),
            "restrictions": EnhancementService._get_commercial_note(algae_type, info) if hasattr(EnhancementService, '_get_commercial_note') else "Consult expert",
            "co2_value": info.get('co2_per_kg', 1.83)
        }

# Import here to avoid circular import
from app.services.enhancement_service import EnhancementService