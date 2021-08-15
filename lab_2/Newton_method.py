import numpy as np

from draw3_d_plot import show


def Newton_method(func, dfunc,x,  d_2_func, accuracy):
    steps = 0
    dx_1 = dfunc(x)  # первая производная
    dx_2 = d_2_func(x)  # вторая производная
    dx_1 = np.array(dx_1)
    dx_2 = np.array(dx_2)
    x_points = []
    y_points = []
    x_points.append(x[0])
    y_points.append(x[1])
    while (dx_2[0] != 0) and (dx_2[1] != 0) and (np.abs(dx_1[0]) > accuracy) and (np.abs(dx_1[1]) > accuracy):
        x = x - dx_1 / dx_2
        x_points.append(x[0])
        y_points.append(x[1])
        dx_1 = dfunc(x)
        dx_2 = d_2_func(x)
        dx_1 = np.array(dx_1)
        dx_2 = np.array(dx_2)
        steps += 1
        if steps == 100:
            break
    show(func, -10, 10, x_points, y_points, 'Newton_method')
    return func(x),steps
