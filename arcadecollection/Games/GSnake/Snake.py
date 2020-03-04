from Components.Collider.CircleCollider import *
from Components.Texture.CircleTexture import *
from ObjectsMng.Object import *
from Inputs.SnakeCntrl import *
from Scene.Window import *
#
from copy import *


class Tail(Object):

    def set_geom(self, head, prev_geom, coll = True):
        
        #Компоненты:
        self.coll = self.AddComponent(CCollider(self, CircleCollider(head.radiusTail)))
        self.paint = self.AddComponent(CTexture(head.surface, self, CircleTexture(head.radiusTail)))

        #
        self.geom = prev_geom
        self.coll.collision = coll
        


class Snake(Object):

    #Массив частей хвоста
    arr_tail = []

    #
    Prev = None

    #Состояния змеи
    start = False #Старт игры
    dead = False #Переменная смерти
    spawn = False #Появление змеи на карте
    defualt_Tquantity = 6

    #Количество очков
    score = 0


    #Диспетчер змеи
    def set_snake(self, surface, position):
        #Определяем экран
        self.surface = surface

        #Стартуем в позиции:
        self.start_atPoint(position)

        #
        self.coll.collision = True

        #Запускаем движение
        self.move()

    #Цикл, ведущий хвост за головой змеи
    def tail(self):
        if self.start: #Начинаем создавать хвост при условном "старте" игры
            #Двигаем хвост, если длина его массива соответствует необходимой длине хвоста
            
            if len(self.arr_tail) < self.length_snake:

                self.arr_tail.append(Tail())
                self.arr_tail[len(self.arr_tail) - 1].set_geom(self, deepcopy(self.Prev))
                #

                for i in self.arr_tail:
                    i.paint.Create()
            else:
                for i in range(len(self.arr_tail)):

                    if i == len(self.arr_tail) - 1: #
                        self.arr_tail[i].geom = deepcopy(self.Prev)
                    #
                    else:
                    #
                    #
                        self.arr_tail[i].geom = deepcopy(self.arr_tail[i + 1].geom)


                    self.arr_tail[i].paint.Create()
                


    #Координаты спавна змеи на старте игры
    def start_atPoint(self, position):

        if not self.spawn:
            #Компоненты:
            self.coll = self.AddComponent(CCollider(self, CircleCollider()))
            self.paint = self.AddComponent(CTexture(self.surface, self, CircleTexture()))

            #Устанавливаем радиус головы и хвоста змеи
            self.paint.type.radius = (position.x + position.y) // 36
            self.radiusTail = int(self.paint.type.radius / 2)

            self.coll.type.radius = self.radiusTail


            #Устанавливаем шаг змеи 
            self.step = Vector(self.radiusTail, self.radiusTail) + Vector(15, 15)

            #Устанавливаем координаты змеи
            self.geom.position = position
            
            #Сообщаем о появлении змеи на карте
            self.spawn = True 


    #Движение змеи
    def move(self):

        #Проверяем возможность передвижения
        if not self.dead:

        #Проверяем ось, по которой движется змея
        #И изменяем направления в зависимости от выбранной стороны: 

            #Ось X
            if Input().horizontal():
                self.geom.direction = Vector(Input().check_hor(self.step.x), 0)
            #
            #
            #Ось Y
            if Input().vertical():
                self.geom.direction = Vector(0, Input().check_vert(self.step.y))


            #
            #Сообщаем о старте игры
            if self.geom.direction.x != 0 or self.geom.direction.y != 0:
                #Обозначаем стартовоую длину змеи
                self.length_snake = self.score + self.defualt_Tquantity

                #
                self.start = True
                


            if not self.coll.Collision():
                self.Prev = deepcopy(self.geom)

                self.move_object()
                self.tail()

                self.paint.Create()
            else:
                self.dead = True

            