'''
5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел.
Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введен после нескольких чисел, то вначале нужно добавить
сумму этих чисел к полученной ранее сумме и после этого завершить программу.
'''

#Вариант с функцией без параметров
def sum_func():
    sum_of_numbers_var1 = 0
    finish = None
    while finish is None:
        list_of_numbers = input("Введите числа через пробел, чтобы программа расчитала их сумму.\n "
                                "Если ввести '!', то программа закончит суммировать числа: ").split()
        for number in list_of_numbers:
            if number != "!":
                sum_of_numbers_var1 += float(number)
            else:
                finish = 1
                break
        print(f"Сумма введенных чисел: {sum_of_numbers_var1}")


sum_func()

# Вариант с функцией c параметрами
def sum_func(sum_of_numbers, numbers , finish):
    for i in numbers:
        if i != "!":
            sum_of_numbers += float(i)
        else:
            finish = 1
            break
    return sum_of_numbers, finish


continue_to_ask_for_numbers = None
sum_of_numbers = 0
while continue_to_ask_for_numbers is None:
    list_of_numbers = input("Введите числа через пробел, чтобы программа расчитала их сумму.\n "
                            "Если ввести '!', то программа закончит суммировать числа: ").split()
    sum_of_numbers, continue_to_ask_for_numbers = sum_func(sum_of_numbers, list_of_numbers, continue_to_ask_for_numbers)
    print(f"Сумма введенных чисел: {sum_of_numbers}")


