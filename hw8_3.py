# 3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список.
# Класс-исключение должен контролировать типы данных элементов списка.
# примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу
# скрипта, введя, например, команду “stop”. При этом скрипт завершается, сформированный список выводится на экран.
# Подсказка: для данного задания примем, что пользователь может вводить только числа и строки. При вводе пользователем
# очередного элемента необходимо реализовать проверку типа элемента и вносить его в список, только если введено число.
# Класс-исключение должен не позволить пользователю ввести текст (не число) и отобразить соответствующее сообщение.
# При этом работа скрипта не должна завершаться.



class DitError(Exception):
    def __init__(self, txt):
        self.stop = False
        self.applist = ''
        self.txt = txt

    def start(self, dit):

        self.dit = dit
        ld = DitError.rec_dit(self.dit)
        self.applist = ''

        if ld[0] == 'Числа на эльфийском: ':
            txt = ''.join(ld)
            raise DitError(txt)


        else:
            if ld == 'q':
                self.stop = True

            else:
                self.applist = ld




    @classmethod
    def val_dit(cls, dit):
        str_val = dit.replace(".", "")
        str_val = str_val.replace("-", "")
        str_val = str_val.split()
        str_val = [s for s in str_val if not s.isdigit()]

        if str_val:
            for el in str_val:
                if el == 'q':
                    return 'q'

            str_val = ['Числа на эльфийском: '] + str_val
            return str_val
        else:
            ls = dit.split()
            ls = list(map(lambda x: float(x), ls))
            return ls

    @staticmethod
    def rec_dit(dit):
        ls = DitError.val_dit(dit)
        return ls



print(
    "Введите строку чисел, разделенных пробелом. Знак минус вводите вместе с отрицательным числом. Дробное вводите через точку. \nПри нажатии Enter последовательность сохраняется. При вводе q - завершение без записи строки q содержащей"
    "(сперва выводится сохраненка)")

d = DitError('')
s = []
while d.stop != True:
    try:
        d.start(input())
        if (d.applist != '') and (d.applist):
            s.extend(d.applist)
    except DitError as err:
        print(err)

print(*s)
