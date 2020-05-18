from pymorphy2 import MorphAnalyzer
from dic import *
from tell import Speaker
from threading import Thread


def post(s):
    print('[{}]'.format(s.capitalize()))


M = MorphAnalyzer()
S = Speaker()


def normalWord(s):
    return M.parse(s)[0].normal_form


def normal(text):
    ntext = [normalWord(s) for s in text.split()]
    return ntext


def execute(*nor):
    nor = list(nor)
    if 'бар' not in nor and 'барри' not in nor:
        return
    for com in nor:
        if com in dic:
            Thread(target=dic[com][1]).start()
            S.speak(dic[com][0])
            return
            
