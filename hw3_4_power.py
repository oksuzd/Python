"""
4. Программа принимает действительное положительное число x и целое отрицательное число y.
Необходимо выполнить возведение числа x в степень y.
Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень.

Подсказка: попробуйте решить задачу двумя способами.
Первый — возведение в степень с помощью оператора **.
Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
"""


def my_func_1(x: float, y: int) -> float:
    """возводит x в степень y с помощью оператора **"""
    return round(x ** y, 4)


def my_func_2(x: float, y: int) -> float:
    """возводит x в степень y с использованием цикла"""
    power = 1
    for i in range(0, abs(y)):
        power *= x

    return round(1/power, 4)


first_number = float(input("Введите действительное положительное число: "))
second_number = int(input("Введите целое отрицательное число: "))

print(my_func_1(first_number, second_number))
print(my_func_2(first_number, second_number))