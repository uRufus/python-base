'''Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.'''
user_input = int(input("Введите положительное число: "))
max_number = 0
while user_input > 0:
    number = user_input % 10
    if max_number < number:
        max_number = number
    user_input //= 10
print(max_number)
