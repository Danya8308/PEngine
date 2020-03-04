#from Games.GSnake.SnakeManager import *
from ObjectsMng.Object import *
from Components.Collider.SquareCollider import *


class a(Object):

    def foo(self):
        self.coll = self.AddComponent(CCollider(self, SquareCollider(Vector(10, 10))))


    

class b(Object):

    def foo(self):
        self.coll = self.AddComponent(CCollider(self, SquareCollider(Vector(20, 20))))


A = a()
B = b()

A.foo()
B.foo()

A.coll.collision = True
B.coll.collision = True

A.geom.position = Vector(100, 100)
B.geom.position = Vector(110, 100)



if A.coll.Collision():
    print('Усе робит')