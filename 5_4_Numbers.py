"""
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""


eng_list = ["One", "Two", "Three", "Four"]
rus_list = ["Один", "Два", "Три", "Четыре"]

new_numbers_list = []

with open("5_4_Numbers.txt") as f:
    strings = f.readlines()
    for i, line in enumerate(strings):
        new_line = line.replace(eng_list[i], rus_list[i])
        new_numbers_list.append(new_line)


with open("5_4_Numbers_new.txt", "w") as f:
    f.writelines(new_numbers_list)
