# Задача 6: 
# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме 
# последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
# Вам требуется написать программу, которая проверяет счастливость билета.

ticketNum = input("Enter 6-digit number of ticket:\t")

numLen = len(ticketNum)

if numLen == 6:

    sumLeft = sumRight = 0
    
    for i in range(3):
        sumLeft+= int(ticketNum[i])
        sumRight+= int(ticketNum[i+3])

    if sumLeft == sumRight:
        print("YES, it is your LUCKY ticket!")
    else:
        print("NO, this ticket is not lucky..")

else: 
    print("Ticket number must be of 6 digits! Try again..")