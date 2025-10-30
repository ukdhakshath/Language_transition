from deep_translator import GoogleTranslator

def translate_text(text, target_lang):
    translated_text = GoogleTranslator(source='auto', target=target_lang).translate(text)
    return translated_text

def main():
    text = input("Enter the text you want to translate: ")
    target_lang = input("Enter the target language (e.g., 'fr' for French, 'es' for Spanish): ")
    translated_text = translate_text(text, target_lang)
    print(f"Translated text: {translated_text}")

if __name__ == "__main__":
    main()