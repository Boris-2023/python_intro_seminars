# Задача 28:
# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

def summa(value_1: int, value_2: int) -> int:
    if value_2 == 0:
        return value_1
    else:
        return summa(value_1 + 1, value_2 - 1)


item_1 = int(input("Enter an item #1: "))
item_2 = int(input("Enter an item #2: "))

print(f"\n{item_1} + {item_2} = {summa(item_1, item_2)}")
