from typing import Dict, Any, List
from app.models.algae_knowledge import get_algae_info

class EnhancementService:
    """Service for enhancing classification results with knowledge base"""
    
    @staticmethod
    def enhance_classification_result(algae_type: str, current_result: Dict[str, Any]) -> Dict[str, Any]:
        """Enhance raw classification results with knowledge base data"""
        
        info = get_algae_info(algae_type)
        toxicity_base = info.get('toxicity_level', 'unknown')
        current_toxic = current_result.get('isToxic', False)
        
        is_toxic = current_toxic or toxicity_base in ['severe', 'high']
        
        enhanced = {
            "algae_type": algae_type,
            "scientific_name": info.get('scientific_name', current_result.get('scientificName', 'Unknown')),
            "arabic_name": info.get('arabic_name', ''),
            "confidence": current_result.get('confidence', 0.5),
            "is_toxic": is_toxic,
            "toxicity_level": toxicity_base,
            "toxicity_warning": info.get('toxicity_warning', 'No toxicity data available'),
            "scientific_warning": info.get('scientific_warning', 'Consult expert for verification'),
            "potential_toxins": info.get('potential_toxins', current_result.get('potentialToxins', [])),
            "health_risks": info.get('health_effects', 'Data pending'),
            "environmental_notes": info.get('habitat', 'No data available'),
            "treatment_methods": info.get('treatment_methods', []),
            "commercial_viability": {
                "sellable": info.get('sellable', False),
                "applications": info.get('uses', ['Research only']),
                "benefits": info.get('benefits', []),
                "note": EnhancementService._get_commercial_note(algae_type, info)
            },
            "co2_sequestration_kg_per_kg": info.get('co2_per_kg', 1.83),
            "habitat": info.get('habitat', 'Various aquatic environments'),
            "recommended_actions": [],
            "safety_instructions": [],
            "emergency_info": None
        }
        
        # Add safety instructions based on toxicity
        if is_toxic:
            enhanced["safety_instructions"] = [
                "DO NOT consume or handle without protective equipment",
                "Keep away from children and pets",
                "Avoid contact with drinking water sources",
                "Seek medical attention if exposed"
            ]
            enhanced["recommended_actions"].append("contact_professional")
            
            if 'symptoms_if_ingested' in info:
                enhanced["emergency_info"] = {
                    "symptoms": info.get('symptoms_if_ingested', 'Unknown'),
                    "action": "Contact Poison Control Center immediately"
                }
        else:
            enhanced["safety_instructions"] = [
                "General safety: Use standard laboratory precautions",
                "Verify strain certification before commercial use"
            ]
        
        # Recommendations based on confidence
        confidence = enhanced["confidence"]
        if confidence < 0.6:
            enhanced["recommended_actions"].append("reclassify_with_clearer_sample")
            enhanced["recommended_actions"].append("send_to_lab_for_confirmation")
        elif confidence < 0.8:
            enhanced["recommended_actions"].append("consider_secondary_verification")
        
        return enhanced
    
    @staticmethod
    def _get_commercial_note(algae_type: str, info: Dict[str, Any]) -> str:
        """Get commercial viability note"""
        sellable = info.get('sellable', 'Unknown')
        
        if sellable == 'Yes':
            return 'Commercially viable for aquaculture and research'
        elif sellable == 'No':
            return 'Not suitable for commercial sale - research only'
        elif sellable == 'Conditional':
            return 'Conditional - requires strain certification and safety testing'
        else:
            return 'Consult expert before commercial use'
    
    @staticmethod
    def generate_summary(enhanced_result: Dict[str, Any]) -> str:
        """Generate a text summary of enhanced results"""
        
        if enhanced_result["is_toxic"]:
            summary = f"WARNING: {enhanced_result['algae_type']} is a "
            summary += f"{'severely ' if enhanced_result['toxicity_level'] == 'severe' else ''}toxic algae.\n\n"
            summary += f"Toxins: {', '.join(enhanced_result['potential_toxins'][:2])}\n"
            summary += f"Health Risks: {enhanced_result['health_risks'][:100]}\n"
            summary += f"Recommendation: {enhanced_result['recommended_actions'][0] if enhanced_result['recommended_actions'] else 'Consult specialist'}"
        else:
            summary = f"{enhanced_result['algae_type']} - "
            summary += f"{enhanced_result['toxicity_level'].upper()} toxicity level\n"
            summary += f"Confidence: {(enhanced_result['confidence']*100):.0f}%\n"
            
            if enhanced_result['commercial_viability']['sellable'] == 'Yes':
                summary += f"Commercial: Yes - {enhanced_result['commercial_viability']['note'][:80]}"
            elif enhanced_result['commercial_viability']['sellable'] == 'Conditional':
                summary += f"Commercial: Conditional - {enhanced_result['commercial_viability']['note'][:80]}"
            else:
                summary += f"Commercial: Not viable - {enhanced_result['commercial_viability']['note'][:80]}"
        
        return summary

    @staticmethod
    def compare_algae_types(algae_list: List[str]) -> Dict[str, Any]:
        """Compare multiple algae types"""
        comparison = {
            "algae_types": algae_list,
            "toxicity_summary": {},
            "commercial_summary": {},
            "recommendations": []
        }
        
        for algae_type in algae_list:
            info = get_algae_info(algae_type)
            comparison["toxicity_summary"][algae_type] = {
                "is_toxic": info.get('is_toxic', False),
                "toxicity_level": info.get('toxicity_level', 'unknown'),
                "toxins": info.get('potential_toxins', [])[:2]
            }
            comparison["commercial_summary"][algae_type] = {
                "sellable": info.get('sellable', 'Unknown'),
                "applications": info.get('uses', [])[:2]
            }
        
        return comparison