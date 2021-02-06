'''
6. Необходимо создать (не программно) текстовый файл, где каждая строка
описывает учебный предмет и наличие лекционных, практических и лабораторных
занятий по этому предмету и их количество. Важно, чтобы для каждого предмета
не обязательно были все типы занятий. Сформировать словарь, содержащий название
предмета и общее количество занятий по нему. Вывести словарь на экран.
Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —

Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
'''

# Вариант 1
subject_hours = {}
with open("task6.txt", "r", encoding="utf-8") as file:
    for line in file.readlines():
        words = line.split(":")
        subject_hours[words[0]] = 0
        for numbers in words[1].split():
            hours = "0"
            for number in numbers:
                if number.isdigit():
                    hours += number
            subject_hours[words[0]] += int(hours)

print(subject_hours)

# Вариант 2
subject_hours = {}
with open("task6.txt", "r", encoding="utf-8") as file:
    for line in file.readlines():
        words = line.replace("(", " ").replace(":", "").split()
        subject_hours[words[0]] = sum([int(number) for number in words[1:] if number.isdigit()])
    print(subject_hours)


