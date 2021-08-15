import numpy as np

from draw3_d_plot import show

H = 10 ** (-7)


def find_min(func, x, y, s_x, s_y, accuracy):
    a = -1000
    b = 1000
    while b - a > accuracy:
        f1 = func([x + a * s_x, y + a * s_y])
        f2 = func([x + b * s_x, y + b * s_y])
        c = (a + b) / 2
        if f1 < f2:
            b = c
        else:
            a = c
    return (a + b) / 2


def conjugate_directions(func, x, accuracy):
    x_points = []
    y_points = []
    s = [[1, 0],
         [0, 1]]
    steps = 0
    while True:
        x_points.append(x[0])
        y_points.append(x[1])
        grad_x = (func([x[0] + H, x[1]]) - func([x[0] - H, x[1]])) / (2 * H)
        grad_y = (func([x[0], x[1] + H]) - func([x[0], x[1] - H])) / (2 * H)
        grad_norm = np.sqrt(grad_x ** 2 + grad_y ** 2)
        if grad_norm < accuracy:
            break
        lambda_ = find_min(func, x[0], x[1], s[0][0], s[0][1], accuracy)
        x1 = x[0] + lambda_ * s[0][0]
        y1 = x[1] + lambda_ * s[0][1]
        lambda_ = find_min(func, x1, y1, s[1][0], s[1][1], accuracy)
        x2 = x1 + lambda_ * s[1][0]
        y2 = y1 + lambda_ * s[1][1]
        lambda_ = find_min(func, x2, y2, s[0][0], s[0][1], accuracy)
        x3 = x2 + lambda_ * s[0][0]
        y3 = y2 + lambda_ * s[0][1]
        s[0][0] = x3 - x1
        s[0][1] = y3 - y1
        x = [x3, y3]
        f = func(x)
        steps += 1
    show(func, -10, 10, x_points, y_points, 'conjugate_directions')
    return steps, f
