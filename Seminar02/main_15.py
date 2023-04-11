
# Задача 15
# Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя, 
# а другой для тещи. Понятно, что для себя нужно выбрать арбуз потяжелей, а для тещи полегче. 
# Но вот незадача: арбузов слишком много и он не знает как же выбрать самый легкий и самый 
# тяжелый арбуз? Помогите ему!

# Пользователь вводит одно число N – количество арбузов. 
# Вторая строка содержит N чисел, записанных на новой строчке каждое. Здесь каждое число – 
# это масса соответствующего арбуза. Все числа натуральные и не превышают 30000.

import random

num_of_melons = int(input("Enter a number of melons:\t"))

min_wgt = 30000
max_wgt = 1

for i in range(num_of_melons):
    wgt = random.randint(5, 25)
    print(wgt, end = " ")
    if wgt < min_wgt:
        min_wgt = wgt
    if wgt > max_wgt:
        max_wgt = wgt

print(f"\n\nmax = {max_wgt}, min = {min_wgt}")