from ObjectsMng.Vector import *
from Components.Color import *
from Components.Component import *
#
from pygame import *

#Поля для работы с геометрией:
class Geometry:
    position = Vector() #Позиция
    direction = Vector() #Направление


class Object(OInformation):

    #Конструктор!
    def __init__(self):
        #Поле для работы с геометрией объекта
        self.geom = Geometry() 

        #Цвет объекта
        self.color = Red

        #Массив компонентов объекта
        self.Components = []

        #
        self.toArray()


    #Добавление компонента в массив компонентов объекта
    def AddComponent(self, component):
        self.Components.append(component)
        #
        return component

    #
    def CheckComponents(self, copmonent):
        
        for cmp in self.Components:
            if type(cmp) == copmonent:
                return cmp

        return None
    
    #Добавление объекта в "массив объектов"
    def toArray(self):
        OArray.append(self)

    #
    def move_object(self, Invert = False):
        if not Invert:
            self.geom.position += self.geom.direction
            
        else:
            self.geom.position += Vector(-self.geom.direction.x, -self.geom.direction.y)