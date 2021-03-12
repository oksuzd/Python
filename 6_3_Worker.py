"""
Реализовать базовый класс Worker (работник), в котором определить атрибуты:
name, surname, position (должность), income (доход).
Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
оклад и премия, например, {"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и
дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position,
передать данные, проверить значения атрибутов, вызвать методы экземпляров).
"""


class Worker:
    worker_income = {"wage": 20000, "bonus": 0}

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.position = Position
        self._income = Position.get_total_income


class Position(Worker):

    def get_full_name(self):
        return self.surname + " " + self.name

    def get_total_income(self, wage=Worker.worker_income["wage"], bonus=Worker.worker_income["bonus"]):
        print(f'Доход сотрудника {self.get_full_name()} составляет {wage + bonus} рублей.')


first_worker = Position("Василий", "Пупкин")
print(first_worker.get_full_name())
first_worker.get_total_income()
second_worker = Position("Александр", "Невский")
second_worker.get_total_income(150000, 20500)
