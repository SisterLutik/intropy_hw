def my_div(arg_1, arg_2):
    try:
        return arg_1 / arg_2
    except ZeroDivisionError:
        return 'Маленькие еще на 0 делить'


print(my_div(int(input('Введите делимое: ')), int(input('Введите делитель: '))))