# метод градиентного спуска (2)
import numpy as np
from draw3_d_plot import show
from functions import gradient, diff


def gradient_method(func, dfunc, x, accuracy):
    steps = 0
    lambda_ = 0.1
    x_points = []
    y_points = []
    f = func(x)
    while True:
        f_prev = f
        x_points.append(x[0])
        y_points.append(x[1])
        x = x - lambda_ * np.array(dfunc(x))
        f = func(x)
        if np.abs(f_prev - f) < accuracy:  # сходимость по функции
            show(func, -10, 10, x_points, y_points, "gradient_method")
            return steps, func(x)
        if steps == 1000:
            print("Метод разошелся " + str(steps))
            break
        steps += 1


def golden_section_method_ng(func, x, grad_, accuracy):
    a = -1000
    b = 1000
    phi = (np.sqrt(5) + 1) / 2
    x1 = a + (b - a) / (phi + 1)
    x2 = b - (b - a) / (phi + 1)
    f1 = func(*(x - grad_ * x1))
    f2 = func(*(x - grad_ * x2))
    while b - a > accuracy:
        if f1 >= f2:
            a = x1
            x1 = x2
            f1 = f2
            x2 = b - (b - a) / (phi + 1)
            f2 = func(*(x - grad_ * x2))
        else:
            b = x2
            x2 = x1
            f2 = f1
            x1 = a + (b - a) / (phi + 1)
            f1 = func(*(x - grad_ * x1))
    return (a + b) / 2


def gradient_method_ng(func, x, accuracy):
    steps = 0
    while True:
        x_prev = x
        grad_ = gradient(func,x)
        grad_ = np.array(grad_)
        lambda_ = golden_section_method_ng(func, x, grad_, accuracy)
        x = x - lambda_ * grad_
        if diff(x, x_prev) < accuracy:  # сходимость по функции
            return steps
        if steps == 1000:
            print("Метод разошелся " + str(steps))
            break
        steps += 1
