from Components.Collider.CircleCollider import *
from Components.Texture.CircleTexture import *
from ObjectsMng.Object import *
from Inputs.SnakeCntrl import *
from Scene.Window import *
#
from copy import *


class Tail(Object):

    def set(self, head, prev_geom):

        #Компоненты:
        self.coll = self.AddComponent(CCollider(self, CircleCollider(head.radiusTail)))
        self.paint = self.AddComponent(CTexture(self, CircleTexture(head.radiusTail)))

        #
        self.geom = prev_geom
        self.coll.collision = True


class Snake(Object):

    #Массив частей хвоста
    arr_tail = []

    #
    Prev = None

    #Состояния змеи
    dead = False #Переменная смерти
    begin = False #Появление змеи на карте
    defualt_Tquantity = 6

    #Количество очков
    score = 0

    #
    def Start(self):
        #Компоненты:
        self.coll = self.AddComponent(CCollider(self, CircleCollider()))
        self.paint = self.AddComponent(CTexture(self, CircleTexture()))

        #Стартуем в позиции:
        self.start_atPoint(Vector(Window.Width // 2,
                                  Window.Height // 2))

        #
        self.coll.collision = True


    #Основной цикл:
    def Update(self):
        #Запускаем движение
        self.move()


    #Координаты спавна змеи на старте игры
    def start_atPoint(self, position):

        #Устанавливаем радиус головы и хвоста змеи
        self.paint.type.radius = (position.x + position.y) // 36
        self.radiusTail = int(self.paint.type.radius / 2)

        self.coll.type.radius = self.radiusTail
        
        #Устанавливаем шаг змеи 
        self.step = Vector(self.radiusTail * 2, self.radiusTail * 2) + Vector(1, 1)

        #Устанавливаем координаты змеи
        self.geom.position = position

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
                self.begin = True


            if not self.coll.Collision():
                self.Prev = deepcopy(self.geom)

                self.move_object()
                self.tail()

            else:
                self.dead = True


    #Цикл, ведущий хвост за головой змеи
    def tail(self):
        if self.begin: #Начинаем создавать хвост при условном "старте" игры
            #Двигаем хвост, если длина его массива соответствует необходимой длине хвоста
            
            if len(self.arr_tail) < self.length_snake:
                self.arr_tail.append(Tail())
                self.arr_tail[-1].set(self, deepcopy(self.Prev))

            else:
                for i in range(len(self.arr_tail)):

                    if i == len(self.arr_tail) - 1: #
                        self.arr_tail[i].geom = deepcopy(self.Prev)
                    #
                    else:
                    #
                    #
                        self.arr_tail[i].geom = deepcopy(self.arr_tail[i + 1].geom)