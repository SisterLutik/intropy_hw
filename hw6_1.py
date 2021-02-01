# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый,
# зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего
# (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном порядке
# (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
from time import sleep
from tkinter import *
from itertools import cycle
from tkinter import Tk



    #root.after(2000, change_color)


class TrafficLight:
        __color = cycle(['red', 'yellow', 'green', 'yellow'])
        __t = cycle([7, 2, 3, 2])
        def __init__(self):
            self.root: Tk = Tk()
            self.root.title("Светофор")

        def running(self):
            self.change_color(self.root, self.__color, self.__t)
            self.root.mainloop()
        def change_color(self, root, color, t):
            self.root['bg'] = (next(color))
            self.root.update()
            sleep(next(t))
            self.change_color(root, color, t)


mt = TrafficLight()
mt.running()
