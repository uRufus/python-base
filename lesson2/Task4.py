'''4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
Если в слово длинное, выводить только первые 10 букв в слове.'''

user_input = input("Введите строку из слов разделенных пробелами: ")
print_list = user_input.split()
line = 1
for word in print_list:
    if len(word) > 10:
        word = word[:10]
    print(f"{line} {word}")
    line += 1
