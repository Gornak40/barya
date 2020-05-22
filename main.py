#!/bin/python3
from recognize import *
from os import system


def main():
    R = Recognizer('_model')
    system('clear')
    R.start()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print()
        post('Пока')
