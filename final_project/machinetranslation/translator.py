"""
module for initializing IBM Watson Language Translator 
"""
import json
import os
import sys, traceback
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import ApiException
from dotenv import load_dotenv

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
#    try:
    authenticator = IAMAuthenticator(APIKEY)
    language_translator = LanguageTranslatorV3(
    version=API_VERSION,
    authenticator=authenticator)
    language_translator.set_service_url(URL)

    return language_translator

#    except ApiException as ex:

#            print ("Method failed with status code " + str(ex.code) + ": " + ex.message)
        
#    except Exception as ex:
#            print(ex)
#            print(traceback.format_exc())

def english_to_french(text:str, translator: LanguageTranslatorV3) -> dict:
    """
    Function for translate English text to French. 
    """
#    try:
    model_id = 'en-fr'
    source_lang = 'en'
    res = translator.translate(
            text=text,
            model_id=model_id,
            source=source_lang).get_result()
    print(json.dumps(res, indent=2, ensure_ascii=False))
    return res
    
#    except Exception as ex:
#        print(ex)
#        print(traceback.format_exc())

def french_to_english(text:str, translator: LanguageTranslatorV3) -> dict:
    """
    Function for translate French text to English. 
    """
#    try:
    model_id = 'fr-en'
    source_lang = 'fr'
    res = translator.translate(
            text=text,
            model_id=model_id,
            source=source_lang).get_result()
    print(json.dumps(res, indent=2, ensure_ascii=False))
    return res

#    except Exception as ex:
#        print(ex)
#        print(traceback.format_exc())
#try-catch
#try:
#    enText = 'This is a shiny day.'
#    frText = 'C\'est un jour soleil.'
#    tlator = initialize_translator()
#    trToFr = english_to_french(enText, tlator)
#    #trToEn = french_to_english(frText, tlator)
#
#except ApiException as ex:
#
#    if type(ex) == ApiException:
#        print ("Method failed with status code " + str(ex.code) + ": " + ex.message)
#    else:
#        print(ex)
#        print(traceback.format_exc())


