# Нахождение индекса в массиве чисел

i = [1, 31, 13, 24, 27, 43, 64, 65, 32, 3, 6, 8, 4, 7, 12]
print(i, '- несортированный массив')

asd = int(input('Введите число для которого хотите найти индекс: '))

for j, k in enumerate(i):
    if asd == k:
        print(j+1)

