from solve_system import LU, inverse_matrix, Jacobi, Gauss
import numpy as np
from scipy.sparse import csr_matrix
from generate_matrix import condition_number_matrix, generate_Gilbert_matrix, generate_matrix_with_size
from draw_graph import show_koef, show_koef_Gilbert, last_task
import time


def test_1():
    a = np.array([[10.0, -7.0, 0.0], [-3.0, 6.0, 2.0], [5.0, -1.0, -5.0]])
    a = csr_matrix(a)
    b = np.array([[1], [2], [3]])
    print("изначальная матрца:")
    print(a.toarray())
    LU_matrix = LU(a)
    print("L:")
    print(LU_matrix[0].toarray())
    print("U:")
    print(LU_matrix[1].toarray())
    print("L*U:")
    print((LU_matrix[0] * LU_matrix[1]).toarray())
    print("обратная матрица:")
    print(inverse_matrix(a).toarray())


def test_4():
    n = 35
    y = []
    x1 = []
    x2 = []
    for i in range(1, 15):
        y.append(i)
        A = condition_number_matrix(n, i)
        b = np.matrix(np.zeros((n, 1)), dtype=np.float64)
        for j in range(n):
            b[j, 0] = j + 1
        LU_matrix = LU(A)
        J = np.linalg.norm((A * Jacobi(A, b, 0.001)[0] - A * b))  # норма матрицы
        G = np.linalg.norm((A * Gauss(LU_matrix[0], LU_matrix[1], csr_matrix(b))[0] - A * b))
        x1.append(J)
        x2.append(G)
        print('Jacobi:', J)
        print('Gauss', G)
    show_koef(x1, x2, y)


def test_5():
    y = []
    x2 = []
    for n in range(3, 50):
        y.append(n)
        A = generate_Gilbert_matrix(n)
        b = np.matrix(np.zeros((n, 1)), dtype=np.float64)
        for j in range(n):
            b[j, 0] = j + 1
        LU_matrix = LU(A)
        #  J = np.linalg.norm((A * Jacobi(A, b, 0.001)[0] - A * b))  # норма матрицы
        G = np.linalg.norm((A * Gauss(LU_matrix[0], LU_matrix[1], csr_matrix(b))[0] - A * b))
        x2.append(G)
        # print('Jacobi:', J)
        print("n =", n, 'Gauss', G)
    show_koef_Gilbert(x2, y)


def test_6(n):
    a = generate_matrix_with_size(n)
    b = np.matrix(np.zeros((n, 1)), dtype=np.float64)
    for j in range(n):
        b[j, 0] = j + 1

    start = time.time()
    J = Jacobi(a, b, 0.001)
    print("Jacobi steps:", J[1])
    print('Time for Jacobi:', time.time() - start)

    start = time.time()
    LU_matrix = LU(a)
    G = Gauss(LU_matrix[0], LU_matrix[1], csr_matrix(b))
    print("Gauss steps:", G[1])
    print('Time for Gauss:', time.time() - start)


if __name__ == '__main__':
    test_1()
    test_4()
    test_5()
    test_6(10)

