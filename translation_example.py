#!/usr/bin/env python3
"""
Translation Examples using TextBlob
This script demonstrates simple language translation using the TextBlob library.
Note: TextBlob uses Google Translate API for translation.
"""

from textblob import TextBlob

def translate_text(text, from_lang='en', to_lang='es'):
    """Translate text from one language to another."""
    blob = TextBlob(text)
    try:
        translated = blob.translate(from_lang=from_lang, to=to_lang)
        return str(translated)
    except Exception as e:
        return f"Translation error: {e}"

def detect_language(text):
    """Detect the language of given text."""
    blob = TextBlob(text)
    try:
        detected_lang = blob.detect_language()
        return detected_lang
    except Exception as e:
        return f"Detection error: {e}"

def english_to_multiple_languages():
    """Translate English text to multiple languages."""
    print("=" * 60)
    print("ENGLISH TO MULTIPLE LANGUAGES")
    print("=" * 60)
    
    english_text = "Hello! Welcome to Natural Language Processing."
    
    languages = {
        'es': 'Spanish',
        'fr': 'French',
        'de': 'German',
        'it': 'Italian',
        'pt': 'Portuguese'
    }
    
    print(f"\nOriginal Text (English): {english_text}\n")
    
    for lang_code, lang_name in languages.items():
        translated = translate_text(english_text, from_lang='en', to_lang=lang_code)
        print(f"{lang_name} ({lang_code}): {translated}")
    
    print()

def bidirectional_translation():
    """Demonstrate translation from English to another language and back."""
    print("=" * 60)
    print("BIDIRECTIONAL TRANSLATION")
    print("=" * 60)
    
    original_text = "Good morning! How are you today?"
    target_lang = 'es'
    
    print(f"\nOriginal Text (English): {original_text}")
    
    # Translate to Spanish
    translated_to_spanish = translate_text(original_text, from_lang='en', to_lang=target_lang)
    print(f"Translated to Spanish: {translated_to_spanish}")
    
    # Translate back to English
    translated_back = translate_text(translated_to_spanish, from_lang=target_lang, to_lang='en')
    print(f"Translated back to English: {translated_back}")
    
    print()

def language_detection_example():
    """Demonstrate language detection."""
    print("=" * 60)
    print("LANGUAGE DETECTION")
    print("=" * 60)
    
    texts = [
        "Hello, how are you?",
        "Bonjour, comment allez-vous?",
        "Hola, ¿cómo estás?",
        "Guten Tag, wie geht es Ihnen?",
        "Ciao, come stai?"
    ]
    
    print("\nDetecting languages of different texts:\n")
    
    for text in texts:
        detected = detect_language(text)
        print(f"Text: {text}")
        print(f"Detected Language: {detected}")
        print("-" * 60)
    
    print()

def translate_common_phrases():
    """Translate common phrases to different languages."""
    print("=" * 60)
    print("COMMON PHRASES TRANSLATION")
    print("=" * 60)
    
    phrases = [
        "Thank you very much",
        "Nice to meet you",
        "Have a great day"
    ]
    
    target_languages = {
        'es': 'Spanish',
        'fr': 'French',
        'de': 'German'
    }
    
    for phrase in phrases:
        print(f"\nEnglish: {phrase}")
        for lang_code, lang_name in target_languages.items():
            translated = translate_text(phrase, from_lang='en', to_lang=lang_code)
            print(f"  {lang_name}: {translated}")
    
    print()

def translate_longer_text():
    """Translate a longer piece of text."""
    print("=" * 60)
    print("LONGER TEXT TRANSLATION")
    print("=" * 60)
    
    text = """Natural Language Processing is a field of artificial intelligence 
    that focuses on the interaction between computers and humans through natural language. 
    The goal is to enable computers to understand, interpret, and generate human language."""
    
    print(f"\nOriginal Text (English):\n{text}")
    
    # Translate to Spanish
    spanish_translation = translate_text(text, from_lang='en', to_lang='es')
    print(f"\nSpanish Translation:\n{spanish_translation}")
    
    # Translate to French
    french_translation = translate_text(text, from_lang='en', to_lang='fr')
    print(f"\nFrench Translation:\n{french_translation}")
    
    print()

def translation_notes():
    """Display important notes about translation."""
    print("=" * 60)
    print("IMPORTANT NOTES ABOUT TRANSLATION")
    print("=" * 60)
    
    print("\n1. TextBlob uses Google Translate API for translation")
    print("2. Internet connection is required for translation to work")
    print("3. Translation quality may vary depending on the complexity of text")
    print("4. Some idioms and cultural references may not translate well")
    print("5. For production use, consider using dedicated translation APIs")
    print("\nCommon Language Codes:")
    print("  en = English, es = Spanish, fr = French, de = German")
    print("  it = Italian, pt = Portuguese, ja = Japanese, zh = Chinese")
    print()

def main():
    """Run all translation examples."""
    print("\n" + "=" * 60)
    print("TEXTBLOB TRANSLATION EXAMPLES")
    print("=" * 60 + "\n")
    
    translation_notes()
    
    print("\nNote: The following examples require an internet connection.\n")
    print("If you see errors, please check your internet connectivity.\n")
    
    # Uncomment the following lines to run actual translation examples
    # These are commented by default to avoid network dependency during testing
    
    # english_to_multiple_languages()
    # bidirectional_translation()
    # language_detection_example()
    # translate_common_phrases()
    # translate_longer_text()
    
    print("=" * 60)
    print("Translation examples completed!")
    print("To run actual translations, uncomment the function calls in main()")
    print("=" * 60)

if __name__ == "__main__":
    main()
