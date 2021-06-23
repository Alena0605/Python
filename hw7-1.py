"""
1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.

Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.

Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде. Далее реализовать
перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.

Подсказка: сложение элементов матриц выполнять поэлементно —
первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.
"""


class Matrix:
    def __init__(self, data_matrix):
        self.data_matrix = data_matrix

    def __str__(self):
        return '\n'.join([' '.join(map(str, line)) for line in self.data_matrix])

    def __add__(self, other):
        result = []
        if len(self.data_matrix) == len(other.data_matrix):
            for line_mat1, line_mat2 in zip(self.data_matrix, other.data_matrix):
                if len(line_mat1) == len(line_mat2):
                    sum_matrix = [el_line1 + el_line2 for el_line1, el_line2 in zip(line_mat1, line_mat2)]
                    result.append(sum_matrix)
                else:
                    return 'Матрицы сложить нельзя'
            return '\n'.join([' '.join(map(str, line)) for line in result])
        else:
            return 'Матрицы сложить нельзя'


matrix_1 = Matrix([[10, 6, 28], [4, 16, 7]])
matrix_2 = Matrix([[42, 17, 34], [11, 57, 79]])
print(f'Первая матрица:\n{matrix_1}')
print(f'Вторая матрица:\n{matrix_2}')

print(f'\nСложение матриц:\n{matrix_1 + matrix_2}')
