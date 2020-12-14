"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""

# python HW_4_1_Salary.py
from argparse import ArgumentParser


def salary(a, b, c):
    return a * b + c


parser = ArgumentParser()
parser.add_argument('performance', type=float, help='размер выработки в час')
parser.add_argument('rate_of_pay', type=float, help='размер ставки в час')
parser.add_argument('bonus', type=float, help='размер премии')
args = parser.parse_args()

print("Заработная плата сотрудника составит", salary(args.performance, args.rate_of_pay, args.bonus), "рублей.")

