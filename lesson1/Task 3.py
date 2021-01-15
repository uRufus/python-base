'''Узнайте у пользователя число n.
Найдите сумму чисел n + nn + nnn.
Например, пользователь ввёл число 3.
Считаем 3 + 33 + 333 = 369.'''
user_input = input("Введите число: ")
input_sum = int(user_input) + int(user_input * 2) + int(user_input * 3)
print(input_sum)
