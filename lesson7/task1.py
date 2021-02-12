'''
1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора
класса (метод __init__()), который должен принимать данные
(список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин,
расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__()
для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации
операции сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый
элемент первой строки первой матрицы складываем с первым
элементом первой строки второй матрицы и т.д.
'''


def check_matrices(a, v):
    if len(a) == len(v):
        for i in range(len(a)):
            if len(a[i]) != len(v[i]):
                return False
        return True
    return False


class Matrix:

    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        self.matrix_str = ""
        for i in self.matrix:
            for j in i:
                self.matrix_str += str(j) + " "
            self.matrix_str += "\n"
        return self.matrix_str

    def __add__(self, other):
        if check_matrices(self.matrix, other.matrix):
            for i in range(len(self.matrix)):
                for k in range(len(self.matrix[0])):
                    self.matrix[i][k] += int(other.matrix[i][k])
        else:
            print("Матрицы нельзя сложить")
        return self.matrix


first_matrix = Matrix([[31, 22], [37, 43], [51, 86]])
second_matrix = Matrix([[29, 38], [23, 17], [9, 4]])
print(first_matrix)
print(first_matrix.matrix)
print(first_matrix + second_matrix)
print(first_matrix.matrix)
print(first_matrix)
