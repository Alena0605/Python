"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.
"""

# Решение через list
seasons_list = ['Зима', 'Весна', 'Лето', 'Осень']

user_month = int(input('Введите номер месяца: '))

if user_month == 12 or user_month == 1 or user_month == 2:
    print(f'{user_month} - {seasons_list[0]}')
elif 3 <= user_month <= 5:
    print(f'{user_month} - {seasons_list[1]}')
elif 6 <= user_month <= 8:
    print(f'{user_month} - {seasons_list[2]}')
elif 9 <= user_month <= 11:
    print(f'{user_month} - {seasons_list[3]}')
else:
    print('Месяца с таким номером не существует!')

# Решение через dict
seasons_dict = {'season_1': 'Зима', 'season_2': 'Весна', 'season_3': 'Лето', 'season_4': 'Осень'}

user_month = int(input('Введите номер месяца: '))

if user_month == 12 or user_month == 1 or user_month == 2:
    print(f'{user_month} - {seasons_dict["season_1"]}')
elif 3 <= user_month <= 5:
    print(f'{user_month} - {seasons_dict["season_2"]}')
elif 6 <= user_month <= 8:
    print(f'{user_month} - {seasons_dict["season_3"]}')
elif 9 <= user_month <= 11:
    print(f'{user_month} - {seasons_dict["season_4"]}')
else:
    print('Месяца с таким номером не существует!')
