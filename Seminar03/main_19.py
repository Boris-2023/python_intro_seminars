#19. Дана последовательность
# из N целых чисел и число K.
# Необходимо сдвинуть всю
# последовательность
# (сдвиг - циклический) на
# K элементов вправо,
# K – положительное число

import random

val_n = int(input("Enter a length of list:\t"))
val_k = int(input("Enter a shift value:\t"))

my_list = [random.randint(0,100) for i in range(val_n)]
print(my_list, '\n')

for _ in range(val_k):
    my_list.insert(0, my_list.pop())

print(my_list)






