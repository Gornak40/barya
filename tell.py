from gtts import gTTS
from os import system
from pygame import mixer, quit as pyquit
from time import time


class Speaker:
    def __init__(self):
        mixer.init()
        
    def speak(self, text, lang='ru'):
        t = time()
        myobj = gTTS(text=text, lang=lang, slow=False)
        myobj.save('.mp3')
        mixer.music.load('.mp3')
        mixer.music.set_volume(1)
        print(time() - t)
        mixer.music.play()
    
    def __del__(self):
        pyquit()

