#Task 1
#За день машина проезжает n километров. Сколько дней нужно, чтобы проехать маршрут длиной m километров? 
#При решении этой задачи нельзя пользоваться условной инструкцией if и циклами.

n = int(input("How many km a car can go in a day: "))
m = int(input("How many km is the route to travel: "))

result = int((m + n - .1)) // n #cannot be less than a day; -.1 чтобы не делилась нацело, иначе 10 и 20 даст 3 дня

print(f"To travel {m} km this car needs {result} days!")


