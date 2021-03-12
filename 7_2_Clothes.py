"""
2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы:
для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани.
Реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
"""

from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, param):
        self.param = param

    @abstractmethod
    def textile_spending(self):
        pass


class Coat(Clothes):
    @property
    def textile_spending(self):
        return round(self.param / 6.5 + 0.5, 2)


class Suit(Clothes):
    @property
    def textile_spending(self):
        return round(2 * self.param + 0.3, 2)


clothes_c = Coat(42)
clothes_s = Suit(1.72)

spend_c = clothes_c.textile_spending
spend_s = clothes_s.textile_spending
common_spending = spend_c + spend_s

print(f'Расход ткани на пальто: {spend_c} м.')
print(f'Расход ткани на костюм: {spend_s} м.')
print(f'Общий расход ткани: {common_spending} м.')
