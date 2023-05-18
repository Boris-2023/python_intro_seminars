# Задача №43.
# Дан список чисел. Посчитайте, сколько в нем пар
# элементов, равных друг другу. Считается, что любые
# два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список
# чисел. Все числа списка находятся на разных
# строках.

import random

num = int(input("Enter a size of the list:\t"))
my_list = [random.randint(1, 10) for _ in range(num)]
print(f"the list: {my_list}")

print(f"\ntotal number of pairs: {sum(my_list.count(item) - 1 for item in my_list) // 2}")# all values with all values, 
print(f"number of uique pairs: {sum(my_list.count(i) // 2 for i in set(my_list))}")# any member of counted pair will no longer patricipate 

