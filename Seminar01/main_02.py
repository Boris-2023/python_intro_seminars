#Task 2
# В некоторой школе решили набрать три новых математических класса и оборудовать кабинеты для них новыми партами. 
# За каждой партой может сидеть два учащихся. Известно количество учащихся в каждом из трех классов. 
# Выведите наименьшее число парт, которое нужно приобрести для них.

class1 = int(input("How many pupils in class 1: "))
class2 = int(input("How many pupils in class 2: "))
class3 = int(input("How many pupils in class 3: "))

result = int((class1 + 1) // 2  + (class2 + 1) // 2 + (class3 + 1) // 2) #cannot be less than a day; -.1 чтобы не делилась нацело, иначе 10 и 20 даст 3 дня

print(f"We need minimum {result} desks!")

