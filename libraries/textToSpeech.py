from gtts import gTTS
from io import BytesIO

class TextToSpeech:
    def convertTextToSpeech(self, text: str):
        try:
            mp3_fp = BytesIO()
            tts = gTTS(text, lang='en')
            tts.write_to_fp(mp3_fp)
            mp3_fp.seek(0)
            return mp3_fp
        except ConnectionError as e:
            raise ConnectionError(f"Unable to connect to the internet {e}")
        except Exception as e:
            raise ConnectionError(f"Error occured while trying to do tts {e}")
                