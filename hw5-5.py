"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

with open('hw5-5.txt', 'w') as f:
    numbers = input('Enter some numbers separated by space: ').split()
    f.write(' '.join(numbers))
    sum_num = sum(map(int, numbers))
    f.write(f'\nSum of numbers is: {sum_num}')

print(f'Sum of numbers is: {sum_num}')
