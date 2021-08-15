import numpy as np
from random import randint
from scipy.sparse import csr_matrix

def condition_number_matrix(n, k):
    A = csr_matrix(([], [], [0] * (n + 1)), shape=(n, n), dtype=np.float64)
    for i in range(n):
        for j in range(n):
            if i == j:
                A[i, j] = (n - 1) + 10 ** (-k)
            else:
                A[i, j] = -1

    return A


def generate_Gilbert_matrix(n):
    a = np.matrix(np.zeros((n, n)))
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            a[i - 1, j - 1] = 1 / (i + j - 1)
    return csr_matrix(a, dtype=np.float64)


def generate_matrix_with_size(n):
    matrix = np.matrix(np.zeros((n, n)))
    for i in range(n):
        matrix[i, i] = randint(7, 12)

        for j in range(n):
            if i != j:
                previousValues = 0

                for k in range(j):
                    if k != i:
                        previousValues += matrix[i, k]

                randomValue = randint(3, 5)
                newPotentalValue = matrix[i, i] - previousValues - randomValue
                matrix[i, j] = 0 if newPotentalValue < 0 else newPotentalValue
    return csr_matrix(matrix, dtype=np.float64)
