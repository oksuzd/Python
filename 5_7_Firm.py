"""
7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

"""
import json


def profit(file_line):
    """словарь, где ключ - название фирмы, а значение - прибыль (убытки)"""
    firm_list = file_line.split()
    firm_profit = int(firm_list[-2]) - int(firm_list[-1])

    return {firm_list[0]: firm_profit}


def average_profit(firms_dict):
    """словарь, где ведется учет средней прибыли фирм"""
    average_sum = 0
    profit_firms = 0
    for val in firms_dict.values():
        if val > 0:
            average_sum += val
            profit_firms += 1
    try:
        aver_prof = average_sum / profit_firms
    except ZeroDivisionError:
        aver_prof = 0

    average_dict = {"Средняя прибыль": round(aver_prof, 2)}

    return average_dict


with open("5_7_Firm.txt", "r", encoding="utf-8") as f:
    all_firms_dict = {}
    all_average_profit = {"Средняя прибыль": 0}

    for line in f.readlines():
        all_firms_dict.update(profit(line))

    all_average_profit.update(average_profit(all_firms_dict))

    profit_list = [all_firms_dict, all_average_profit]

with open("5_7_Firm.json", "w") as f:
    json.dump(profit_list, f)
