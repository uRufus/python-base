'''
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
'''
from random import randint
with open("task5.txt", "w", encoding="utf-8") as file:
    for number in range(randint(3, 30)):
        file.write(f"{randint(1, 100)} ")

with open("task5.txt", "r", encoding="utf-8") as file:
    sum_of_numbers = 0
    for number in file.readline().split():
        sum_of_numbers += int(number)
    print(sum_of_numbers)
