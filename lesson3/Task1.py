'''1.Реализовать функцию,принимающую два числа(позиционные аргументы)
и выполняющую их деление.Числа запрашивать у пользователя,
предусмотреть обработку ситуации деления на ноль.'''


def numbers_quotient(dividend, divisor):
    try:
        dividend = float(dividend)
        divisor = float(divisor)
    except ValueError:
        return "Одно из чисел введено некорректно"
    try:
        quotient = dividend / divisor
    except ZeroDivisionError:
        return "На ноль делить нельзя"
    return quotient


first_number = input("Введите число которое будете делить: ")
second_number = input("Введите число на которое будете делить: ")
print(f"Резльтат деления числа {first_number} на число {second_number}:"
      f" {numbers_quotient(first_number, second_number)}")

