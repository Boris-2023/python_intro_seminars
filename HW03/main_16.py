
# Задача 16:
# Требуется вычислить, сколько раз встречается некоторое число X в списке A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов списка.
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X

import random

list_size = int(input("Enter a length of the list:\t"))
value = int(input("Enter a value from 1 to 10:\t"))

my_list = [random.randint(1, 10) for i in range(list_size)]

print(my_list, '\n')

cnt = 0
for i in range(list_size):
    if my_list[i] == value:
        cnt += 1

print("The value", value, "encounters", cnt, "times in the list")
