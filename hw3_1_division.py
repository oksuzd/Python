"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""


def division_func(num_1, num_2):
    """Принимает два числа и выполняет их деление"""
    if num_2 != 0:
        print(f"{first_number:} / {second_number} = {round(num_1 / num_2, 2)}")
    else:
        print("Делить на 0 нельзя!")


first_number = input("Введите первое число: ")
second_number = input("Введите второе число: ")

division_func(float(first_number), float(second_number))
