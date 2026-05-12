from app.core.constants import ALGAE_KEYWORDS
from typing import Tuple, List

class ValidationService:
    """Service for validating questions - now more permissive"""
    
    @staticmethod
    def is_algae_related(question: str) -> Tuple[bool, List[str]]:
        """
        Check if the question is related to algae or adjacent fields.
        Returns: (is_related, list_of_found_keywords)
        Now more permissive: only completely unrelated short questions are marked false.
        """
        question_lower = question.lower()
        found_keywords = []
        
        for keyword in ALGAE_KEYWORDS:
            if keyword.lower() in question_lower:
                found_keywords.append(keyword)
        
        # إذا كان السؤال طويلاً (>20 حرف) ووجدنا أي كلمة مفتاحية، أو حتى بدونها نعتبره ذا صلة
        # هذا يسمح بمرور معظم الأسئلة
        if len(question.split()) > 3 or len(question) > 20:
            # الأسئلة الطويلة تعتبر ذات صلة افتراضياً
            return True, found_keywords
        
        # تحيات قصيرة جداً (مثل "hi", "hello") نعتبرها ذات صلة ونتعامل معها لطيفاً
        short_greetings = ["hi", "hello", "hey", "مرحبا", "اهلا", "سلام", "thanks", "شكرا"]
        if question_lower in short_greetings:
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
    def sanitize_input(text: str, max_length: int = 1000) -> str:
        """Sanitize user input - increased max length"""
        if not text:
            return ""
        
        sanitized = text.strip()
        
        if len(sanitized) > max_length:
            sanitized = sanitized[:max_length]
        
        return sanitized