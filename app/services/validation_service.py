from app.core.constants import ALGAE_KEYWORDS
from typing import Tuple, List

class ValidationService:
    """Service for validating questions and extracting algae mentions"""
    
    @staticmethod
    def is_algae_related(question: str) -> Tuple[bool, List[str]]:
        """
        Check if the question is related to algae
        Returns: (is_algae_related, list_of_found_keywords)
        """
        question_lower = question.lower()
        found_keywords = []
        
        for keyword in ALGAE_KEYWORDS:
            if keyword.lower() in question_lower:
                found_keywords.append(keyword)
        
        # Greeting and short questions are considered within scope
        if len(question.split()) <= 2 and not found_keywords:
            return True, found_keywords
            
        return len(found_keywords) > 0, found_keywords
    
    @staticmethod
    def extract_algae_mentions(text: str) -> List[str]:
        """Extract algae type names mentioned in the text"""
        known_types = [
            "Microcystis", "Anabaena", "Nostoc", "Skeletonema", 
            "Karenia", "Aphanizomenon", "Nodularia", "Oscillatoria",
            "Gymnodinium", "Prorocentrum", "Noctiluca", "Spirulina",
            "Chlorella", "Dunaliella", "Haematococcus", "Dolichospermum"
        ]
        
        found = []
        text_lower = text.lower()
        
        for algae_type in known_types:
            if algae_type.lower() in text_lower:
                found.append(algae_type)
        
        return found
    
    @staticmethod
    def sanitize_input(text: str, max_length: int = 500) -> str:
        """Sanitize user input to prevent injection and limit length"""
        if not text:
            return ""
        
        # Remove any potential injection patterns
        sanitized = text.strip()
        
        # Limit length
        if len(sanitized) > max_length:
            sanitized = sanitized[:max_length]
        
        return sanitized