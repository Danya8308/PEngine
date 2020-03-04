from Components.Texture.CTexture import *
#

class SquareTexture:
    
    def __init__(self, size = Vector(0, 0)):
        self.size = size
        

    #Создаем квадрат
    def Create(self, surface, obj, width, height):
        draw.rect(surface, self.obj.color,
                  (self.obj.geom.position.x, self.obj.geom.position.y,
                   width, height))


