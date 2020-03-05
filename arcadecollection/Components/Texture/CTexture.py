from Components.Component import *
#

class CTexture(Component):
    
    def __init__(self, obj, Type):
        self.object = obj
        self.type = Type
        #
        InScene.append(self)

    
    def Update(self):
        self.type.Draw(self.object)