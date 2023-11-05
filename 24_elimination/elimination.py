import numpy as np

def calc_solution(A, b):
    A = A.copy()
    b = b.copy()
    # Perform Gaussian elimination
    n = len(b)
    for i in range(n):
        # Find the pivot element
        pivot = A[i, i]
        if pivot == 0:
            for j in range(i+1, n):
                if A[j, i] != 0:
                    # Swap the current row with the lower row
                    A[[i, j]] = A[[j, i]]
                    b[[i, j]] = b[[j, i]]
                    pivot = A[i, i]
                    break
            else:
                raise ValueError("Matrix is singular")
        # Eliminate the elements below the pivot
        for j in range(i+1, n):
            factor = A[j, i] / pivot
            A[j, i:] -= factor * A[i, i:]
            b[j] -= factor * b[i]

    # Back-substitution to find the solution
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = (b[i] - np.dot(A[i, i+1:], x[i+1:])) / A[i, i]
    return x

if __name__ == '__main__':
    #Define the matrix A and vector b (3by3)
    # A = np.array([[1, 2, 3], [2, 3, 2], [4, -1, 4]], dtype=float)
    # b = np.array([7, 5, 3], dtype=float)
    #Define the matrix A and vector b (2by2)
    A = np.array([[1, 3], [2, 1]], dtype=float)
    b = np.array([4, 3], dtype=float)

    x = calc_solution(A, b)
    # Print the solution
    print("Solution: ", x)