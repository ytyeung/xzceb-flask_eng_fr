import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
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


def englishToFrench(englishText):
    """
    Translate English to French
    """
    translation = language_translator.translate(
        text=englishText,
        source='en',
        model_id='en-fr').get_result()

    frenchText=translation['translations'][0]['translation']

    return frenchText

def frenchToEnglish(frenchText):
    """
    Translate French to English
    """
    translation = language_translator.translate(
    text=frenchText,
    source='fr',
    model_id='fr-en').get_result()

    englishText=translation['translations'][0]['translation']
    return englishText