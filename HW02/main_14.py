# Задача 14: 
# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

max_value = int(input("Enter the maximum value to print:\t"))

print("\n")

val = 1
while val < max_value:
    print(val, end = ' ')
    val *= 2

print("\n")