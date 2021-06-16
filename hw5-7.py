"""
7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.

Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].

Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
"""

import json

with open('hw5-7.txt') as f:
    lines = f.readlines()

firm_with_profit = {}
dict_avr_pr = {'average_profit': ''}
list_avr_pr = []
firm_with_loss = {}

for line in lines:
    firm_data = line.split()
    profit = int(firm_data[2]) - int(firm_data[3])
    if profit > 0:
        firm_with_profit[firm_data[0]] = profit
        list_avr_pr.append(profit)
    elif profit < 0:
        firm_with_loss[firm_data[0]] = profit

average_profit = sum(list_avr_pr) / len(list_avr_pr)
dict_avr_pr['average_profit'] = average_profit

firm_list = [firm_with_profit, dict_avr_pr, firm_with_loss]
print(firm_list)

with open('hw5-7.json', 'w') as f_json:
    json.dump(firm_list, f_json)

with open('hw5-7.json') as f_json:
    print(json.load(f_json))
