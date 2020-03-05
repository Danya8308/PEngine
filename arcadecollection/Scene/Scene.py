from Scene.Window import *
#


InScene = []

class Scene:

    start = False

    def Run():
        for obj in InScene:
            if not obj.start:
                obj.Start()
                obj.start = True

            obj.Update()