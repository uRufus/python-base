'''1.Реализовать функцию,принимающую два числа(позиционные аргументы)
и выполняющую их деление.Числа запрашивать у пользователя,
предусмотреть обработку ситуации деления на ноль.'''


def numbers_division(number1, number2):
    try:
        number1 = float(number1)
        number2 = float(number2)
    except ValueError:
        return"Одно из чисел введено некорректно"
    try:
        division = number1 / number2
    except ZeroDivisionError:
        return "На ноль делить нельзя"
    return division


first_number = input("Введите число которое будете делить:")
second_number = input("Введите число на которое будете делить:")
print(f"Резльтат деления числа {first_number} на число {second_number}:"
      f" {numbers_division(first_number, second_number)}")

