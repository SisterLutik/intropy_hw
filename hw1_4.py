# 4. Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.
n = int(input("Введите число: "))
bigger = 0
while n != 0:
    p = n % 10
    if p > bigger:
        bigger = p
    n = n // 10
print('самая большая цифра в числе:', bigger)
