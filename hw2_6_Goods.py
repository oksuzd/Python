# 6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента —
# номер товара и словарь с параметрами (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.

# Пример готовой структуры:
# [
# (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
# (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
# (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
# Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара,
# например название, а значение — список значений-характеристик, например список названий товаров.
#
# Пример:
# {
# “название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7],
# “ед”: [“шт.”]
# }

# формируем каталог товаров
goods_list = []
catalogue_list = []
goods_num = int(input("Введите количество наименований товаров: "))

for i in range(goods_num):
    name = input(f'Введите название {i+1} товара: ')
    price = input(f'Введите цену товара "{name}": ')
    number = input(f'Введите количество товара "{name}": ')
    unit = input(f'Введите единицу измерения товара "{name}": ')
    goods_dict = {"Название": name, "Цена": price, "Количество": number, "Ед.": unit}
    goods_list.append(goods_dict)

print("\nКаталог товаров:")
for i in enumerate(goods_list, 1):
    catalogue_list.append(i)
    print(i)

# собираем аналитику (группируем информацию)
list_name = []
list_price = []
list_number = []
list_unit = []
keys_list = []
values_list = [list_name, list_price, list_number, list_unit]
analytic_dict = zip(keys_list, values_list)

for k in goods_list[0].keys():
    keys_list.append(k)

for el in goods_list:
    for key, val in el.items():
        if key == keys_list[0]:
            list_name.append(val)
        elif key == keys_list[1]:
            list_price.append(val)
        elif key == keys_list[2]:
            list_number.append(val)
        elif key == keys_list[3]:
            list_unit.append(val)

print("\nАнализ товаров:")

for k, v in dict(analytic_dict).items():
    print(f'{k}: {v}')
