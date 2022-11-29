"""
Unit test for translator.py modeules
"""

import unittest
from translator import englishToFrench,frenchToEnglish

class TestEnglishToFrench (unittest.TestCase):
    """
    Unit test for translator.py english_to_french
    """
    def test_for_null(self):
        """
        test for null '', return None when null
        """
        self.assertEqual(englishToFrench(''), None)

    def test_for_hello(self):
        """
        Test for Hello
        """
        self.assertEqual(englishToFrench('Hello'),'Bonjour')

class FrenchToEnglish(unittest.TestCase):
    """
    Unit test for translator.py french_to_english
    """
    def test_for_null(self):
        """
        Test for null '', return None when null
        """
        self.assertEqual(frenchToEnglish(''), None)
    def test_for_bonjour(self):
        """
        Test for Bonjour
        """
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')

unittest.main()