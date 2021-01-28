'''
6. Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools.
Обратите внимание, что создаваемый цикл не должен быть бесконечным.
Необходимо предусмотреть условие его завершения.
Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.
'''

from sys import argv
from itertools import count, cycle


def count_func(a):
    for i in count(a):
        if i < 30:
            print(i)
        else:
            break


def cycle_func(b):
    for i in cycle("ABC"):
        if b > 1:
            print(i)
            b -= 1
        else:
            break


number_my_func, number_cycle_func = argv[1:]
count_func(int(number_my_func))
cycle_func(int(number_cycle_func))

