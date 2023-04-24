# Задача 33. 
# Хакер Василий получил доступ к классному журналу и хочет 
# заменить все свои минимальные оценки на максимальные. 
# Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.

# Задача №33.
# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

import random

num_marks = int(input("Enter a number marks for Vasiliy: "))
marks = [random.randint(1,5) for _ in range(num_marks)]

print(marks)

max_mark = max(marks)
min_mark = min(marks)

for i in range(num_marks):
    if marks[i] == max_mark:
        marks[i] = min_mark

print(marks)