from Components.Collider.CCollider import *
#

class CircleCollider:
    
    def __init__(self, radius = 0):
        self.radius = radius #радиус коллайдера
         

    #Ищем все точки данного объекта в World
    def FindPoint(self, obj, point):

        #Начинаем считать точки по тому же принцепу, что и в квадрате: с верхней левой точки
        begin_point = obj.geom.position + Vector(-self.radius, -self.radius)
        centre = obj.geom.position #Центр окружности

        #Проверяем, находится ли точка в окружности
        for point_x in range(begin_point.x, begin_point.x + self.radius * 2 + 1):
            for point_y in range(begin_point.y, begin_point.y + self.radius * 2 + 1):

                #Супер классная формула кто ее не знает тот канешь капец))0)
                if (centre.x - point_x) ** 2 + (centre.y - point_y) ** 2 <= self.radius ** 2:                    
                    point.add((point_x, point_y))

        return point