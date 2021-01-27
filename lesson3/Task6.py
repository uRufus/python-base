'''
6. Реализовать функцию int_func(), принимающую слово из маленьких латинских
букв и возвращающую его же, но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
Продолжить работу над заданием. В программу должна попадать строка из слов,
разделенных пробелом. Каждое слово состоит из латинских букв в нижнем регистре.
Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
Необходимо использовать написанную ранее функцию int_func().
'''

# 1 Вариант
def int_func(word):
    return word[0].upper() + word[1:]


def upper_first_letters_string(words):
    words = words.split()
    for word in words:
        word = int_func(word)
        print(word, end=" ")
    print("")


upper_first_letters_string(input("Введите слова через пробел:"))


# 2 Вариант
def upper_first_letters(words):
    return words.title()


print(upper_first_letters(input("Введите слова через пробел:")))
