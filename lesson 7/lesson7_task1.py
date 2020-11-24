# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
class Matrix:
    def __init__(self, list_matr_1):
        self.list_matr_1 = list_matr_1


    def __str__(self):
        pass


    def __add__(self, other):
        matr = [[0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]]

        for i in range(len(self.list_matr_1)): # перебор по i - строка

            for j in range(len(other.list_matr_1[i])): # перебор по j - столбец

                matr[i][j] = self.list_matr_1[i][j] + other.list_matr_1[i][j]

        return  str('\n'.join(['\t'.join([str(j) for j in i]) for i in matr]))





my_matrix_1 = Matrix([[1, 2],
                    [6, 2],
                    [11, 7]])

my_matrix_2 = Matrix([[0, 0],
                    [0, 7],
                    [9, 5]])

print(my_matrix_1 + my_matrix_2)
