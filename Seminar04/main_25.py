# Задача №25.
# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.

str_split = input("Enter a set of symbols separated by space ' ':\t").split()

#print(f"\nString as a list: {str_split}\n")

res = {}
for i in str_split:
    if i in res:
        print(f'{i}_{res[i]}', end=' ')
    else:
        print(i, end=' ')
        
    res[i] = res.get(i, 0) + 1

print("\n")
