# 45
# Два различных натуральных числа n и m называются дружественными, если сумма
# делителей числа n (включая 1, но исключая само n) равна числу m и наоборот.
# Например, 220 и 284 – дружественные числа. По данному числу k выведите все
# пары дружественных чисел, каждое из которых не превосходит k. Программа получает
# на вход одно натуральное число k, не превосходящее 105. Программа должна вывести
# все пары дружественных чисел, каждое из которых не превосходит k.

# num = int(input("Enter the limit for values:\t"))
num = 10001

# ------------> basic
# def find_dividers(val: int) -> list:
#     return [i for i in range(1, val//2 + 1) if val % i == 0]

# for i in range(1, num):
#     sum_cur = sum(find_dividers(i))
#     for j in range(i + 1, num):
#         if sum_cur == j and sum(find_dividers(j)) == i:
#             print(f"{i} \U0001F91D {j}")
#             break


# ------------> nice Python
def sum_dividers(number: int) -> int:
    sum_div = 0
    for div in range(1, number//2 + 1):
        if not number % div:
            sum_div += div
    return sum_div


for num_test in range(num):
    sum_cur = sum_dividers(num_test)
    if num_test == sum_dividers(sum_cur) and num_test < sum_cur:
        print(num_test, sum_cur, sep='\U0001F91D')


# -----------> chatGPT
# import math

# def sum_of_divisors(n):
#     sum = 1
#     for i in range(2, int(math.sqrt(n))+1):
#         if n % i == 0:
#             sum += i
#             if i != n/i:
#                 sum += n/i
#     return sum

# k = int(input())

# for i in range(1, k+1):
#     sum1 = sum_of_divisors(i)
#     if sum1 <= k:
#         sum2 = sum_of_divisors(sum1)
#         if sum2 == i and i < sum1:
#             print(i, sum1)
