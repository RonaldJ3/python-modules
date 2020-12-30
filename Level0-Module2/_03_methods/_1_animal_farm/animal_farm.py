from tkinter import simpledialog, Tk

from playsound import playsound
from PIL import Image


def animals():
    window = Tk()
    window.withdraw()

    # TODO 1.Ask the user which animal they want, then see and
    #  hear the animal they chose using one of the methods below.

    # TODO 2. Make it so that the user can keep entering new animals.


def moo():
    # playsound('cow.wav')
    im = Image.open("cow.jpg")
    im.show()


def quack():
    # playsound('duck.wav')
    im = Image.open("duck.jpg")
    im.show()


def woof():
    # playsound('dog.wav')
    im = Image.open("dog.jpg")
    im.show()


def meow():
    # playsound('meow.wav')
    im = Image.open("cat.jpg")
    im.show()


def llamascream():
    # playsound('llama.wav')
    im = Image.open("llama.jpg")
    im.show()


if __name__ == '__main__':
    animals()