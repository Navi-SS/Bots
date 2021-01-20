from google_trans_new import google_translator
from urllib.parse import quote
import requests
from io import BytesIO

class TranslateService():

    languages={"spanish":"es","english":"en","russian":"ru","french":"fr","portuguese":"pt",
                "german":"de","italian":"it","ukrainian":"uk","japanese":"ja","chinese":"zh",
                "hindi":"hi","arabic":"ar","bengali":"bn","indonesian":"id"}

    def translate(self,message):
        message=message.split()
        if len(message) >= 3:
            if message[0] in self.languages and message[1] in self.languages:
                input_lang=self.languages[message[0]]
                output_lang=self.languages[message[1]]
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
            voice_uri = f"https://translate.google.com/translate_tts?ie=UTF-8&q={message}&tl={self.languages[language]}-us&client=tw-ob&idx=0"
            res = requests.get(voice_uri,headers={'User-Agent': 'Mozilla/5.0'})
            if res.status_code == 200:
                return BytesIO(res.content)
            return None
        return None
