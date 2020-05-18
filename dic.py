import webbrowser
from requests import get


def Bround():
    webbrowser.open('https://codeforces.com/contests')


def do_nothing():
    return


def Byandex():
    webbrowser.open('https://yandex.ru')


def Bdnevnik():
    webbrowser.open('https://dnevnik.mos.ru/student_diary/student_diary/15362958')


dic = {
    'раунд': ('открываю раунд', Bround),
    'спасибо': ('пожалуйста', do_nothing),
    'привет': ('привет', do_nothing),
    'яндекс': ('открываю яндекс', Byandex),
    'дневник': ('открываю дневник', Bdnevnik)
    }
