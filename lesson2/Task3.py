'''3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.'''

# Вариант со списком
list_of_months = ["зима", "зима", "весна",
                  "весна", "весна", "лето",
                  "лето", "лето", "осень",
                  "осень",  "осень", "зима"
                  ]

while True:
    month = int(input("Введите номер месяца: "))
    if 0 < month < 13:
        break

print(list_of_months[month - 1])

# Вариант со словарем
while True:
    month = int(input("Введите номер месяца: "))
    if 0 < month < 13:
        break

seasons_dict = {
    "зима": [12, 1, 2],
    "весна": [3, 4, 5],
    "лето": [6, 7, 8],
    "осень": [9, 10, 11]
}

for key, values in seasons_dict.items():
    for value in values:
        if value == month:
            print(key)
            break
