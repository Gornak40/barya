from pymorphy2 import MorphAnalyzer


M = MorphAnalyzer()


def normalWord(s):
    return M.parse(s)[0].normal_form


def normal(text):
    ntext = [normalWord(s) for s in text.split()]
    return ntext