# задание 1: реализовать методы спуска
import numpy as np
from functions import *

from draw3_d_plot import show


# метод наискорейшего спуска (1) лямда выбраннна золотым сечением
def fastest_descent(func, dfunc, x, accuracy):
    steps = 0
    x_points = []
    y_points = []
    f = func(x)
    while True:
        grad_ = dfunc(x)
        x_prev = x
        lambda_ = Fibonacci_method(func, x, grad_, accuracy)
        f_prev = f
        x_points.append(x[0])
        y_points.append(x[1])
        x = x - lambda_ * np.array(dfunc(x))
        f = func(x)
        if np.abs(f_prev - f) < accuracy and abs(x[0] - x_prev[0]) < accuracy and abs(x[0] - x_prev[0]) < accuracy:  # сходимость по аргументу
            show(func, -10, 10, x_points, y_points, "fastest_descent")
            return steps, func(x)
        steps += 1
