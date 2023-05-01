# Задача 32: 
# Определить индексы элементов массива (списка), значения которых 
# принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

import random

num = int(input("Enter a size of the list:\t"))
my_min = int(input("Enter a minimum to compare:\t"))
my_max = int(input("Enter a maximum to compare:\t"))

my_list = [random.randint(1, 10) for _ in range(num)]
print(f"the list: {my_list}")

print(f"\nindexes of elements whithin the range:\n{[i for i in range(num) if my_list[i] >= my_min and my_list[i] <= my_max]}")

