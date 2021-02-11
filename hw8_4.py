# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
# уникальные для каждого типа оргтехники.
# 5. Продолжить работу над первым заданием. Разработайте методы, которые отвечают за приём оргтехники на склад и
# передачу в определённое подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру (например, словарь).
# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например, для
# указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.

class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt

class Sklad:
    def __init__(self):
        self.place = {"Сканер крутанский": 2, "Принтер БеларусьТрактор": 8}
        self.dis = {"Сканер крутанский": "цветной испанский", "Принтер БеларусьТрактор": "синий"}
    def __str__(self):
        numbers = [str(i) for i in range(len(self.place))]
        zipped = dict(zip(numbers, self.dis))
        for key, values in zipped.items():
            print(f'{key}. {values}')
        print("Выберете технику из списка, написав номер, получите описание:")
        o = input()
        if zipped.get(o) != None:
            return f'{zipped.get(o)} - {self.dis.get(zipped.get(o))} '
        else:
            return 'Пустота'

    def set(self, org):
        if self.place.get(org.model) == None:
            self.place[org.model] = org.q
        else:
            #self.place.get(org.model) = self.place.get(org.model) + org.q
            self.dis[org.model] = org.full

    def get(self):
        try:
            numbers = [str(i) for i in range(len(self.place))]
            zipped = dict(zip(numbers, self.place))
            print("Выберете технику из списка, написав номер:")
            for key,values in zipped.items():
                print(f'{key}. {values}')
            o = input()
            if zipped.get(o) !=None:
                print(f'{zipped.get(o)} - {self.place.get(zipped.get(o))} шт. на складе')
                qq = int(input(f'Сколько надо? '))
                if qq > self.place.get(zipped.get(o)):
                    print(f'Это слишком много... даем {self.place.get(zipped.get(o))}')
                    qq = {self.place.get(zipped.get(o))}
                if qq == {self.place.get(zipped.get(o))}:
                    del self.place[zipped.get(o)]
                else:
                    self.place[zipped.get(o)] = (self.place.get(zipped.get(o)) - qq)
            else:
                raise OwnError('Мы не нашли ничего такого')
        except ValueError:
            print("Вы ввели не число. Не даем ничего")
        except OwnError as err:
            print(err)

class Org_tex:
    def __init__(self, name, q, color):
        self.q = Org_tex.val_dit('Введите кооректное колличество ', q)
        self.name = name
        self.color = 'цветной' if Org_tex.val_12('Некорректный тип: цветной -1, ч/б -2: ', color) == 1 else'ч/б'
        self.full = [self.color]

    def __str__(self):
        return f"{self.model} {self.full}: {self.q} шт."


    @classmethod
    def val_dit(cls, st, d):
        d = str(d)
        while not d.isdigit():
            d = input(st)
        return int(d)

    @classmethod
    def val_12(cls,st, d):
        v = [1,2]
        d = int(d) if d.isdigit() else d
        while d not in v:
            d = input(st)
            d = int(d) if d.isdigit() else d

        return d


class Printr(Org_tex):
    def __init__(self, name, q, color, laz):
        super().__init__(name, q, color )
        self.laz = 'лазерный' if Org_tex.val_12('Некооректный ввод: лазерный -1, струйный -2: ', laz) == 1 else 'струйный'
        self.model = f'Принтер {self.name}'
        self.full = self.color +', '+ self.laz

class Scan(Org_tex):
    def __init__(self, name, q, color, form):
        super().__init__(name, q, color )
        self.form = "A" + Scan.val_15(form)
        self.model = f'Сканер {self.name}'
        self.full = [self.color, self.form]

    @classmethod
    def val_15(cls, d):
        v = [1,2,3,4]
        d = int(d) if d.isdigit() else d
        while d not in v:
            d = input('Введите формат от 1 до 4 ')
            d = int(d) if d.isdigit() else d
        return d
class Kser(Org_tex):
    def __init__(self, name, q, color, comp):
        super().__init__(name, q, color)
        self.comp = 'с подключение' if Org_tex.val_12('Некооректный ввод: с подключение к компу -1, без -2: ',comp)  == 1 else 'стационарный'
        self.model = f'Ксерокс {self.name}'
        self.full = [self.color, self.comp]

m=0
s = Sklad()
val_vid = ['1','2','3']
while m != 'q':
    m = int(input(
        'Введите цифру, чтобы: 1 - добавить технику, 2 - смотреть склад и описание техники, 3 - взять технику, q - выход '))
    if m == 1:
        try:
            t = input('Введите вид техники: 1 - Принтер, 2 - Сканер, 3 - Ксерокс')
            if t not in val_vid:
                raise OwnError("Не то значение вида техники (от 1 до 3)")
        except OwnError as err:
            print(err)
        else:
            name = input('Введите имя модели ')
            q = input('Введите колличество ')
            color = input('1 - цветной, 2 - ч/б ')
            if t == '1':
                laz =input('1 - лазерный, 2 - струйный ')
                t_obj = Printr(name, q, color, laz)
            elif t == '2':
                f =input('Введите форма листа А (от 1 до 4) ')
                t_obj = Scan(name, q, color, f)
            else:
                comp = input('1 - с подключением к компу, 2 - стационарный ')
                t_obj = Kser(name, q, color, comp)
            s.set(t_obj)
    elif m == 2:
        print(s)
    elif m == 3:
        s.get()
