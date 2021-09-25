import unittest
from translator import *


class TestIBMTranslator(unittest.TestCase):

    def test_initialize_translator(self):
        self.assertIsInstance(initialize_translator(), LanguageTranslatorV3)
        
        with self.assertRaises(ApiException):
            URL = os.environ['URL'] + 'some_tail'
            initialize_translator()
    
    def test_french_to_english(self):
        URL = os.environ['URL']
        translator_instance = initialize_translator();
        
        if translator_instance == None:
            raise Exception('The instance of translator has not initialized!')
       
        test_val = 'Bonjour'
        expected_val = 'Hello'
        self.assertEqual(french_to_english(test_val, translator_instance)['translations'][0]['translation'], expected_val)
    
        test_val = 'maison'
        expected_val = 'House'
        self.assertEqual(french_to_english(test_val, translator_instance)['translations'][0]['translation'], expected_val)
        
        test_val = 'racine'
        expected_val = 'Root'
        self.assertEqual(french_to_english(test_val, translator_instance)['translations'][0]['translation'], expected_val)
        
        with self.assertRaises(ValueError):
            test_val = None
            french_to_english(test_val, translator_instance)

def test_english_to_french(self):
        URL = os.environ['URL']
        translator_instance = initialize_translator();
        
        if translator_instance == None:
            raise Exception('The instance of translator has not initialized!')

        test_val = 'Good day'
        expected_val = 'Bonnjour'
        self.assertEqual(english_to_french(test_val, translator_instance)['translations'][0]['translation'], expected_val)

        test_val = 'I\'m going farther'
        expected_val = 'Je vais plus loin'
        self.assertEqual(english_to_french(test_val, translator_instance)['translations'][0]['translation'], expected_val)

        test_val = 'dog'
        expected_val = 'chien'
        self.assertEqual(english_to_french(test_val, translator_instance)['translations'][0]['translation'], expected_val)

        test_val = 'feather'
        expected_val = 'plume'
        self.assertEqual(english_to_french(test_val, translator_instance)['translations'][0]['translation'], expected_val)

        with self.assertRaises(ValueError):
            test_val = None
            expected_val = None
            self.assertEqual(english_to_french(test_val, translator_instance)['translations'][0]['translation'], expected_val)

if __name__ == '__main__':
    unittest.main()

