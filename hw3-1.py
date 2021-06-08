"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""


def get_division(divisible, divisor):
    try:
        return divisible / divisor
    except ZeroDivisionError:
        return 'Внимание! Вы пытаетесь делить на 0!'


print(get_division(int(input('Введите делимое: ')), int(input('Введите делитель: '))))
