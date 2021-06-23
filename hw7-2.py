"""
2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.

Для определения расхода ткани по каждому типу одежды использовать формулы:
для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3).
Проверить работу этих методов на реальных данных.

Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
"""

from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, param):
        self.param = param

    @abstractmethod
    def sum_cloth(self):
        pass


class Coat(Clothes):

    @property
    def sum_cloth(self):
        cloth_for_coat = self.param / 6.5 + 0.5
        return round(cloth_for_coat, 2)


class Suit(Clothes):

    @property
    def sum_cloth(self):
        cloth_for_suit = 2 * self.param + 0.3
        return round(cloth_for_suit, 2)


coat_1 = Coat(44)
suit_1 = Suit(165)
print(coat_1.sum_cloth)
print(suit_1.sum_cloth)

print(f'Общий расход ткани: {coat_1.sum_cloth + suit_1.sum_cloth}')
