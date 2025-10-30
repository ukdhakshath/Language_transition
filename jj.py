from deep_translator import GoogleTranslator
from langdetect import detect
import pyperclip
import gtts
import os
import time

# Kannada language support
SUPPORTED_LANGUAGES = {
    'kn': 'Kannada',
    'en': 'English',
    'hi': 'Hindi',
    'ta': 'Tamil',
    'te': 'Telugu',
    'ml': 'Malayalam'
}

def detect_language(text):
    """Detect input language automatically"""
    try:
        return detect(text)
    except:
        return "Unknown"

def translate_to_kannada(text, source_lang='auto'):
    """Specialized Kannada translation function"""
    try:
        return GoogleTranslator(source=source_lang, target='kn').translate(text)
    except Exception as e:
        return f"Translation error: {str(e)}"

def text_to_speech(text, language='kn'):
    """Convert translated text to speech"""
    try:
        tts = gtts.gTTS(text, lang=language)
        tts.save("kannada_audio.mp3")
        os.system("start kannada_audio.mp3")  # Works on Windows
        return "Playing audio..."
    except Exception as e:
        return f"Audio error: {str(e)}"

def main():
    print("\n=== ಕನ್ನಡ ಭಾಷಾ ಅನುವಾದಕ (Kannada Language Translator) ===")
    print("Supported languages:")
    for code, name in SUPPORTED_LANGUAGES.items():
        print(f"{code} - {name}")

    while True:
        print("\nOptions:")
        print("1. Translate to Kannada")
        print("2. Translate from Kannada")
        print("3. Detect language")
        print("4. Speak Kannada translation")
        print("5. Copy to clipboard")
        print("6. Exit")

        choice = input("\nChoose an option (1-6): ").strip()

        if choice == "1":
            text = input("\nEnter text to translate to Kannada: ").strip()
            if not text:
                print("Please enter some text")
                continue

            # Auto-detect source language
            source_lang = detect_language(text)
            if source_lang in SUPPORTED_LANGUAGES:
                print(f"Detected language: {SUPPORTED_LANGUAGES.get(source_lang)}")
            else:
                print("Could not detect language, using auto-translate")

            translated = translate_to_kannada(text, source_lang)
            print(f"\nಕನ್ನಡ ಅನುವಾದ (Kannada Translation): {translated}")

        elif choice == "2":
            text = input("\nEnter Kannada text to translate: ").strip()
            if not text:
                print("Please enter some Kannada text")
                continue

            target_lang = input("Enter target language code: ").strip().lower()
            if target_lang not in SUPPORTED_LANGUAGES:
                print("Unsupported language")
                continue

            translated = GoogleTranslator(source='kn', target=target_lang).translate(text)
            print(f"\nTranslation: {translated}")

        elif choice == "3":
            text = input("\nEnter text to detect language: ").strip()
            if not text:
                print("Please enter some text")
                continue

            lang_code = detect_language(text)
            lang_name = SUPPORTED_LANGUAGES.get(lang_code, "Unknown")
            print(f"\nDetected language: {lang_code} ({lang_name})")

        elif choice == "4":
            if 'translated' not in locals():
                print("First translate some text to Kannada")
                continue
            print(text_to_speech(translated))

        elif choice == "5":
            if 'translated' not in locals():
                print("Nothing to copy")
                continue
            pyperclip.copy(translated)
            print("Kannada translation copied to clipboard!")

        elif choice == "6":
            print("ನಿಮ್ಮನ್ನು ನೋಡಿಕೊಳ್ಳಿ! (Goodbye!)")
            break

        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()