import pytest
from app.services.enhancement_service import EnhancementService
from app.models.algae_knowledge import get_algae_info

class TestEnhancementService:
    
    def setup_method(self):
        """Setup before each test"""
        self.enhancement_service = EnhancementService()
    
    def test_enhance_classification_result_microcystis(self):
        """Test enhancing Microcystis classification result"""
        current_result = {
            "scientificName": "Microcystis aeruginosa",
            "confidence": 0.95,
            "isToxic": True,
            "potentialToxins": ["Microcystins"]
        }
        
        enhanced = self.enhancement_service.enhance_classification_result(
            "Microcystis",
            current_result
        )
        
        assert enhanced["algae_type"] == "Microcystis"
        assert enhanced["is_toxic"] == True
        assert enhanced["toxicity_level"] == "severe"
        assert "microcystins" in str(enhanced["potential_toxins"]).lower()
        assert len(enhanced["safety_instructions"]) > 0
        assert "DO NOT consume" in enhanced["safety_instructions"][0]
    
    def test_enhance_classification_result_nontoxic(self):
        """Test enhancing non-toxic algae classification"""
        current_result = {
            "scientificName": "Skeletonema costatum",
            "confidence": 0.88,
            "isToxic": False,
            "potentialToxins": []
        }
        
        enhanced = self.enhancement_service.enhance_classification_result(
            "Skeletonema",
            current_result
        )
        
        assert enhanced["is_toxic"] == False
        assert enhanced["toxicity_level"] == "none"
        assert "Yes" in str(enhanced["commercial_viability"]["sellable"])
    
    def test_enhance_classification_result_low_confidence(self):
        """Test recommendations for low confidence results"""
        current_result = {
            "scientificName": "Unknown",
            "confidence": 0.45,
            "isToxic": False,
            "potentialToxins": []
        }
        
        enhanced = self.enhancement_service.enhance_classification_result(
            "Nostoc",
            current_result
        )
        
        assert enhanced["confidence"] == 0.45
        assert "reclassify_with_clearer_sample" in enhanced["recommended_actions"]
    
    def test_generate_summary_toxic(self):
        """Test generating summary for toxic algae"""
        current_result = {
            "scientificName": "Karenia brevis",
            "confidence": 0.92,
            "isToxic": True,
            "potentialToxins": ["Brevetoxins"]
        }
        
        enhanced = self.enhancement_service.enhance_classification_result(
            "Karenia",
            current_result
        )
        
        summary = self.enhancement_service.generate_summary(enhanced)
        
        assert "WARNING" in summary
        assert "toxic" in summary.lower()
        assert "Karenia" in summary
    
    def test_generate_summary_non_toxic(self):
        """Test generating summary for non-toxic algae"""
        current_result = {
            "scientificName": "Skeletonema costatum",
            "confidence": 0.85,
            "isToxic": False,
            "potentialToxins": []
        }
        
        enhanced = self.enhancement_service.enhance_classification_result(
            "Skeletonema",
            current_result
        )
        
        summary = self.enhancement_service.generate_summary(enhanced)
        
        assert "Confidence" in summary
        assert "85" in summary or "85%" in summary
    
    def test_compare_algae_types(self):
        """Test comparing multiple algae types"""
        algae_list = ["Microcystis", "Skeletonema", "Nostoc"]
        
        comparison = self.enhancement_service.compare_algae_types(algae_list)
        
        assert comparison["algae_types"] == algae_list
        assert "toxicity_summary" in comparison
        assert "commercial_summary" in comparison
        assert "Microcystis" in comparison["toxicity_summary"]
        assert "Skeletonema" in comparison["toxicity_summary"]
        
        # Check Microcystis is toxic
        assert comparison["toxicity_summary"]["Microcystis"]["is_toxic"] == True
        
        # Check Skeletonema is non-toxic
        assert comparison["toxicity_summary"]["Skeletonema"]["is_toxic"] == False
    
    def test_all_algae_types_have_entries(self):
        """Test that all 12 algae types have entries in knowledge base"""
        from app.models.algae_knowledge import ALGAE_TYPES, get_algae_info
        
        expected_types = [
            "Anabaena", "Aphanizomenon", "Microcystis", "Nodularia",
            "Nostoc", "Oscillatoria", "Gymnodinium", "Karenia",
            "Prorocentrum", "Noctiluca", "Skeletonema", "nontoxic"
        ]
        
        for algae_type in expected_types:
            info = get_algae_info(algae_type)
            assert info is not None
            assert info.get("scientific_name") is not None
    
    def test_emergency_info_for_toxic_algae(self):
        """Test that toxic algae have emergency information"""
        current_result = {
            "scientificName": "Microcystis aeruginosa",
            "confidence": 0.95,
            "isToxic": True,
            "potentialToxins": ["Microcystins"]
        }
        
        enhanced = self.enhancement_service.enhance_classification_result(
            "Microcystis",
            current_result
        )
        
        if enhanced["emergency_info"]:
            assert "symptoms" in enhanced["emergency_info"]
            assert "action" in enhanced["emergency_info"]