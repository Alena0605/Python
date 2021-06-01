"""
4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
"""

num = int(input('Введите число: '))
max_num = 0

while num:
    sep_num = num % 10
    if max_num < sep_num:
        max_num = sep_num
    num = num // 10

print(max_num)
