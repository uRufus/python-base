'''
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую
построчно данные. При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
'''

russian_numbers = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
with open("task4_original.txt", "r", encoding="utf-8") as file:
    with open("task4_new.txt", "w", encoding="utf-8") as new_file:
        for line in file.readlines():
            line = line.split()
            new_file.write(f"{russian_numbers[line[0]]} {line[1]} {line[2]}\n")



