# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен
# принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix
# (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем
# с первым элементом первой строки второй матрицы и т.д.

class Matrix:
        def __init__(self, matrix):
            self.matrix = matrix
            a = len(self.matrix[0])
            for i in range(len(self.matrix)):
               if a != len(self.matrix[i]):
                   self.matrix = ''
                   print(matrix, ' матрица не матрица')



        def __add__(self, over):
            if (len(self.matrix) == len(over.matrix)) and (len(self.matrix[0]) == len(over.matrix[0])):
                ad = [[int(self.matrix[ii][i]) + int(over.matrix[ii][i]) for i in range(len(self.matrix[ii]))] for ii in range(len(self.matrix))]

                return Matrix(ad)
            return 'Wrong - разная размерность'

        def __str__(self):
            a = '\n'.join(''.join([str(el) + (7 - len(str(el)))*' ' for el in x]) for x in self.matrix)
            return a


matrix_1 = Matrix([[11,2], [1,2], [8,2]])
matrix_2 = Matrix([[1,2], [3,4], [4,3]])
print(matrix_1 + matrix_2)
print('')
print(matrix_2)
matrix_3 = Matrix([[1,23,4], [4,3]])
matrix_4 = Matrix([[1,2], [3,4]])
print(matrix_1 + matrix_4)
