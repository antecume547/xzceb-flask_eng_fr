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
        print(type(translator_instance))
        if translator_instance == None:
            raise Exception('The instance of translator has not initialized!')
       
        test_val = 'Bonjour'
        expected_val = 'God day'
        self.assertEqual(french_to_english(translator_instance,str(test_val)), expected_val)
    
        test_val = 'colere'
        expected_val = 'anger'
        self.assertEqual(french_to_english(translator_instance,test_val), expected_val)
        
        test_val = 'racine'
        expected_val = 'root'
        self.assertEqual(french_to_english(translator_instance,test_val), expected_val)
        
        test_val = None
        expected_val = None
        self.assertEqual(french_to_english(translator_instance,test_val), expected_val)

def test_english_to_french(self):
        URL = os.environ['URL']
        translator_instance = initialize_translator();
        test_val = 'Good day'
        expected_val = 'Bonnjour'
        self.assertEqual(english_to_french(translator_instance,test_val), expected_val)

        test_val = 'I\'m going farther'
        expected_val = 'Je vais plus loin'
        self.assertEqual(english_to_french(translator_instance,test_val), expected_val)

        test_val = 'dog'
        expected_val = 'chien'
        self.assertEqual(english_to_french(translator_instance,test_val), expected_val)

        test_val = 'feather'
        expected_val = 'plume'
        self.assertEqual(english_to_french(translator_instance,test_val), expected_val)

        test_val = None
        expected_val = None
        self.assertEqual(english_to_french(translator_instance,test_val), expected_val)

if __name__ == '__main__':
    unittest.main()

