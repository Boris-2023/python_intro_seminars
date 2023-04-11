#Задача 2: Найдите сумму цифр трехзначного числа

num = input("Enter a value:\t\t")

sum = 0
for i in range(len(num)):
    sum+= int(num[i])

print(f"The sum of digits:\t{sum}")