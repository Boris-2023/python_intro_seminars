# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

# *Пример:*
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

def power(base: int, pwr: int) -> int:
    if pwr == 1:
        return base
    else:
        return base*power(base, pwr-1)


base_value = int(input("Enter a value of base:\t"))
power_value = int(input("Enter a value of power:\t"))

print(f"\n{base_value} raised to power {power_value} is:\t{power(base_value, power_value)}")
