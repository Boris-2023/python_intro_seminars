# Задача №41.
# Дан массив, состоящий из целых чисел. Напишите
# программу, которая в данном массиве определит
# количество элементов, у которых два соседних и, при
# этом, оба соседних элемента меньше данного. Сначала
# вводится число N — количество элементов в массиве
# Далее записаны N чисел — элементы массива. Массив
# состоит из целых чисел.

import random


def tops(list_1: int) -> int:
    if len(list_1) < 3:
        return 0
    else:
        tops_num = 0
        for i in range(1, len(list_1)-1):
            if list_1[i] > list_1[i-1] and list_1[i] > list_1[i+1]:
                tops_num += 1
    return tops_num


num = int(input("Enter a size of the list:\t"))
my_list = [random.randint(1, 10) for _ in range(num)]
print(f"the list: {my_list}")

print(f"\nnumber of tops in the list is {tops(my_list)}")
