from gtts import gTTS
from os import system
from mpg123 import Mpg123


class Speaker:
    def speak(self, text, lang='ru'):
        speaker = gTTS(text=text, lang=lang, slow=False)
        print('Saving')
        speaker.save('.mp3')
        print('Playing')
        system('mpg123 .mp3')


Speaker().speak('идите нахуй, мудилы, сосите член, матери ваши конченные, аааааа')