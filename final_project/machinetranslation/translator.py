import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()
api_key = os.environ['apikey']
url = os.environ['url']

# Create an instance of the IBM Watson Language Translator
authenticator = IAMAuthenticator(api_key)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)
language_translator.set_service_url(url)

# ... (the rest of the imports and setup code)

def translate_english_to_french(english_text):
    """Translate the English text to French."""
    if english_text is None:
        return None
    translation = language_translator.translate(
        text=english_text,
        source='en',
        target='fr'
    ).get_result()
    french_text = translation['translations'][0]['translation']
    return french_text

def translate_french_to_english(french_text):
    """Translate the French text to English."""
    if french_text is None:
        return None
    translation = language_translator.translate(
        text=french_text,
        source='fr',
        target='en'
    ).get_result()
    english_text = translation['translations'][0]['translation']
    return english_text
