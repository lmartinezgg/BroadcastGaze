# test_broadcastgaze.py
"""
Tests for BroadcastGaze module.
"""

import unittest
from broadcastgaze import BroadcastGaze

class TestBroadcastGaze(unittest.TestCase):
    """Test cases for BroadcastGaze class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = BroadcastGaze()
        self.assertIsInstance(instance, BroadcastGaze)
        
    def test_run_method(self):
        """Test the run method."""
        instance = BroadcastGaze()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
