'''3.Реализовать функцию my_func(),которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.'''


def sum_of_two_max_out_of_three(number1, number2, number3):
    sum_list=[number1, number2, number3]
    sum_list.sort()
    return sum_list[2] + sum_list[1]


print(sum_of_two_max_out_of_three(3, 4, 4))
