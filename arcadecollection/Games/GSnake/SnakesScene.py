from Games.GSnake.Snake import *
#


class SnakeScene:
    
    InScene.append(Window(1240, 800))
    InScene.append(Snake())


    #Основной цикл сессии Snake
    def snakeLoop(self):
        while not(Window.Stop()):
            time.delay(100)

            Scene.Run()

            #Обновляем экран
            display.update()


SnakeScene().snakeLoop()