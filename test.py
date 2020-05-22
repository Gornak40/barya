from vosk import Model, KaldiRecognizer
from os import path
from pyaudio import PyAudio, paInt16
# https://github.com/alphacep/vosk-api/blob/master/doc/models.md

P = PyAudio()
stream = P.open(format=paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
stream.start_stream()
model = Model('_model')
rec = KaldiRecognizer(model, 16000)

print('Привет, я Баря!')

while True:
    data = stream.read(2000)
    if not len(data):
        break
    if rec.AcceptWaveform(data):
        text = eval(rec.Result())
        if text.get('text'):
            print(text.get('text'))
#     else:
#         text = eval(rec.PartialResult())
#         if text.get('partial'):
#             print(text['partial'])

#print(rec.FinalResult())
