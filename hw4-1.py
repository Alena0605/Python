"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""

from sys import argv


def get_salary():
    work_in_hours, rate_in_hour, bonus = argv[1:]
    salary = (int(work_in_hours) * int(rate_in_hour)) + int(bonus)
    return salary


print(get_salary())
