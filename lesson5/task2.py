'''
2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
'''

# Вариант 1
strings, words = 0, 0
with open("task2.txt", "r", encoding="utf-8") as file:
    for lines in file.readlines():
        strings += 1
        for word in lines.split():
            words += 1

print(strings, words)

# Вариант 2
strings = 0
words = {}
with open("task2.txt", "r", encoding="utf-8") as file:
    for lines in file.readlines():
        strings += 1
        for word in lines.split():
            if strings not in words:
                words[strings] = 1
            else:
                words[strings] += 1
print(f"Количество строк: {strings} "
      f"количество слов в каждой строке: {words}")

# Вариант 3
strings, words = 0, 0
with open("task2.txt", "r", encoding="utf-8") as file:
    for lines in file.readlines():
        strings += 1
        for word in lines.split():
            words += 1
        print(f"В строке {strings} лежит {words} слов")
        words = 0

print(f"Общее количество строк: {strings}")
