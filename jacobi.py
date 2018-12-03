from pprint import pprint
from numpy import array, zeros, diag, diagflat, dot


def jacobi(matrix_a, vector_b, iteration_number=25, vector_x=None):
    """Solves the equation Ax=b via the Jacobi iterative method."""
    # Create an initial guess if needed
    if vector_x is None:
        vector_x = zeros(len(matrix_a[0]))

    # Create a vector of the diagonal elements of A
    # and subtract them from A
    diagonal_matrix = diag(matrix_a)
    R = matrix_a - diagflat(diagonal_matrix)

    # Iterate for N times
    for i in range(iteration_number):
        vector_x = (vector_b - dot(R, vector_x)) / diagonal_matrix
    return vector_x


a = array([[2.0, 1.0], [5.0, 7.0]])
b = array([11.0, 13.0])
guess = array([1.0, 1.0])

sol = jacobi(a, b, iteration_number=25, vector_x=guess)

print("A:")
pprint(a)

print("b:")
pprint(b)

print("x:")
pprint(sol)
