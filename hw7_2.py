# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого
# проекта — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V
# и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма
# (2 * H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать
# абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod

class Dress(ABC):


    @property
    @abstractmethod
    def sum(self):
        pass

    def __add__(self, other):
        return self.sum + over.sum


class Coat(Dress):

    def __init__(self, v):
        self.v = v

    @property
    def v(self):
      return self.__v

    @v.setter
    def v(self, v):
        if (v > 0):
          self.__v = v
        else:
            print('Не можем разобрать размер, но на глаз 48')
            self.__v = 48
    def sum(self):
      return round((self.v / 6.5) + 0.5,2)

class Suit(Dress):
    def __init__(self, h):
        self.h = h

    @property
    def h(self):
      return self.__h

    @h.setter
    def h(self,h):
        if ((type(h) == int) or (type(h) == float)) and (100 < h < 211):
          self.__h= h
        else:
            print('Не можем разобрать рост, но на глаз 165')
            self.__h = 165
    def sum(self):
        return round(2 * self.h + 0.3,2)
c = Coat(45)
s = Suit(122)
print(c.sum()+s.sum())
c1 = Coat(-45)
s1 = Suit(100)
print(c1.sum()+s1.sum())