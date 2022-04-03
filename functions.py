import math


def get_function(num):
    if num == 1:
        return lambda x: math.log(x**3 + math.sqrt(1 - x**3) + 9)
    if num == 2:
        return lambda x: x ** 2 - 3 * x - 2
    if num == 3:
        return lambda x: math.sin(x) - math.cos(x) + 0.2*x
    if num == 4:
        return lambda x: 1/x
    if num == 5:
        return lambda x: x**2 if x < 2 else 2*x
    if num == 6:
        return lambda x: math.sqrt(x)


def get_function_name(num):
    if num == 1:
        return "log(x^3 + sqrt(1 - x^3) + 9)"
    if num == 2:
        return "x^2 - 3x - 2"
    if num == 3:
        return "sin(x) - cos(x) + 0.2x"
    if num == 4:
        return "1/x"
    if num == 5:
        return "x^2 при x < 2, 2x при х >= 2"
    if num == 6:
        return "sqrt(x)"
