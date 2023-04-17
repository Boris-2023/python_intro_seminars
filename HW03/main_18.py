# Задача 18:
# Требуется найти в списке A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов списка.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

import random

max_val = 100  # max value in the list

list_size = int(input("Enter a length of the list:\t"))
value = int(input("Enter a value from 1 to 100:\t"))

my_list = [random.randint(1, max_val) for i in range(list_size)]

print(my_list, '\n')

min_diff = 100
index_val_found = 0
for i in range(list_size):
    cur_diff = abs(my_list[i] - value)
    if cur_diff < min_diff:
        min_diff = cur_diff
        index_val_found = i
        if min_diff == 0:
            break  # no need to find better

print("The closest value to", value, "is the element #",
      index_val_found + 1,", which is equal to", my_list[index_val_found])
