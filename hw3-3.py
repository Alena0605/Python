"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""


def my_func(arg_1, arg_2, arg_3):
    min_arg = min([arg_1, arg_2, arg_3])
    sum_arg = sum([arg_1, arg_2, arg_3]) - min_arg
    return sum_arg


print(my_func(10, 3, 7))
