'''
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем
нуля в качестве делителя программа должна корректно обработать эту
ситуацию и не завершиться с ошибкой.
'''


class ExceptZeroDiv(Exception):
    pass


def zero_div_exception(a, b):
    try:
        if b != 0:
            print(a / b)
        else:
            raise ExceptZeroDiv
    except ExceptZeroDiv:
        print("На ноль делить нельзя")


zero_div_exception(10, 0)
zero_div_exception(10, 2)
zero_div_exception(4, 0)
