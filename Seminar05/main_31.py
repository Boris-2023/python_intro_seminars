# Задача 31 
# Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ..., где
# a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи

def fibo(n):
    if n in [0, 1]:
        return n
    return fibo(n-1) + fibo(n-2)
    
n = int(input("Enter a number: "))
print(f"The element #{n} of Fibo sequence is: {fibo(n)}")