"""
Unit test Module to the translator module
"""
import json
import os
import unittest
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import ApiException
from dotenv import load_dotenv
from translator import initialize_translator, french_to_english, english_to_french
#get envars
load_dotenv()

#global constants for connection to the API endpoint
APIKEY = os.environ['APIKEY']
URL = os.environ['URL']
API_VERSION = os.environ['API_VERSION']

class TestIBMTranslator(unittest.TestCase):
    """
    Class for unittesting translator module's functions 
    """
    def test_initialize_translator(self):
        """
        testing if initialize_translator() function returns with type LanguageTranslatorV3  
        """
        self.assertIsInstance(initialize_translator(), LanguageTranslatorV3)
        
    def test_french_to_english(self):
        """
        Testing if the french_to_english function returns with the appropriate values and if throws the ValueError exception
        when the parameter is None object
        """
        translator_instance = initialize_translator();
        
        if translator_instance == None:
            raise Exception('Instance of translator has not initialized!')
       
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
        """
        Testing if the english_to_french function returns with the appropriate values and if throws the ValueError exception
        when the parameter is None object
        """
        URL = os.environ['URL']
        translator_instance = initialize_translator();
        
        if translator_instance == None:
            raise Exception('The instance of translator has not initialized!')

        test_val = 'Hello'
        expected_val = 'Bonjour'
        self.assertEqual(english_to_french(test_val, translator_instance)['translations'][0]['translation'], expected_val)

        test_val = 'I\'m going farther'
        expected_val = 'Je vais plus loin'
        self.assertEqual(english_to_french(test_val, translator_instance)['translations'][0]['translation'], expected_val)

        test_val = 'dog'
        expected_val = 'Chien'
        self.assertEqual(english_to_french(test_val, translator_instance)['translations'][0]['translation'], expected_val)

        test_val = 'feather'
        expected_val = 'Plume'
        self.assertEqual(english_to_french(test_val, translator_instance)['translations'][0]['translation'], expected_val)

        with self.assertRaises(ValueError):
            test_val = None
            expected_val = None
            self.assertEqual(english_to_french(test_val, translator_instance)['translations'][0]['translation'], expected_val)

if __name__ == '__main__':
    unittest.main()

