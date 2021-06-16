"""
1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""

with open('hw5-1.txt', 'w') as f:
    while True:
        string = input('Enter some text: ')
        if string:
            f.write(f'{string}\n')
        else:
            break
