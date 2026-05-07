class BioAlgaException(Exception):
    """Base exception for BioAlga application"""
    pass

class AlgaeNotFoundError(BioAlgaException):
    """Raised when an algae type is not found in knowledge base"""
    pass

class OpenAIError(BioAlgaException):
    """Raised when OpenAI API fails"""
    pass

class ValidationError(BioAlgaException):
    """Raised when input validation fails"""
    pass

class RateLimitError(BioAlgaException):
    """Raised when rate limit is exceeded"""
    pass