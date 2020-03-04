from Components.Texture.CTexture import *
#

class CircleTexture:
    
    def __init__(self, radius = 0):
        self.radius = radius


    #Создаем круг
    def Draw(self, surface, obj):
        draw.circle(surface, obj.color, (obj.geom.position.x, obj.geom.position.y), self.radius)