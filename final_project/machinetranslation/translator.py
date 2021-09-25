"""
Module for initializing IBM Watson Language Translator 
"""
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

#import these for debugging purpose 
#import sys, traceback
#import json
#from ibm_watson import ApiException

#get envars
load_dotenv()

#global constants for connection to the API endpoint
APIKEY = os.environ['APIKEY']
URL = os.environ['URL']
API_VERSION = os.environ['API_VERSION']

def initialize_translator() -> LanguageTranslatorV3:
    """
    Function for instantiate the Translator. It gets global variables to authenticating and
    return with translator instance.
    """
    authenticator = IAMAuthenticator(APIKEY)
    language_translator = LanguageTranslatorV3(
    version=API_VERSION,
    authenticator=authenticator)
    language_translator.set_service_url(URL)

    return language_translator

def english_to_french(text:str, translator: LanguageTranslatorV3) -> dict:
    """
    Function for translate English text to French.
    """
    model_id = 'en-fr'
    source_lang = 'en'
    res = translator.translate(
            text=text,
            model_id=model_id,
            source=source_lang).get_result()
#    print(json.dumps(res, indent=2, ensure_ascii=False))
    return res


def french_to_english(text:str, translator: LanguageTranslatorV3) -> dict:
    """
    Function for translate French text to English.
    """
    model_id = 'fr-en'
    source_lang = 'fr'
    res = translator.translate(
            text=text,
            model_id=model_id,
            source=source_lang).get_result()
#    print(json.dumps(res, indent=2, ensure_ascii=False))
    return res

#try-catch for debugging purpose
#try:
#    enText = 'This is a shiny day.'
#    frText = 'C\'est un jour soleil.'
#    tlator = initialize_translator()
#    trToFr = english_to_french(enText, tlator)
#    #trToEn = french_to_english(frText, tlator)
#
#except ApiException as ex:
#
#        print ("Method failed with status code " + str(ex.code) + ": " + ex.message)
#except Exception as ex:
#        print(ex)
#        print(traceback.format_exc())
