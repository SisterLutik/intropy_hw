# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа запрашивать у
# пользователя, предусмотреть обработку ситуации деления на ноль.

def my_div(arg_1, arg_2):
    try:
        return arg_1 / arg_2
    except ZeroDivisionError:
        return 'Маленькие еще на 0 делить'


print(my_div(int(input('Введите делимое: ')), int(input('Введите делитель: '))))