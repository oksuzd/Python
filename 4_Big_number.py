# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

n = input("Введите целое положительное число n: ")
i = 0
max_number = 0

while i != len(n):
    if int(n[i]) > max_number:
        max_number = int(n[i])
    i += 1
print("Самая большая цифра в числе:", max_number)