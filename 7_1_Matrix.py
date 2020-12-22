"""
1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.

Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции
сложения двух объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно —
первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.
"""

from random import randint


class Matrix:
    def __init__(self, list_of_lists):
        self.matrix = list_of_lists

    def __str__(self):
        def list_to_string(some_list, spacer="\t"):
            return f"{spacer}".join(map(str, some_list))
        row_list = [list_to_string(self.matrix[i]) for i in range(len(self.matrix))]
        result_str = list_to_string(row_list, "\n")

        return f'{result_str}\n'

    def __add__(self, other_matrix):
        res = []
        for i in range(len(self.matrix)):
            row = []
            for j in range(len(self.matrix[i])):
                a = self.matrix[i][j] + other_matrix.matrix[i][j]
                row.append(a)
            res.append(row)
        return res


n = randint(3, 5)
m = randint(3, 5)

matrix_1 = Matrix([[randint(0, 10) for j in range(m)] for i in range(n)])
matrix_2 = Matrix([[randint(0, 10) for j in range(m)] for i in range(n)])
res_matrix = Matrix(matrix_1 + matrix_2)

print(matrix_1)
print(matrix_2)
print(res_matrix)
