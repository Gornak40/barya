# https://github.com/alphacep/vosk-api/blob/master/doc/models.md
from vosk import Model, KaldiRecognizer
from pyaudio import PyAudio, paInt16
from terminal import *


def post(s):
    print('[{}]'.format(s))


class Recognizer:
    def __init__(self, name='_model'):
        self.P = PyAudio()
        self.stream = self.P.open(format=paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
        self.stream.start_stream()
        self.model = Model(name)
        self.rec = KaldiRecognizer(self.model, 16000)
        post('Мои уши готовы')
        
    def start(self):
        post('Внимательно вас слушаю')
        while True:
            data = self.stream.read(2000)
            if not len(data):
                break
            if self.rec.AcceptWaveform(data):
                text = eval(self.rec.Result())
                if text.get('text'):
                    print('[Вы]', text.get('text'))
                    print('[Команды]', *normal(text.get('text')))
