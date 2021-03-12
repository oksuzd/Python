"""
2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

with open("5_2_Data_count.txt", "r", encoding="utf-8") as f:
    data = f.readlines()

print(f'Количество строк в файле: {len(data)}')

for i, el in enumerate(data):
    print(f'В {i+1} строке {len(el.split())} слов')
