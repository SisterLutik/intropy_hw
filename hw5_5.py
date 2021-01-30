# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

from random import randint
import json

data = [randint(-20, 20) for i in range(5)]
with open("my_file(5).txt", "w") as write_f:
    json.dump(data, write_f)

with open("my_file(5).txt") as read_f:
    data1 = json.load(read_f)

print(sum(data1))