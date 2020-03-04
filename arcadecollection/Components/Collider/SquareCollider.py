from Components.Collider.CCollider import *
#

class SquareCollider:
    
    def __init__(self, vector = Vector(0, 0)):
        self.size = vector #размер коллайдера


    #Ищем все точки данного объекта в World
    def FindPoint(self, obj, point):

        for x in range(obj.geom.position.x, obj.geom.position.x + self.size.x + 1):
            for y in range(obj.geom.position.y, obj.geom.position.y + self.size.y + 1):
                point.add((x, y))

        return point


