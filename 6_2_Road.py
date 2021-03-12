"""
2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
толщиной в 1 см * число см толщины полотна. Проверить работу метода.
Например: 20м * 5000м * 25кг * 5см = 12500 т
"""


class Road:
    def __init__(self, name, length, width):
        self.name = name
        self._length = length
        self._width = width

    def mass(self, mass_of_1m, depth):
        return (self._length * self._width * mass_of_1m * depth) / 1000

    def print_info(self, road_name, asphalt_mass):
        print(f'Для покрытия дороги "{road_name}" потребуется {asphalt_mass} т. асфальта.')


first_road = Road("Южная", 20, 5000)
second_road = Road("Восточная", 40, 3000)
first_road.print_info(first_road.name, first_road.mass(25, 5))
first_road.print_info(second_road.name, second_road.mass(15, 4))
