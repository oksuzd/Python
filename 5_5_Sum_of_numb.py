"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

from random import randint

with open("5_5_Sum_of_numb.txt", "w") as f:
    for i in range(randint(5, 10)):
        print(f'{str(randint(1, 100))}', end=" ", file=f)

with open("5_5_Sum_of_numb.txt") as f:
    numbers = f.read()
    sum_numbers = sum(map(int, numbers.split()))

print(f'Числа в файле: {numbers}')
print(f'Сумма чисел: {sum_numbers}')
