from Components.Component import *
#

class CTexture(Component):
    
    def __init__(self, surface, obj, Type):
        self.surface = surface
        self.object = obj
        self.type = Type

    
    def Create(self):
        self.type.Create(self.surface, self.object)