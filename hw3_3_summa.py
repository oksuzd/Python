"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""


def my_func(a, b, c):
    """возвращает сумму наибольших двух аргументов"""
    start_list = [a, b, c]

    def pop_max_el(some_list):
        """извлекает и возвращает максимальный элемент списка"""
        return some_list.pop(some_list.index(max(some_list)))

    return pop_max_el(start_list) + pop_max_el(start_list)


first_number = float(input("Введите первое число: "))
second_number = float(input("Введите второе число: "))
third_number = float(input("Введите третье число: "))

print(my_func(first_number, second_number, third_number))
