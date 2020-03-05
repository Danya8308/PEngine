from Components.Texture.CTexture import *
#

class SquareTexture:
    
    def __init__(self, size = Vector(0, 0)):
        self.size = size
        

    #Создаем квадрат
    def Draw(self, obj, width, height):
        draw.rect(Window.Surface, self.obj.color,
                  (self.obj.geom.position.x, self.obj.geom.position.y,
                   width, height))


