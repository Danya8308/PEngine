from Scene.Scene import *
from SystemMethods.StartUpdate import *
from ObjectsMng.Vector import * 
#
from pygame import *
from copy import *


#Массив всех созданных объектов
OArray = []

class OArrayTag:

    #В планах (:
    def __init__(self, tag, number):
        for obj in OArray:
            if obj.tag == tag:
                pass



class OInformation(StartUpdate):

    #Тэг объекта
    tag = 'Object'