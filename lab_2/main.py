import numpy as np
from fastest_descent import *
from gradient_method import *
from conjugate_gradients import *
from Newton_method import *
from conjugate_gradients import *
from conjugate_derection import *
from draw3_d_plot import *
from scipy.optimize import minimize
from func_generator import gen_func, condition_numbers
from random import randint


def in_an_interval(number: float):
    return 8 <= number < 10


def test_random_function():
    x0 = [randint(0, 10) for _ in range(10)]
    res = {}
    for n in range(2, 10):
        print("Случайная квадратичная задача для функции " + str(n) + " преременных: ")
        for i in range(10):
            value = gradient_method_ng(gen_func(n), x0, 0.01)
            print("Количество шагов: " + str(value))
            key = condition_numbers[-1]
            if in_an_interval(key):
                res[key] = [value, n]
            print("---------=========--------")
    print(res)


def test():
    x0 = [randint(0, 10) for _ in range(2)]
    index_from_k_dependency = {}
    res = {}
    for i in range(100):
        value = gradient_method_ng(gen_func(2), x0, 0.01)
        key = condition_numbers[-1]
        if value is not None:
            index_from_k_dependency[key] = value
        print("Количество шагов: " + str(value))
        print("---------=========--------")
    for key in sorted(index_from_k_dependency.keys()):
        res[key] = index_from_k_dependency[key]

    return res


if __name__ == '__main__':
    x0 = [10, -9]
    x0_3d = [10, -9, 12]
    x0_4d = [10, -9, 12, -9]
    x0_5d = [10, -9, 12, -9, 10]
    x0_6d = [10, -9, 12, -9, 10, 16]
    # print(Newton_method(func2, dfunc2, x0, d2func2, 0.01))
    # show_first(func, -10, 10)
    # res = minimize(func, x0, method='powell', options={'xtol': 1e-2, 'disp': True})
    # print(fastest_descent(func2,dfunc2,x0,0.01))
    # print(gradient_method(func, x0, 0.01))
    # print(gradient_method_ng(func, x0, 0.01))
    # print(conjugate_directions(func, dfunc, x0, 0.01))
    # print(conjugate_directions(func2, dfunc2, x0, 0.01))
    # print(conjugate_directions(func2, x0, 0.01))
    # print(conjugate_direction_right(func2, 10, -9, 100, 0.1))
    print(gradient_method(func,dfunc,  x0, 0.01))
    print(conjugate_gradient_method(func, dfunc, x0, 0.01))
    # test_random_function()
