#
# i = [1, 31, 13, 24, 27, 43, 64, 65, 32, 3, 6, 8, 4, 7, 12]
# print(i, '- несортированный массив')
#
# asd = int(input('Введите число для которого хотите найти индекс: '))
# i_s = 0
# for j, k in enumerate(i):
#     if asd == k:
#         print(j+1)

#
# for x in range(len(i)):
#     for n in range(len(i)-1):
#         if i[n] > i[n+1]:
#             s = i[n]
#             i[n] = i[n+1]
#             i[n+1] = s
# print(i, '- массив после сортировки по возврастанию')
#
# z = int(input('Введите число для которого хотите найти индекс: '))
#
# first = 0           # хранит индекс первого элемента списка
# mid = len(i)//2     # хранит индекс элемента списка в середине
# last = len(i)-1     # хранит индекс последнего элемента списка
#
# if z == i[first]:
#     print(first + 1)
# elif z == i[last]:
#     print(last + 1)
# # elif z == i[mid]:
# #     print(mid + 1)
# else:
#     while z != i[mid] or last - first == 1:
#         if z > i[mid]:
#             first = mid
#             mid = (mid + last)//2
#         else:
#             last = mid
#             mid = (last - mid)//2
#     print(mid + 1)



# АЛГОРИТМЫ ПОИСКА(i - массив, z - ввод переменной пользователем):



class Chelovek:
    def can_walk(self):
        print('я умею ходить')
    def can_breathe(self):
        print('я умею дышать')
    def can_eat(self):
        print('я умею кушать')
    pass

class Architect(Chelovek):
    def can_build(self):
        print('я умею строить')
    pass

class Architect_3cat(Architect):
    def help_architect(self):
        print('я помогаю главному архитектору')
    def pappers_bringer(self):
        print('я подношу бумажки главному архитектору')

class Doctor(Chelovek):
    def can_heal(self):
        print('я умею лечить')
class Okoolist(Doctor):
    def can_heal_eyes(self):
        print('я умею лечить глаза')
    pass


# АЛГОРИТМЫ ПОИСКА(i - массив, z - ввод переменной пользователем):
class Search:
    @staticmethod
    def search_binar(i, z):           # бинарный поиск индекса в массиве, где z - число из массива для которого ищется индекс
        g = Sort.sort_bubble(i)
        first = 0                           # хранит индекс первого элемента списка
        mid = len(g)//2                     # хранит индекс элемента списка в середине
        last = len(g)-1                     # хранит индекс последнего элемента списка
        if z == g[first]:
            print(first + 1, '- индекс искомого числа')
        elif z == g[last]:
            print(last + 1, '- индекс искомого числа')
        else:
            while z != g[mid] or last - first == 1:
                if z > g[mid]:
                    first = mid
                    mid = (mid + last)//2
                else:
                    last = mid
                    mid = (last - mid)//2
            print(mid + 1, '- индекс искомого числа')


    @staticmethod
    def search_posled(i, z):          # последовательный метод поиска
        var = 0
        while var <= len(i) and var != z:
            if i[var] == z:
                print(var + 1, '- индекс искомого числа')
                break
            else:
                var += 1


    @staticmethod
    def search_perebor(i, z):        # метод поиска перебором
        for n in range(len(i)):
            if z == i[n]:
                print(n + 1, '- индекс искомого числа')


# ФУНКЦИИ СОРТИРОВКИ


class Sort:
    @staticmethod
    def sort_bubble(i):
        for run in range(len(i) - 1):
            for n in range(len(i) - 1 - run):
                if i[n] > i[n + 1]:
                    i[n], i[n + 1] = i[n + 1], i[n]
        return i

    @staticmethod
    def sort_selection(i):
        for n in range(len(i)):
            lowest_index = n
            for j in range(n + 1, len(i)):
                if i[j] < i[lowest_index]:
                    lowest_index = j
            i[n], i[lowest_index] = i[lowest_index], i[n]
        return i

    @staticmethod
    def sort_insertion(i):
        for n in range(len(i)):
            cursor = i[n]
            pos = n
            while pos > 0 and i[pos - 1] > cursor:
                i[pos] = i[pos - 1]
                pos = pos - 1
            i[pos] = cursor
        return i

    @staticmethod
    def sort_gnome(i):
        n, size = 1, len(i)
        while n < size:
            if i[n - 1] <= i[n]:
                n += 1
            else:
                i[n - 1], i[n] = i[n], i[n - 1]
                if n > 1:
                    n -= 1
        return i

    @staticmethod
    def sort_partition(i):
        left = i[0]
        right = i[len(i) - 1]
        while right > left:
            pivot = (left + right) // 2
            part = i[pivot]
            begin = left
            end = right
            while begin <= end:
                while part > i[begin]:
                    begin += 1
                while part < i[end]:
                    end -= 1
                if begin <= end:
                    i[begin], i[end] = i[end], i[begin]
                    begin += 1
                    end -= 1
            if end - left < right - begin:
                i.sort_partition(i, left, end)
                left = begin
            else:
                i.sort_partition(i, begin, right)
                right = end
