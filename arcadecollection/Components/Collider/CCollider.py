from Components.Component import *
#


class CCollider(Component):

    def __init__(self, obj, Type):
        #Состояния:
        self.collision = False
        self.trigger = False

        #
        self.object = obj

        #Тип коллайдера
        self.type = Type 

        #Коллайдер внутреннего объекта
        self.inner_coll = None

    #
    def Point(self):
        point = set()
        return self.type.FindPoint(self.object, point)

    #Проверка на вхождение в объект
    def Inside(self):

        for obj in OArray:
            if not(obj is self.object):
                self.inner_coll = obj.CheckComponents(CCollider)
                #
                #
                if self.inner_coll != None:
                    if self.Point().intersection(self.inner_coll.Point()) != set():                        
                        return obj
            #
            #
        return None
    
    #Проверка на столкновение
    def Collision(self):
        self.coll_obj = self.Inside()

        if self.coll_obj != None:
            if self.collision and self.inner_coll.collision:
                if self.collision and self.inner_coll.collision:
                    return True
                #
                #
        return False 


    #Проверка на триггер
    def Trigger(self):
        self.trig_obj = self.Inside()

        if self.trig_obj != None:
            if self.trigger and self.trig_obj.coll.trigger:
                if self.type.coll.trigger and self.trig_obj.coll.trigger:
                    return True
                #
                #
        return False