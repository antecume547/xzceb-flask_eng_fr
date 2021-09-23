"""
module for initializing IBM Watson Language Translator 
"""
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
import sys, traceback
from ibm_watson import ApiException
from dotenv import load_dotenv

#get envars
load_dotenv()

#constants
APIKEY = os.environ['APIKEY']
URL = os.environ['URL']
API_VERSION = os.environ['API_VERSION']

def initialize_translator():
    """
    Function for instantiate the Translator. It gets global variables to authenticating and
    return with translator instance.
    """
    authenticator = IAMAuthenticator(APIKEY)
    language_translator = LanguageTranslatorV3(
        version=API_VERSION,
        authenticator=authenticator)

    return language_translator.set_service_url(URL)

def english_to_french(text:str, translator: LanguageTranslatorV3) -> DetailedResponse:
    """
    Function for translate English text to French. 
    """
    model_id = 'en-fr'
    source_lang = 'en'
    return translator.translate(
            text,
            model_id,
            source_lang
            ).get_result()

def french_to_english(text:str, translator: LanguageTranslatorV3) -> DetailedResponse:
    """
    Function for translate French text to English. 
    """
    model_id = 'fr-en'
    source_lang = 'fr'
    return translator.translate(
            text,
            model_id,
            source_lang
            ).get_result()

#try-catch
try:
    enText = 'This is a shiny day.'
    frText = 'C\'est un jour soleil.'

    tlator = initialize_translator()
    trToFr = english_to_french(enText, tlator)
    trToEn = french_to_english(frText, tlator)

except ApiException as ex:

    if type(ex) == ApiException:
        print "Method failed with status code " + str(ex.code) + ": " + ex.message
    else:
        print(ex)
        print(traceback.format_exc())


