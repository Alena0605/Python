"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""

with open('hw5-3.txt') as f:
    lines = f.readlines()

all_income = 0
worker = 0
for line in lines:
    word = line.split()
    if int(word[1]) < 20000:
        print(word[0])
        all_income += int(word[1])
        worker += 1

avr_income = all_income / worker

print(f'Размер средней величины дохода сотрудников: {round(avr_income, 2)}')
