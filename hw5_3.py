# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов. Определить,
# кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней
# величины дохода сотрудников.

# без codecs выдавало ошибку nicodeDecodeError:
# 'charmap' codec can't decode byte 0x98 in position 1: character maps to <undefined>

import codecs

f_obj = codecs.open("text_3.txt", "r", "utf_8_sig" )
d = {}
for line in f_obj:
        s = line.split()
        d[s[0]] = float(s[1])

a = [{key for key,val in d.items() if val < 20000}]
print("зарплата сотрудников с окладом менее 20 тыс. ", a)
print("Средняя зарплата ", sum(d.values())/len(d))
f_obj.close()

