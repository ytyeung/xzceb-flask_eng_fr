"""
This module provides en-fr / fr-en translation with IBM Watson Translation
"""

#import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv


load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

"""
Create translator instance
"""
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)


def englishToFrench(english_text):
    """
    Translate English to French
    """

    # return nothing when empty
    if english_text in ('',None):
        return ''

    translation = language_translator.translate(
        text=english_text,
        source='en',
        model_id='en-fr').get_result()

    french_text=translation['translations'][0]['translation']

    return french_text

def frenchToEnglish(french_text):
    """
    Translate French to English
    """
    # return nothing when empty
    if french_text in ('',None):
        return ''

    translation = language_translator.translate(
    text=french_text,
    source='fr',
    model_id='fr-en').get_result()

    english_text=translation['translations'][0]['translation']
    return english_text
