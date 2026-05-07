"""
BioAlga Backend Application
AI-powered algae classification assistant and knowledge base
"""

__version__ = "2.0.0"
__author__ = "BioAlga Team"
__description__ = "Specialized algae classification and information system"

from app.core.config import settings
from app.core.constants import ALGAE_KEYWORDS, ERROR_MESSAGES

__all__ = [
    'settings',
    'ALGAE_KEYWORDS', 
    'ERROR_MESSAGES',
    '__version__'
]