"""
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
Проверьте его работу на данных, вводимых пользователем.
При вводе пользователем ноля в качестве делителя программа должна корректно обработать эту ситуацию
и не завершиться с ошибкой.
"""


class MyZeroDivisionError(Exception):
    def __init__(self):
        self.text = "Делить на ноль нельзя!"


n = int(input("Введите число n: "))
m = int(input("Введите число m: "))

try:
    if m == 0:
        raise MyZeroDivisionError()
except MyZeroDivisionError as error:
    print(error.text)
else:
    print(f"Результат деления m/n: {n / m}")
