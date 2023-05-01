# Задача 30:  
# Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов 
# нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

#def arythm_progr(el_1: int, step: int, num: int) -> list:

elem_1 = int(input("enter the 1st value of progression:\t"))
step = int(input("enter the step of the progression:\t"))
size = int(input("enter the number of element to print:\t"))

print(f"\narithmetical progression:\n{[i for i in range(elem_1, size*step+1, step)]}")