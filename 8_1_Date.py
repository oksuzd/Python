"""
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату
в виде строки формата «день-месяц-год». В рамках класса реализовать два метода.
Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
"""

from random import randint


class Date:
    def __init__(self, some_date):
        self.the_date = some_date

    def __str__(self):
        self.valid_date(self.get_number(self.date_list, 0), self.get_number(self.date_list, 1),
                        self.get_number(self.date_list, 2))
        return f'{self.get_number(self.date_list, 0):02}-' \
               f'{self.get_number(self.date_list, 1):02}-{self.get_number(self.date_list, 2):04}'

    @property
    def date_list(self):
        return self.the_date.split("-")

    @classmethod
    def get_number(cls, some_list, i):
        return int(some_list[i])

    @staticmethod
    def valid_date(day, month, year):
        if day > 31 or month > 12 or year > 2020:
            print(f"Дата некорректна.")
        else:
            print(f"Дата корректна.")


date_1 = Date(f'{randint(1,35)}-{randint(1,15)}-{randint(1980,2030)}')
print(date_1)
