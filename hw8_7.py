# 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число». Реализуйте перегрузку
# методов сложения и умножения комплексных чисел. Проверьте работу проекта. Для этого создаёте экземпляры класса
# (комплексные числа), выполните сложение и умножение созданных экземпляров. Проверьте корректность полученного
# результата.


class MyIm:
    def __init__(self, v, m):
        self.v = v
        self.m = m

    def __str__(self):
        return f"{self.v} + {self.m}*i"

    def __mul__(self, other):
        return MyIm(self.v+ other.v , self.m + + other.m)

    def __add__(self, other):
        return MyIm((self.v * other.v - self.m * other.m), (self.v*other.m + self.m*other.v))

a = MyIm(3,4)
print(a)
b = MyIm(8,1)
print(a+b)
print(a*b)