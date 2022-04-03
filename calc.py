import math


def calc_short_part(func, a, b):
    return ((b-a)/6) * (func(a) + 4*(func((a+b)/2)) + func(b))


def calc_integral(func, a, b):
    if a == b:
        return 0
    mul = 1
    if a > b:
        mul = -1
        a, b = b, a
    i = 0
    i_prev = 100
    n = 10
    d_prev = 0
    while abs(i - i_prev) > 0.0001:
        i_prev = i
        h = (b-a)/n
        i = 0
        for k in range(n):
            try:
                temp_summ = calc_short_part(func, a + h*k, a + h*(k + 1))
            except Exception:
                temp_summ = None
            if temp_summ is not None and temp_summ != math.inf and temp_summ != -math.inf:
                i += temp_summ
        n *= 2
        #print(i, n, abs(i - i_prev))
        if d_prev < abs(i - i_prev) and n > 163840:
            print("Интеграл расходится")
            exit()
        d_prev = abs(i - i_prev)
    return round(i * mul, 4)
