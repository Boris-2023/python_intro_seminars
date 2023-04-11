# Задача №11. Решение в группах
# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6

value = int(input("Enter a value:\t"))

# val_prev1 = 0
# val_prev2 = 1
# val_cur = 1
# cnt = 2

# while val_cur < value:
#     val_cur = val_prev1 + val_prev2
#     val_prev1 = val_prev2
#     val_prev2 = val_cur
#     cnt += 1

# if val_cur == value :
#      print(f"{cnt}")
# else :
#      print("-1")

     
first = 0
second = 1
index = 2

while second < value:
     first, second = second, first + second
     index+=1

print(index if second == value else -1)