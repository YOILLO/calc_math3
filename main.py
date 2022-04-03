from calc import *
from functions import *

for i in range(6):
    print(f"{i+1}: {get_function_name(i+1)}")

num = -1
while num <= 0 or num >= 7:
    try:
        num = int(input("Выебрите фукнцию: "))
    except Exception:
        print("Введите число")

a = -1
b = -1
while True:
    try:
        a = float(input("Введите a: "))
        b = float(input("Введите b: "))
        if (a == b):
            print("Введите разные числа")
        break
    except Exception:
        print("Введите числа")

print(f"Ответ: {calc_integral(get_function(num), a, b)}")
