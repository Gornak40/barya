import webbrowser
from requests import get
from os import system


def browser(url):
    system('yandex-browser-beta {} > /dev/null 2>&1'.format(url))


def post(s):
    print('[{}]'.format(s.capitalize()))


def Bround():
    browser('https://codeforces.com/contests')


def do_nothing():
    return


def Byandex():
    browser('https://yandex.ru')


def Bdnevnik():
    browser('https://dnevnik.mos.ru/student_diary/student_diary/15362958')


def BMavrin():
    browser('https://www.youtube.com/user/pavelmavrin/videos')


def Bclean():
    system('clear')


def Bupdate():
    system('clear')
    system('sudo apt update -y')
    system('sudo apt upgrade -y')
    system('sudo apt autoremove -y')


def Bexit():
    post('Пока')
    exit()


dic = {
    'раунд': ('открываю раунд', Bround),
    'спасибо': ('пожалуйста', do_nothing),
    'привет': ('привет', do_nothing),
    'яндекс': ('открываю яндекс', Byandex),
    'дневник': ('открываю дневник', Bdnevnik),
    'павел': ('открываю канал Павла Маврина', BMavrin),
    'молодец': ('всегда рада помочь', do_nothing),
    'очистить': ('логи чисты', Bclean),
    'обновить': ('обновляю систему', Bupdate),
    'пока': ('пока', Bexit)
    }
