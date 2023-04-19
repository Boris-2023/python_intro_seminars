# Задача 22: 
# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

import random

size_1 = int(input("Enter a number of elements for 1st set: "))
size_2 = int(input("Enter a number of elements for 2nd set: "))

list_1 = [random.randint(1, 10) for _ in range(size_1)]
list_2 = [random.randint(1, 10) for _ in range(size_2)]

set_common = sorted((set(list_1).intersection(list_2)))

print(f"\nlist #1:\t{list_1}\nlist #2:\t{list_2}\n\nintersection:\t{set_common}")

