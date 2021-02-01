# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (
# булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
# повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый
# класс метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar
# переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться
# сообщение о превышении скорости. Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к
# атрибутам, выведите результат. Выполните вызов методов и также покажите результат.
import random
from itertools import cycle
import random
from time import sleep

class Car:
        speed =  5
        color = 'red'
        name = 'tesla'
        is_police = False

        def go(self):
            print('Go ', self.name)
        def stop(self):
            print('Stop ', self.name)
        def turn(self, direction):
            print('Turn ', direction,' ', self.name)
        def show_speed(self):
            print(self.speed,' ', 'км/ч у ', self.name)

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print('Привышение скорости на ', self.speed - 40, 'км/ч у ', self.name)
        else:
            print(self.speed, 'км/ч у ', ' ', self.name)
class SportCar(Car):
    pass
class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print('Привышение скорости на ', self.speed - 40, 'км/ч у ', self.name)
        else:
            print(self.speed, ' ', 'км/ч у ', self.name)
class PoliceCar(Car):
    is_police = True

def randturn():
    a = random.randint(0, 1)
    if a == 1:
        return 'left'
    else:
        return 'right'

def changespeed():
    return random.randint(0,310)

def action(car):
    a = random.randint(1,4)
    if a ==1:
        car.speed = changespeed()
        car.show_speed()
    elif a == 2:
        car.turn(randturn())
    elif a == 3:
        car.go()
    else:
        car.stop()

def change(car):
    action(next(car))
    sleep(1)
    change(car)

car1 = TownCar()
car1.name = 'Valera'
car2 = SportCar()
car2.name = 'Mersedes'
car3 = WorkCar()
car3.color = 'blue'
car3.name = 'tractor'
car4 = PoliceCar()

beebee = cycle([car1, car2, car2, car4])
change(beebee)
