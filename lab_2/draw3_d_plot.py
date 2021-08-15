import numpy as np
import matplotlib.pyplot as plt


def show_first(func, a, b):
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1, projection='3d')
    x = []
    x1, y1 = np.mgrid[a:b:100j, a:b:100j]
    x.append(x1)
    x.append(y1)
    ax.contour(x[0], x[1], func(x), levels=100, cmap='viridis')
    plt.show()


def show(func, a, b, x_points, y_points, graph_name):
    fig = plt.figure()
    x = []
    ax = fig.add_subplot(1, 1, 1, projection='3d')
    ax.set_title(graph_name)
    x1, y1 = np.mgrid[a:b:100j, a:b:100j]
    x.append(x1)
    x.append(y1)
    ax.contour(x1, y1, func(x), levels=100, cmap='viridis')

    points_func = []
    for i in range(len(x_points)):
        points_func.append(func([x_points[i], y_points[i]]))
        ax.scatter(x_points[i], y_points[i], func([x_points[i], y_points[i]]), c='deeppink')

    ax.plot([x_points[i] for i in range(len(x_points))], [y_points[i] for i in range(len(y_points))],
            [points_func[i] for i in range(len(points_func))], c='deeppink')
    plt.show()
