import numpy as np


from draw3_d_plot import show


def golden_section_method_cgm(func, s, p, accuracy):
    a = 0
    b = 1e5
    delta_a_b = np.abs(a - b)
    phi = 2 - ((1 + np.sqrt(5)) / 2)
    x1 = a + phi * delta_a_b
    x2 = b - phi * delta_a_b
    while delta_a_b > accuracy:
        point_1 = s + x1 * p
        point_2 = s + x2 * p
        f1 = func(point_1)
        f2 = func(point_2)
        if f1 < f2:
            b = x2
        else:
            a = x1
        x2 = x1
        x1 = b + a - x2
        delta_a_b = np.abs(a - b)
    return (a + b) / 2


def conjugate_gradient_method(f, gradf,x, accuracy):
    # f функция, gradf ее градиент
    x_points = []
    y_points = []
    p = gradf(x)
    p = np.array(p) * (-1)
    grad_square = np.dot(p, p)
    steps = 0
    while True:
        lambda_ = golden_section_method_cgm(f, x, p, 0.01)
        x_points.append(x[0])
        y_points.append(x[1])
        x = x + lambda_ * p
        new_grad = gradf(x)
        new_grad = np.array(new_grad) * (-1)
        new_grad_square = np.dot(new_grad, new_grad)

        if steps % (5 * 2) == 0:
            beta = 0
        else:
            beta = new_grad_square / grad_square
        p = new_grad + beta * p
        steps += 1
        grad_square = new_grad_square
        if grad_square < accuracy:
            break
    show(f, -10, 10, x_points, y_points, "conjugate_gradient")
    return f(x), steps
