# 37
# Дано натуральное число N и последовательность из N элементов. Требуется вывести эту последовательность в обратном порядке.


def rev(n: int, s='') -> str:
    if n != 0:
        return s + str(n) + " " + rev(n-1)
    else:
        return s


n = int(input("Enter a number: "))
print(f"{rev(n)}\n")
