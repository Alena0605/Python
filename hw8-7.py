"""
7. Реализовать проект «Операции с комплексными числами».
Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение и умножение
созданных экземпляров.
Проверьте корректность полученного результата.
"""


class ComplexNumber:
    def __init__(self, a, b, *args):
        self.a = a
        self.b = b
        self.c = 'a + b * i'

    def __add__(self, other):
        return f'Сумма комплексных чисел:\n' \
               f'c = {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        return f'Произведение комплексных чисел:\n' \
               f'c = {self.a * other.a - (self.b * other.b)} + {self.a * other.b} * i'

    def __str__(self):
        return f'c = {self.a} + {self.b} * i'


c_1 = ComplexNumber(1, 3)
c_2 = ComplexNumber(-2, 8)

print(c_1)
print(c_2)
print(c_1 + c_2)
print(c_1 * c_2)
