from SystemMethods.StartUpdate import *
#
from pygame import *

class Window(StartUpdate):

    #
    Width = 0
    Height = 0

    #
    Surface = display.set_mode((0, 0))

    #
    #Конструктор
    def __init__(self, width = 0, height = 0):
        Window.Width = width
        Window.Height = height
    

    #
    def Update(self):
        self.openWin()


    #Проверка на событие QUIT
    def Stop():
        for i in event.get():
            if i.type == QUIT:
                return True
            #
        return False


    #Метод открытия окна
    def openWin(self):
        init()
        #
        Window.Surface = display.set_mode((Window.Width,
                                          Window.Height))


    #Метод, закрывающий окно
    def Exit(self):
        quit()