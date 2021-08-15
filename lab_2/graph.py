import matplotlib.pyplot as plt
from main import test




def show_koef():
    index_from_k_dependency = test()
    fig, ax = plt.subplots()
    ax.set(xlabel='Число обусловленности', ylabel='Количество итераций',
           title='Зависимость количества итераций \nот числа обусловленности функции')
    x = index_from_k_dependency.keys()
    y = index_from_k_dependency.values()
    plt.xlim([0, 20])
    plt.plot(x, y)
    ax.grid()
    plt.show()


def show_n():
    x = [2, 3, 4, 5, 6]
    y = [20, 21, 23, 18, 17]
    plt.grid(axis='y', alpha=0.75)
    plt.ylim(0,35)
    plt.xlabel('Размерность пространства')
    plt.ylabel('Количество итераций')
    plt.title('Зависимость итераций  \nот размерности пространства')
    plt.plot(x, y)
    plt.show()

show_n()
