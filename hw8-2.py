"""
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля в качестве делителя
программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class OwnException(Exception):
    def __init__(self, error):
        self.error = error


user_divisible = int(input('Введите делимое: '))
user_divider = int(input('Введите делитель: '))

try:
    if user_divider == 0:
        raise OwnException('Деление на 0 невозможно!')
    else:
        res = round(user_divisible / user_divider, 2)
        print(f'Результат равен: {res}')
except OwnException as er:
    print(er)
