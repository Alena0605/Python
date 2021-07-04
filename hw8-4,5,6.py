"""
4. Начните работу над проектом «Склад оргтехники».
Создайте класс, описывающий склад. А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
-----------------------------------------------------------------------------------------------------------------------
5. Продолжить работу над первым заданием.
Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
можно использовать любую подходящую структуру, например словарь.
-----------------------------------------------------------------------------------------------------------------------
6. Продолжить работу над вторым заданием.
Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
изученных на уроках по ООП.
"""

from abc import ABC, abstractmethod


class NotNumber(Exception):
    def __init__(self, text):
        self.text = text


class Warehouse:
    pass


class OfficeEquipment(ABC):
    def __init__(self, name: str, price: int, amount):
        self.name = name
        self.price = price
        self.amount = amount
        self.warehouse_dict = {'Модель': self.name, 'Цена за шт.': self.price, 'Количество': self.amount}

    def __str__(self):
        return f'{self.warehouse_dict}'

    def __add__(self, other):
        try:
            if type(self.warehouse_dict['Количество']) == int and type(other.warehouse_dict['Количество']) == int:
                result = self.warehouse_dict['Количество'] + other.warehouse_dict['Количество']
                return {'Модель': self.name, 'Цена за шт.': self.price, 'Количество': result}
            else:
                raise NotNumber('Вы ввели не число!')
        except NotNumber as er:
            return f'В объекте {self.name} возникла ошибка! {er}'

    def __sub__(self, other):
        try:
            if type(self.warehouse_dict['Количество']) == int and type(other.warehouse_dict['Количество']) == int:
                result = self.warehouse_dict['Количество'] - other.warehouse_dict['Количество']
                print(f'После передачи {self.name} в другое подразделение, на складе осталось:')
                return {'Модель': self.name, 'Цена за шт.': self.price, 'Количество': result}
            else:
                raise NotNumber('Вы ввели не число!')
        except NotNumber as er:
            return f'В объекте {self.name} возникла ошибка! {er}'

    @abstractmethod
    def action(self):
        return f'{self.name} - работает'


class Printer(OfficeEquipment):
    @property
    def action(self):
        return f'Принтер {self.name} - печатает'


class Scanner(OfficeEquipment):
    @property
    def action(self):
        return f'Сканер {self.name} - сканирует'


class Xerox(OfficeEquipment):
    @property
    def action(self):
        return f'Ксерокс {self.name} - копирует'


printer_1 = Printer('Phaser 3052', 10000, 10)
scanner_1 = Scanner('DocuMate 3125', 12000, 7)
scanner_2 = Scanner('DocuMate 6480', 16000, 14)
printer_2 = Printer('Phaser 3052', 10000, '3')
xerox_1 = Xerox('B210', 8000, 6)

print(scanner_1)
print(scanner_2)
print(printer_1 + printer_2)
print(xerox_1)
print(scanner_1 - Scanner('DocuMate 3125', 12000, 2))

print('-' * 100)

print(printer_1.action)
print(scanner_1.action)
print(xerox_1.action)

