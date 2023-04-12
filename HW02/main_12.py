# Задача 12: 
# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), 
# а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму 
# этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

sum = int(input("Enter the sum of values:\t"))
prod = int(input("Enter the product of values:\t"))

if sum > 0 and prod > 0 and sum <= 2000 and prod <= 1000000:
    descr = sum*sum - 4*prod

    if descr >= 0:
        print(f"The values are: {int((sum - pow(descr, .5))/2)} and {int((sum + pow(descr, .5))/2)}")
    else:
        print("There are no such values!!!")
else:
    print("Both values must be in range 1 -> 1000, try again!")
