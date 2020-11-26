# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

month_num = int(input("Введите номер месяца: "))

# решение через списки
winter = [1, 2, 12]
spring = list(range(3, 6))
summer = list(range(6, 9))
autumn = list(range(9, 12))

if month_num in winter:
    print("зима")
elif month_num in spring:
    print("весна")
elif month_num in summer:
    print("лето")
else:
    print("осень")

# решение через словарь
seasons = {"зима": [1, 2, 12],
           "весна": [3, 4, 5],
           "лето": [6, 7, 8],
           "осень": [9, 10, 11]}

for key, val in seasons.items():
    if month_num in val:
        print(key)
