"""
2. Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.
"""

time_in_sec = int(input('Введите время в секундах: '))

seconds = time_in_sec % 60
minutes = time_in_sec // 60
hours = minutes // 60
minutes = minutes % 60

print(f'{hours:02}:{minutes:02}:{seconds:02}')
