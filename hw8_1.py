# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
# «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число,
# месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию
# числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.

class Data:
    def __init__(self, dat):
        self.dat = dat
        Data.val_dat(self.dat)


    @classmethod
    def pars_dat(cls, dat):
        ls = dat.split('-')
        ls = list(map(lambda x: int(x), ls))
        return ls



    @staticmethod
    def val_dat(dat):
        ls = Data.pars_dat(dat)
        if not 0<ls[0]<=31:
            print('вышло за пределы дня', ls)
        elif not 1 <= ls[1] <= 12:
            print('не придумали название для этого месяца', ls)
        elif not 1970 <= ls[2] <= 2323:
            print('год не тот', ls)


v = Data('01-04-1224')
c = Data('01-04-1999')
print(c)




