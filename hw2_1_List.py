# 1. Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента. Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

my_list = [1, "два", 3.3, ["четыре", 5], (6.6, "семь"), {8: "восемь"}, True, type(False)]

for i in range(len(my_list)):
    print(f'Тип {i} элемента списка: {type(my_list[i])}')
