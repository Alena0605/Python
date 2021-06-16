"""
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4

Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""

with open('hw5-4.txt') as f:
    lines = f.readlines()

with open('new_hw5-4.txt', 'w') as new_f:
    for line in lines:
        if 'One' in line:
            new_line = line.replace('One', 'Один')
        elif 'Two' in line:
            new_line = line.replace('Two', 'Два')
        elif 'Three' in line:
            new_line = line.replace('Three', 'Три')
        elif 'Four' in line:
            new_line = line.replace('Four', 'Четыре')
        new_f.write(new_line)
