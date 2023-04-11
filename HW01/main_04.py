# Задача 4: 
# Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. 
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, 
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?


totalNum = int(input("Enter a number of shapes made by all the kids:\t")) #total number of shapes

if totalNum % 6 == 0:
    print(f"Pete, Kate and Serge have accordingly made:\t{totalNum//6}, {totalNum//3*2}, {totalNum//6}")
else: 
    print(f"There is no solution for total number of shapes equal to {totalNum} !")