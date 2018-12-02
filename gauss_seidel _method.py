import numpy as np
from scipy.linalg import solve


def gauss(matrix_a, vector_b, vector_x, n):
    lower_triangular = np.tril(matrix_a)
    upper_triangular = matrix_a - lower_triangular
    for i in range(n):
        vector_x = np.dot(np.linalg.inv(lower_triangular), vector_b - np.dot(upper_triangular, vector_x))
        print(str(i).zfill(3))
        print(vector_x)
    return vector_x


'''___MAIN___'''

A = np.array([[4.0, -2.0, 1.0], [1.0, -3.0, 2.0], [-1.0, 2.0, 6.0]])
b = [1.0, 2.0, 3.0]
x = [1, 1, 1]

n = 20

print(gauss(A, b, x, n))
print(solve(A, b))
