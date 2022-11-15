from stepik import Search, Sort
import time, random


# Код для поиска индекса
#
# i = [1, 23, 432, 423, 53, 12, 43, 8, 76, 6, 9, 80]
# i.sort()
# print(i)
# z = int(input('Введите число из массива: '))
# start_time = time.time()        # Для того чтобы заработал таймер, напишите свой код ниже
# Search.search_binar(i, z)
#
# print("--- %s seconds ---" % (time.time() - start_time))        # Строчка выводит время исполнения программы


# Код для сортировки

i = list(range(0, 50))
random.shuffle(i)
# i = [1, 23, 432, 423, 53, 12, 43, 8, 76, 6, 9, 24134, 80, 34, 54, 364, 23523]
print(i, '- массив до сортировки')
start_time = time.time()        # Для того чтобы заработал таймер, напишите свой код ниже
g = Sort.sort_partition(i)
print(g, '- массив после сортировки')

print("--- %s seconds ---" % (time.time() - start_time))        # Строчка выводит время исполнения программы


# в классы человек архитектор обьявить финкции в privat public protected
# сделать репозиторий на гит(нехаб) и закинуть все свои проги
