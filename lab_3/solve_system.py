import numpy as np
from scipy.sparse import csr_matrix


def LU(matrix: csr_matrix):
    n = matrix.shape[0]
    U = matrix.copy()
    L = np.matrix(np.zeros((n, n)))
    for k in range(1, n):
        for j in range(k - 1, n):
            for i in range(j, n):
                L[i, j] = U[i, j] / U[j, j]
        for i in range(k, n):
            for j in range(k - 1, n):
                U[i, j] = U[i, j] - L[i, k - 1] * U[k - 1, j]
    return csr_matrix(L), csr_matrix(U)


def Gauss(L: csr_matrix, U: csr_matrix, b: np.array):
    steps = 0
    n = L.shape[0]
    y = np.matrix(np.zeros((n, 1)))
    for i in range(n):
        for j in range(i):
            y[i, 0] -= L[i, j] * y[j, 0]
            steps += 1
        y[i, 0] += b[i, 0]
    x = np.matrix(np.zeros((n, 1)))
    for i in reversed(range(n)):
        x[i, 0] = y[i, 0]
        for j in range(i + 1, n):
            x[i, 0] -= U[i, j] * x[j, 0]
            steps += 1
        x[i, 0] /= U[i, i]
    return x, steps


def inverse_matrix(matrix):
    n = matrix.shape[0]
    LU_ = LU(matrix)
    L = LU_[0]
    U = LU_[1]
    res = np.matrix(np.zeros((n, n)))
    for i in range(n):
        E = np.matrix(np.zeros((n, n)))
        E[i, 0] = 1
        x = Gauss(L, U, E)
        for j in range(n):
            res[j, i] = x[0][j, 0]
    return csr_matrix(res)


def Jacobi(matrix, b, accuracy):
    steps = 0
    n = matrix.shape[0]
    x = np.matrix(np.zeros((n, 1)))
    temp = np.matrix(np.zeros((n, n)))
    b_ = b.copy()
    for i in range(n):
        for j in range(n):
            if j == i:
                temp[i, j] = 0
            else:
                temp[i, j] = matrix[i, j] / matrix[i, i]
        b_[i, 0] /= matrix[i, i]

    for i in range(1000):
        x_prev = x
        x = (b_ - np.dot(temp, x))
        if np.linalg.norm(x - x_prev) < accuracy:
            break
        steps += 1
    return csr_matrix(x), steps


