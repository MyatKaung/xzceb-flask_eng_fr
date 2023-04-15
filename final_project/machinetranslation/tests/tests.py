import unittest
from translator import translate_english_to_french, translate_french_to_english

class TestTranslatorMethods(unittest.TestCase):
    def test_translate_french_to_english_null_input(self):
        self.assertEqual(translate_french_to_english(None), None)

    def test_translate_english_to_french_null_input(self):
        self.assertEqual(translate_english_to_french(None), None)

    def test_translate_english_to_french_hello(self):
        self.assertEqual(translate_english_to_french("Hello"), "Bonjour")

    def test_translate_french_to_english_bonjour(self):
        self.assertEqual(translate_french_to_english("Bonjour"), "Hello")

    def test_translate_french_to_english_hello(self):
        self.assertNotEqual(translate_french_to_english("Hello"), "Bonjour")

    def test_translate_english_to_french_bonjour(self):
        self.assertNotEqual(translate_english_to_french("Bonjour"), "Hello")

if __name__ == '__main__':
    unittest.main()

    