# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
# вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту
# ситуацию и не завершиться с ошибкой.


class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt

inp_data = input("Введите делимое и делитель через пробел: ")

try:
    ls = inp_data.split()
    ls = list(map(lambda x: int(x), ls))
    if ls[1] == 0:
        raise OwnError("Маленькике на 0 делить!")
except ValueError:
    print("Вы ввели не число")
except IndexError:
    print("Нет делителя и делить не на что")
except OwnError as err:
    print(err)
else:
    print(f"Все хорошо. Ваше число: {ls[0]/ls[1]}")
