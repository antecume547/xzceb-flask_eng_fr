import unittest
from translator import *

#from dotenv import load_dotenv
#from ibm_watson import LanguageTranslatorV3
#from ibm_cloud_sdk_core.authenticators import IAMAuthenticator


#get envars for tests
#load_dotenv()
#
##global constants for tests
#APIKEY = os.environ['APIKEY']
#URL = os.environ['URL']
#API_VERSION = os.environ['API_VERSION']

class TestIBMTranslator(unittest.TestCase):

    def test_initialize_translator(self):
        self.assertIsInstance(initialize_translator(), LanguageTranslatorV3)
        
        with self.assertRaise(ApiException):
        URL = os.environ['URL'] + 'some_tail'
        initialize_translator()
    
    def test_french_to_english(self):
        translator_instance = initialize_translator();
       
        test_val = 'Bonjour'
        expected_val = 'God day'
        self.assertEquale(french_to_english(french_to_english(translator_instance,test_val), expected_val))
    
        test_val = 'colere'
        expected_val = 'anger'
        self.assertEquale(french_to_english(french_to_english(translator_instance,test_val), expected_val))
        
        test_val = 'racine'
        expected_val = 'root'
        self.assertEquale(french_to_english(french_to_english(translator_instance,test_val), expected_val))
        
        test_val = None
        expected_val = None
        self.assertEquale(french_to_english(french_to_english(translator_instance,test_val), expected_val))

def test_ english_to_french(self):
        translator_instance = initialize_translator();
        test_val = 'Good day'
        expected_val = 'Bonnjour'
        self.assertEquale(english_to_french(english_to_french(translator_instance,test_val), expected_val))

        test_val = 'I\'m going farther'
        expected_val = 'Je vais plus loin'
        self.assertEquale(english_to_french(english_to_french(translator_instance,test_val), expected_val))

        test_val = 'dog'
        expected_val = 'chien'
        self.assertEquale(english_to_french(english_to_french(translator_instance,test_val), expected_val))

        test_val = 'feather'
        expected_val = 'plume'
        self.assertEquale(english_to_french(english_to_french(translator_instance,test_val), expected_val))

        test_val = None
        expected_val = None
        self.assertEquale(english_to_french(english_to_french(translator_instance,test_val), expected_val))

if __name__ == '__main__':
    unittest.main()

