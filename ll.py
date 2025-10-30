from deep_translator import GoogleTranslator
import pyperclip
import gtts
import os

class KannadaTranslator:
    def __init__(self):
        self.supported_langs = {
            'en': 'ಇಂಗ್ಲಿಷ್',
            'hi': 'ಹಿಂದಿ',
            'ta': 'ತಮಿಳು',
            'te': 'ತೆಲುಗು',
            'ml': 'ಮಲಯಾಳಂ'
        }
    
    def translate_to_kannada(self, text):
        """ಇತರ ಭಾಷೆಗಳಿಂದ ಕನ್ನಡಕ್ಕೆ ಅನುವಾದಿಸಿ"""
        try:
            return GoogleTranslator(source='auto', target='kn').translate(text)
        except Exception as e:
            return f"ದೋಷ: {str(e)}"
    
    def translate_from_kannada(self, text, target_lang):
        """ಕನ್ನಡದಿಂದ ಇತರ ಭಾಷೆಗಳಿಗೆ ಅನುವಾದಿಸಿ"""
        try:
            return GoogleTranslator(source='kn', target=target_lang).translate(text)
        except Exception as e:
            return f"ದೋಷ: {str(e)}"
    
    def speak_kannada(self, text):
        """ಕನ್ನಡ ಪಠ್ಯವನ್ನು ಧ್ವನಿಯಲ್ಲಿ ಪ್ಲೇ ಮಾಡಿ"""
        try:
            tts = gtts.gTTS(text, lang='kn')
            tts.save("kannada_voice.mp3")
            os.system("start kannada_voice.mp3")  # Windows
            return "ಧ್ವನಿ ಚಾಲನೆಯಲ್ಲಿದೆ..."
        except Exception as e:
            return f"ಧ್ವನಿ ದೋಷ: {str(e)}"
    
    def start_chat(self):
        print("\nನಮಸ್ಕಾರ! ಕನ್ನಡ ಅನುವಾದ ಚಾಟ್ಬಾಟ್ಗೆ ಸುಸ್ವಾಗತ!")
        print("ನಾನು ಇವುಗಳನ್ನು ಮಾಡಬಲ್ಲೆ:")
        print("1. ಇತರ ಭಾಷೆಗಳಿಂದ ಕನ್ನಡಕ್ಕೆ ಅನುವಾದಿಸಿ")
        print("2. ಕನ್ನಡದಿಂದ ಇತರ ಭಾಷೆಗಳಿಗೆ ಅನುವಾದಿಸಿ")
        print("3. ಕನ್ನಡದಲ್ಲಿ ಮಾತನಾಡಿ (ಟೆಕ್ಸ್ಟ್-ಟು-ಸ್ಪೀಚ್)")
        print("4. ನಕಲು ಮಾಡಿ (ಕ್ಲಿಪ್ಬೋರ್ಡ್)")
        print("5. ನಿರ್ಗಮನ")
        
        while True:
            choice = input("\nನಿಮ್ಮ ಆಯ್ಕೆ (1-5) ತಿಳಿಸಿ: ").strip()
            
            if choice == "1":
                text = input("\nದಯವಿಟ್ಟು ಅನುವಾದಿಸಲು ಪಠ್ಯವನ್ನು ನಮೂದಿಸಿ: ")
                if not text:
                    print("ದಯವಿಟ್ಟು ಕೆಲವು ಪಠ್ಯವನ್ನು ನಮೂದಿಸಿ")
                    continue
                
                translated = self.translate_to_kannada(text)
                print(f"\nಕನ್ನಡ ಅನುವಾದ: {translated}")
                self.current_translation = translated
            
            elif choice == "2":
                text = input("\nದಯವಿಟ್ಟು ಕನ್ನಡ ಪಠ್ಯವನ್ನು ನಮೂದಿಸಿ: ")
                if not text:
                    print("ದಯವಿಟ್ಟು ಕೆಲವು ಕನ್ನಡ ಪಠ್ಯವನ್ನು ನಮೂದಿಸಿ")
                    continue
                
                print("\nಲಭ್ಯವಿರುವ ಭಾಷೆಗಳು:")
                for code, name in self.supported_langs.items():
                    print(f"{code} - {name}")
                
                target_lang = input("ಗಮ್ಯಸ್ಥಾನ ಭಾಷೆಯ ಕೋಡ್ ನಮೂದಿಸಿ (ಉದಾ: 'en'): ")
                if target_lang not in self.supported_langs:
                    print("ಅಸಮರ್ಥ ಭಾಷೆ")
                    continue
                
                translated = self.translate_from_kannada(text, target_lang)
                print(f"\nಅನುವಾದ: {translated}")
                self.current_translation = translated
            
            elif choice == "3":
                if not hasattr(self, 'current_translation'):
                    print("ಮೊದಲು ಕನ್ನಡಕ್ಕೆ ಅನುವಾದಿಸಿ")
                    continue
                print(self.speak_kannada(self.current_translation))
            
            elif choice == "4":
                if not hasattr(self, 'current_translation'):
                    print("ನಕಲು ಮಾಡಲು ಏನೂ ಇಲ್ಲ")
                    continue
                pyperclip.copy(self.current_translation)
                print("ಕನ್ನಡ ಅನುವಾದವನ್ನು ಕ್ಲಿಪ್ಬೋರ್ಡ್ಗೆ ನಕಲು ಮಾಡಲಾಗಿದೆ!")
            
            elif choice == "5":
                print("ಧನ್ಯವಾದಗಳು! ಮತ್ತೆ ಭೇಟಿ ಮಾಡೋಣ!")
                break
            
            else:
                print("ಅಮಾನ್ಯ ಆಯ್ಕೆ, ದಯವಿಟ್ಟು ಮತ್ತೆ ಪ್ರಯತ್ನಿಸಿ")

if __name__ == "__main__":
    translator = KannadaTranslator()
    translator.start_chat()