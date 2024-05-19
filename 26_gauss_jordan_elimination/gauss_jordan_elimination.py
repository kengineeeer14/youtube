import numpy as np

def gauss_jordan_inverse(A):
    n = len(A)
    A_inv = np.eye(n)
    
    # Forward elimination
    for i in range(n):
        # Find the pivot element
        pivot = A[i, i]
        if pivot == 0:
            # Search for a non-zero pivot element in lower rows
            for j in range(i+1, n):
                if A[j, i] != 0:
                    # Swap the current row with the lower row
                    A[[i, j]] = A[[j, i]]
                    A_inv[[i, j]] = A_inv[[j, i]]
                    pivot = A[i, i]
                    break
            else:
                raise ValueError("Matrix is singular")
        # Make pivot one
        # A[i] /= pivot
        # A_inv[i] /= pivot
        for j in range(i+1, n):
            factor = A[j, i] / pivot
            A[j] -= factor * A[i]
            A_inv[j] -= factor * A_inv[i]
    
    # Backward elimination
    for i in range(n-1, -1, -1):
        for j in range(i):
            factor = A[j, i] / A[i, i]
            A[j] -= factor * A[i] 
            A_inv[j] -= factor * A_inv[i]

    # Make pivot one
    for i in range(n):
        pivot = A[i, i]
        A[i] /= pivot
        A_inv[i] /= pivot
    
    return A_inv

# Test the function
A = np.array([[1, -2, 0], [-1, 2, -2], [0, -1, 2]], dtype=float)
print("A:\n", A)
print("Inverse of A:\n", gauss_jordan_inverse(A))