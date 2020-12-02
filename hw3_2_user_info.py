"""
2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
"""


def user_info_func(name, surname, birth, city, email, tel_numb):
    print(f"\nПользователь: {surname} {name}, {birth} года рождения, проживает в г. {city}. "
          f"Контактная информация: {email}, {tel_numb}.")


user_name = input("Введите имя: ")
user_surname = input("Введите фамилию: ")
user_birt = input("Введите год рождения: ")
user_city = input("Введите город проживания: ")
user_email = input("Введите email: ")
user_tel_numb = input("Введите телефон: ")

user_info_func(name=user_name, surname=user_surname, birth=user_birt, city=user_city, email=user_email, tel_numb=user_tel_numb)