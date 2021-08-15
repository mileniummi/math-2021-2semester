import numpy as np


def func(x):
    return np.sin(x) * np.power(x, 3)


def func2(x):
    return np.sin(x) - np.log(np.power(x, 2)) - 1


def func3(x):
    return np.power(x, 4) + np.power(x, 3) + 3 * x + 12

def func4(x):
    return np.exp(np.sin(x)) * np.power(x,2)


def fibonacci(n):
    x1 = 0
    x2 = 1
    for i in range(0, n - 1):
        sum = x1 + x2
        x1 = x2
        x2 = sum
    return x2


# метод дихотомии
def dichotomy_method(func, a, b, accuracy):
    delta_a_b = np.abs(a - b)
    delta = accuracy / 2
    function_calcs = 0
    distance = []
    step = 0
    delta_a_b_prev =0
    while delta_a_b > accuracy:
        delta_a_b_prev = delta_a_b;
        x1 = ((a + b - delta) / 2)
        x2 = ((a + b + delta) / 2)
        x1_value = func(x1)
        x2_value = func(x2)
        function_calcs += 2
        if x1_value > x2_value:
            a = x1
        else:
            b = x2
        delta_a_b = np.abs(a - b)
        distance.append([delta_a_b/delta_a_b_prev])
        step += 1
    print(distance)
    return distance, function_calcs, func(a), a


# метод золотого сечения
def golden_section_method(func, a, b, accuracy):
    delta_a_b = np.abs(a - b)
    function_calcs = 0
    distance = []
    phi = 2 - ((1 + np.sqrt(5)) / 2)
    x1 = a + phi * delta_a_b
    x2 = b - phi * delta_a_b
    x1_value = func(x1)
    x2_value = func(x2)
    function_calcs += 2
    step = 0
    while delta_a_b > accuracy:
        delta_a_b_prev = delta_a_b
        if x1_value < x2_value:
            b = x2
            x2 = x1
            x2_value = x1_value
            x1 = a + phi * np.abs(a - b)
            x1_value = func(x1)
            function_calcs += 1
        else:
            a = x1
            x1 = x2
            x1_value = x2_value
            x2 = b - phi * np.abs(a - b)
            x2_value = func(x2)
            function_calcs += 1
        delta_a_b = np.abs(a - b)
        distance.append([delta_a_b/delta_a_b_prev])
        step += 1
    print(distance)
    return step, function_calcs, func(a), a


# метод Фибоначи
def Fibonacci_method(func, a, b, accuracy):
    delta_a_b = np.abs(a - b)
    n = 1
    distance = []
    function_calcs = 0
    while fibonacci(n + 2) < delta_a_b / accuracy:
        n += 1
    x1 = a + (fibonacci(n) / fibonacci(n + 2)) * delta_a_b
    x2 = a + (fibonacci(n + 1) / fibonacci(n + 2)) * delta_a_b
    x1_value = func(x1)
    x2_value = func(x2)
    function_calcs += 2
    steps = n
    while delta_a_b > accuracy:
        delta_a_b_prev = delta_a_b
        if x1_value <= x2_value:
            n -= 1
            b = x2
            x2 = x1
            x2_value = x1_value
            x1 = a + (fibonacci(n) / fibonacci(n + 2)) * np.abs(a - b)
            x1_value = func(x1)
            function_calcs += 1
        else:
            n -= 1
            a = x1
            x1 = x2
            x1_value = x2_value
            x2 = a + (fibonacci(n + 1) / fibonacci(n + 2)) * np.abs(b - a)
            x2_value = func(x2)
            function_calcs += 1
        delta_a_b = np.abs(a - b)
        distance.append([delta_a_b/delta_a_b_prev])

    res = (a + b) / 2.0
    print(distance)
    return steps, function_calcs, func(res), res


# метод парабол
def parabola_method(func, a, b, accuracy):
    x1 = a
    x2 = a + (np.abs(b - a) / 2)
    x3 = b
    function_calcs = 0
    f1 = func(x1)
    f2 = func(x2)
    f3 = func(x3)
    function_calcs += 3
    steps = 0
    u_prev = b
    u = b + accuracy + 1
    while np.abs(u - u_prev) > accuracy:
        u_prev = u
        u = x2 - ((np.power((x2 - x1), 2) * (f2 - f3) - np.power((x2 - x3), 2) * (f2 - f1)) / (
                2 * ((x2 - x1) * (f2 - f3) - (x2 - x3) * (f2 - f1))))
        fu = func(u)
        function_calcs += 1
        if x1 < u < x2 < x3:
            if fu >= f2:
                x1 = u
                f1 = fu
            else:
                x3 = x2
                f3 = f2
                x2 = u
                f2 = fu
        else:
            if fu > f2:
                x3 = u
                f3 = fu
            else:
                x1 = x2
                f1 = f2
                x2 = u
                f2 = fu
        steps += 1
    return steps, function_calcs, func(u), u


# Комбинированный метод Брента
def Brent_method(func, a, b, accuracy):
    c = b
    function_calcs = 0
    steps = 0
    k = (3 - np.sqrt(5)) / 2
    x = w = v = (a + c) / 2
    fx = fw = fv = func(x)
    function_calcs += 1
    delta_a_c = e = np.abs(c - a)
    while True:
        if max((x - a), (c - x)) < accuracy:
            return steps, function_calcs, func(x), x
        g = e
        e = delta_a_c
        u = w - ((np.power((w - x), 2) * (fw - fv) - np.power((w - v), 2) * (fw - fx)) / (
                2 * ((w - x) * (fw - fv) - (w - v) * (fw - fx))))
        if np.isnan(u) or u < a or u > c or np.abs(u - x) > g / 2:
            if x < (a + c) / 2:
                u = x + k * (c - x)  # golden_section
                delta_a_c = c - x
            else:
                u = x - k * (x - a)  # golden section
                delta_a_c = x - a
        fu = func(u)
        function_calcs += 1
        if fu <= fx:
            if u >= x:
                a = x
            else:
                c = x
            v = w
            w = x
            x = u
            fv = fw
            fw = fx
            fx = fu
        else:
            if u >= x:
                c = u
            else:
                a = u
            if fu < fw or w == x:
                v = w
                w = u
                fv = fw
                fw = fu
            elif fu <= fv or v == x or v == w:
                v = u
                fv = fu
        steps += 1


def main():
    #print(dichotomy_method(func4, -2, 6, 0.001))
    #print(golden_section_method(func4, -2, 6, 0.001))
    print(Fibonacci_method(func4, -2, 6, 0.001))
    #print(parabola_method(func4, -2, 6, 0.001))
    #print(Brent_method(func4, -2, 6, 0.001))


if __name__ == '__main__':
    main()
