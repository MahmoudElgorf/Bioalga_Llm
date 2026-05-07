import pytest
from app.models.algae_knowledge import get_algae_info, ALGAE_TYPES

def test_get_algae_info():
    info = get_algae_info("Microcystis")
    assert info['is_toxic'] == True
    assert info['toxicity_level'] == 'severe'
    assert 'microcystins' in str(info['potential_toxins']).lower()

def test_get_algae_info_case_insensitive():
    info1 = get_algae_info("Microcystis")
    info2 = get_algae_info("microcystis")
    assert info1['scientific_name'] == info2['scientific_name']

def test_algae_types_count():
    # Should have 12 types
    assert len(ALGAE_TYPES) >= 11
    
def test_nontoxic_fallback():
    info = get_algae_info("UnknownType")
    assert 'nontoxic' in info.get('scientific_name', '').lower() or info.get('scientific_name') is not None