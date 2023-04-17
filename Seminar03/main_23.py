# 23. Дан список, состоящий из целых чисел. Напишите программу, 
# которая подсчитает количество элементов списка, больших предыдущего (элемента с предыдущим номером)

import random

val = int(input("Enter a length of list:\t"))
my_list = [random.randint(0, 5) for i in range(val)]

cnt = 0
for i in range(1, len(my_list)):
    if my_list[i] > my_list[i-1]:
        cnt+=1

print(my_list,'\n',cnt)
