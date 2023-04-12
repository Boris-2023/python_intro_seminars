# Задача 10: 
# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки 
# были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, 
# которые нужно перевернуть

import random

coins_num = int(input("Enter a number of coins on the table:\t"))
heads_num = 0 #counter for heads
for i in range(coins_num):
    coin_side = random.randint(0,1)
    print(coin_side, end = ' ')
    if coin_side == 0:
        heads_num += 1

print(f"\n{heads_num if heads_num < coins_num / 2 else coins_num - heads_num}")
