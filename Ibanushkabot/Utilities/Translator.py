from google_trans_new import google_translator
from urllib.parse import quote
import requests
from io import BytesIO

class TranslateService():

    languages={"español":"es","ingles":"en","ruso":"ru","frances":"fr","portugues":"pt",
                "aleman":"de","italiano":"it","ucraniano":"uk","japones":"ja","chino":"zh",
                "hindi":"hi","arabe":"ar","bengali":"bn","indonesio":"id"}

    def translate(self,message):
        message=message.split()
        languagein=message[0].lower()
        languageout=message[1].lower()
        if len(message) >= 3:
            if languagein in self.languages and languageout in self.languages:
                input_lang=self.languages[languagein]
                output_lang=self.languages[languageout]
                text=' '.join(message[2:])
                translator = google_translator()
                translate_text = translator.translate(text,lang_src=input_lang,lang_tgt=output_lang)
                return translate_text
            else:
                return None
        else:
            return None
    
    def voice_translate(self,language,message):
        if message is not None:
            message=quote(message)
            voice_uri = f"https://translate.google.com/translate_tts?ie=UTF-8&q={message}&tl={self.languages[language.lower()]}-us&client=tw-ob&idx=0"
            res = requests.get(voice_uri,headers={'User-Agent': 'Mozilla/5.0'})
            if res.status_code == 200:
                return BytesIO(res.content)
            return None
        return None
    
    def all_translate(self,text):
        if text != None:
            detector = google_translator()
            detect_result = detector.detect(text)
            traductions=[]
            for language in self.languages.values():
                traductions.append(detector.translate(text,lang_src=detect_result[0],lang_tgt=language))
            lang_1=f'Español: {traductions[0]}'
            lang_2=f'Ingles: {traductions[1]}'
            lang_3=f'Ruso: {traductions[2]}'
            lang_4=f'Frances: {traductions[3]}'
            lang_5=f'Portugues: {traductions[4]}'
            lang_6=f'Aleman: {traductions[5]}'
            lang_7=f'Italiano: {traductions[6]}'
            lang_8=f'Ucraniano: {traductions[7]}'
            lang_9=f'Japones: {traductions[8]}'
            lang_10=f'Chino: {traductions[9]}'
            lang_11=f'Hindi: {traductions[10]}'
            lang_12=f'Arabe: {traductions[11]}'
            lang_13=f'Bengali: {traductions[12]}'
            lang_14=f'Indonesio: {traductions[13]}'
            return f'{lang_1}\n\n{lang_2}\n\n{lang_3}\n\n{lang_4}\n\n{lang_5}\n\n{lang_6}\n\n{lang_7}\n\n{lang_8}\n\n{lang_9}\n\n{lang_10}\n\n{lang_11}\n\n{lang_12}\n\n{lang_13}\n\n{lang_14}'
        else:
            return None
