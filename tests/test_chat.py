import pytest
from app.services.validation_service import ValidationService

def test_is_algae_related():
    service = ValidationService()
    
    # Algae related questions
    assert service.is_algae_related("What is microcystin?")[0] == True
    assert service.is_algae_related("Tell me about cyanobacteria")[0] == True
    assert service.is_algae_related("How to treat algal blooms?")[0] == True
    
    # Non-algae questions
    assert service.is_algae_related("What is the weather today?")[0] == False
    assert service.is_algae_related("Tell me a joke")[0] == False

def test_extract_algae_mentions():
    service = ValidationService()
    
    mentions = service.extract_algae_mentions("Microcystis and Anabaena are cyanobacteria")
    assert "Microcystis" in mentions
    assert "Anabaena" in mentions

def test_sanitize_input():
    service = ValidationService()
    
    long_text = "a" * 600
    sanitized = service.sanitize_input(long_text, max_length=500)
    assert len(sanitized) == 500
    
    assert service.sanitize_input("  hello  ") == "hello"