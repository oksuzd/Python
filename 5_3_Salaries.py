"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""

print("Оклад менее 20 тыс. имеют следующие сотрудники: ")

with open("5_3_Salaries.txt") as f:
    salary_sum = 0
    employees = f.readlines()
    for el in employees:
        salary = el.split()
        salary_sum += float(salary[1])
        if float(salary[1]) < 20000:
            print(salary[0])

print("Средняя величина дохода сотрудников:", round(salary_sum / len(employees), 2))
