import matplotlib.pyplot as plt


def show_koef(x1, x2, y):
    fig, ax = plt.subplots()
    ax.set(xlabel='Число обусловленности k')
    plt.plot(y, x1, label="Jacobi")
    plt.plot(y, x2, label="Gauss")
    plt.legend()
    ax.grid()
    plt.show()


def show_koef_Gilbert(x1, y):
    fig, ax = plt.subplots()
    ax.set(xlabel='Размерность пространства  n')
    plt.plot(y, x1, label="Jacobi")
    plt.legend()
    ax.grid()
    plt.show()


def last_task():
    fig, ax = plt.subplots()
    y = [10, 50, 100]
    x1 = [17, 17, 21]
    x2 = [90, 2450, 9900]
    ax.set(ylabel='Количество итераций', xlabel='Размерность марицы',
           title="Зависимость количества итераций \nот размерности матрицы")
    plt.plot(y, x1, label="Jacobi")
    plt.plot(y, x2, label="Gauss")
    plt.legend()
    ax.grid()
    plt.show()
