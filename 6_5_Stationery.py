"""
5. Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.”
Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw.
Для каждого из классов методы должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""


class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f"{self.title}: запуск отрисовки.")


class Pen(Stationery):
    def draw(self):
        print("Отрисовка ручки.")


class Pencil(Stationery):
    def draw(self):
        print("Отрисовка карандаша.")


class Handle(Stationery):
    def draw(self):
        print("Отрисовка маркера.")


thing_1 = Stationery("Ластик")
thing_2 = Pen("Ручка")
thing_3 = Pencil("Карандаш")
thing_4 = Handle("Маркер")
thing_1.draw()
thing_2.draw()
thing_3.draw()
thing_4.draw()
