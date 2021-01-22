'''5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных
чисел. У пользователя необходимо запрашивать новый элемент рейтинга.
Если в рейтинге существуют элементы с одинаковыми значениями,
то новый элемент с тем же значением должен разместиться после них.
Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].'''

# Первый вариант. Не соответствует постановке задачи, просьба смотреть сразу второй вариант
my_list = [7, 5, 3, 3, 2]
print(f"Рейтинг {my_list}")
user_input = int(input("Введите новый элемент рейтинга: "))
my_list.append(user_input)
my_list.sort(reverse=True)
print(f"Новый рейтинг {my_list}")

# Второй вариант
my_list = [7, 5, 3, 3, 2]
print(f"Рейтинг {my_list}")
user_input = int(input("Введите новый элемент рейтинга 2: "))
new_list = []
check = 0
for element in my_list:
    if user_input > element:
        new_list.append(user_input)
        user_input = 0
        check += 1
    new_list.append(element)
if len(my_list) == len(new_list):
    new_list.append(user_input)
print(f"Новый рейтинг {new_list}")

# Третий вариант
my_list = [7, 5, 3, 3, 2]
print(f"Рейтинг {my_list}")
user_input = int(input("Введите новый элемент рейтинга 3: "))
check = 0
for element in my_list:
    if user_input > element:
        my_list.insert(check, user_input)
        break
    check += 1
if user_input not in my_list:
    my_list.append(user_input)
print(f"Новый рейтинг {my_list}")
