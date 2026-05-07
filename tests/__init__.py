"""
BioAlga Backend Tests
"""

import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Test configuration
TEST_CONFIG = {
    "test_openai_key": "sk-test-key-for-ci",
    "test_algae_types": [
        "Microcystis",
        "Anabaena", 
        "Nostoc",
        "Skeletonema",
        "Karenia"
    ]
}

__all__ = ['TEST_CONFIG']