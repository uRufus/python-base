'''
1. Создать программно файл в текстовом формате, записать в него построчно данные,
вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.
'''
# Вариант 1
with open("task1.txt", "w", encoding="utf-8") as file:
    while True:
        line = (input("Введите данные: "))
        if line != "":
            file.write(line + "\n")
        else:
            break

# Вариант 2
with open("task1.txt", "w", encoding="utf-8") as file:
    while (line := input("Введите данные: ")) != "":
        file.write(line + "\n")
