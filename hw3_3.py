# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших
# двух аргументов.

def my_func(a, b, c):
    sum_1 = a
    sum_2 = b

    if sum_1 < sum_2:
        if sum_1 < c:
            sum_1 = c
    else:
        if sum_2 < c:
            sum_2 = c
    return sum_1 + sum_2



print("Введите 3 числа через Enter ")
print("Сумма наибольших", my_func(int(input()), int(input()), int(input())))











