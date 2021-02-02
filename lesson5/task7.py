'''
7. Создать (не программно) текстовый файл, в котором каждая строка
должна содержать данные о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании,
а также среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
а также словарь со средней прибылью. Если фирма получила убытки,
также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
'''

from json import dump
with open("task7.txt", "r", encoding="utf-8") as file:
    firms = {}
    profit = 0
    number_of_profit_firms = 0
    for line in file.readlines():
        line = line.split()
        profit_loss = int(line[2]) - int(line[3])
        firms[line[0]] = profit_loss
        if profit_loss >= 0:
            profit += profit_loss
            number_of_profit_firms += 1
with open("task7.json", "w", encoding="utf-8") as json_file:
    dump([firms, {"average_profit": round(profit / number_of_profit_firms, 2)}], json_file)

# # Вариант 2
from json import dump
with open("task7.txt", "r", encoding="utf-8") as file:
    profit = 0
    number_of_profit_firms = 0
    firms = [line.split() for line in file.readlines()]
    firms2 = {firm[0]: int(firm[2]) - int(firm[3]) for firm in firms}
    for value in firms2.values():
        if value >= 0:
            profit += value
            number_of_profit_firms += 1
with open("task7.json", "w", encoding="utf-8") as json_file:
    dump([firms2, {"average_profit": round(profit / number_of_profit_firms, 2)}], json_file)

# Вариант 3
from json import dump
with open("task7.txt", "r", encoding="utf-8") as file:
    firms = [line.split() for line in file.readlines()]
    firms2 = {firm[0]: int(firm[2]) - int(firm[3]) for firm in firms}
    ave_profit = [value for value in firms2.values() if value >= 0]
    with open("task7.json", "w", encoding="utf-8") as json_file:
        dump([firms2, {"average_profit": round(sum(ave_profit) / len(ave_profit), 2)}], json_file)