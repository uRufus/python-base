'''
3. Реализовать программу работы с органическими клетками.
Необходимо создать класс Клетка. В его конструкторе инициализировать
параметр, соответствующий количеству клеток (целое число).
В классе должны быть реализованы методы перегрузки
арифметических операторов: сложение (__add__()), вычитание (__sub__()),
умножение (__mul__()), деление (__truediv__()).Данные методы должны применяться
только к клеткам и выполнять увеличение, уменьшение, умножение и
обычное (не целочисленное) деление клеток, соответственно. В методе деления должно
осуществляться округление значения до целого числа.
Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно
равняться сумме ячеек исходных двух клеток.
Вычитание. Участвуют две клетки. Операцию необходимо выполнять только
если разность количества ячеек двух клеток больше нуля, иначе выводить соответствующее сообщение.
Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется
как произведение количества ячеек этих двух клеток.
Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется
как целочисленное деление количества ячеек этих двух клеток.
В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и
количество ячеек в ряду. Данный метод позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****..., где количество
ячеек между \n равно переданному аргументу. Если ячеек на формирование ряда не хватает,
то в последний ряд записываются все оставшиеся.
Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5.
Тогда метод make_order() вернет строку: *****\n*****\n**.
Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда
метод make_order() вернет строку: *****\n*****\n*****.
Подсказка: подробный список операторов для перегрузки доступен по ссылке.
'''


class Cell:

    def __init__(self, cells):
        self.cells = int(cells)

    def __add__(self, other):
        self.cells += other.cells
        return self.cells

    def __sub__(self, other):
        if (self.cells - other.cells) > 0:
            self.cells -= other.cells
            return self.cells
        else:
            return "Вычитание клеток невозможно"

    def __mul__(self, other):
        self.cells *= other.cells
        return self.cells

    def __truediv__(self, other):
        self.cells //= other.cells
        return self.cells

    def make_order(self, cells_in_stage):
        return "".join(["*" if i % cells_in_stage != 0 else "*\n" for i in range(1, self.cells + 1)])


cell_a = Cell(16)
cell_b = Cell(2)
cell_a + cell_b
print(cell_a.cells)
cell_a - cell_b
print(cell_a.cells)
cell_a / cell_b
print(cell_a.cells)
cell_a * cell_b
print(cell_b.cells)
print(cell_a.cells)
print(cell_a.make_order(5))

