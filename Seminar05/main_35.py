# Задача 35
# Напишите функцию, которая принимает одно число и проверяет, является ли оно простым

def is_prime_number(num: int) -> bool:
    if num in [1, 2]:
        return True
    elif num % 2 == 0:
        return False
    else:
        for i in range(3, num//2+1, 2):
            if num % i == 0:
                return False
    return True

# def prime_numbers(n, div):
#     if div == n-1:
#         print("YES")
#     elif n % div == 0:
#         print(f"NO, e.g. can be divided by {div}..")
#     else:
#         prime_numbers(n, div + 1)


value = int(input("Enter a value to check if it is a prime one: "))
# prime_numbers(value, 2)

print(f'Value {value} is' + ('' if is_prime_number(value) else ' NOT') + ' a prime number')
