'''
1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
'''

from sys import argv

hours, rate, bonus = argv[1:]

# Вариант 1
print(f"Заработная плата равна: {float(hours) * float(rate) + float(bonus)}")

# Вариант 2
print(f"Заработная плата равна: {float(argv[1]) * float(argv[2]) + float(argv[3])}")
