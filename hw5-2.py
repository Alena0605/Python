"""
2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

with open('hw5-2.txt') as f:
    cnt_lines = 0
    cnt_all_words = 0
    for line in f.read().splitlines():
        cnt_lines += 1
        cnt_words = 0
        for word in line.split():
            cnt_words += 1
            cnt_all_words += 1
        print(f'Количество слов в {cnt_lines} строке - {cnt_words}.')

print(f'\nИТОГО:\nКоличество строк: {cnt_lines}\nКоличество всех слов: {cnt_all_words}')
