'''
2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь
определенное название. К типам одежды в этом проекте относятся пальто
и костюм. У этих типов одежды существуют параметры:
размер (для пальто) и рост (для костюма). Это могут быть обычные
числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать
формулы: для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3). П
роверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные
на этом уроке знания: реализовать абстрактные классы для основных
классов проекта, проверить на практике работу декоратора @property.
'''

from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def fabric_consumption(self):
        pass


class Suit(Clothes):

    def __init__(self, height):
        self.height = height

    @property
    def fabric_consumption(self):
        return 2 * self.height + 0.3


class Coat(Clothes):

    def __init__(self, size):
        self.size = size

    @property
    def fabric_consumption(self):
        return self.size/6.5 + 0.5


suit = Suit(4)
suit2 = Suit(14)
coat = Coat(9)
coat2 = Coat(18)

clothes = [
    suit.fabric_consumption,
    coat.fabric_consumption,
    suit2.fabric_consumption,
    coat2.fabric_consumption
]
print(round(sum(clothes), 2))
