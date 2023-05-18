# Задача №39. Решение в группах
# Даны два массива чисел. Требуется вывести те элементы
# первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит
# число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество
# элементов во втором массиве. Затем элементы второго массива

import random

num_1 = int(input("Enter the size of list #1:\t"))
num_2 = int(input("Enter the size of list #2:\t"))

list_1 = [random.randint(1, 10) for _ in range(num_1)]
list_2 = [random.randint(1, 10) for _ in range(num_2)]

print(f"list #1: {list_1}")
print(f"list #2: {list_2}")
print(f"result : {[item for item in list_1 if item not in list_2]}")