import os
import uuid


class Tools:
    def __int__(self):
        pass

    def text_to_speech(self, text):
        file_path = None
        try:
            import gtts
            from gtts import gTTS

            language = 'en'
            obj = gTTS(text=text, lang=language, slow=False)

            filename = f"{str(uuid.uuid4())}.mp3"
            folder = 'media/speech_files'
            try:
                os.mkdir(folder)
            except:
                pass
            obj.save(f"{folder}/{filename}")
            file_path = f"{folder}/{filename}"
        except Exception as e:
            pass

        return file_path