import numpy as np

# first way
def matrix_multiplication_1(A, B):
    result = np.zeros((A.shape[0], B.shape[1]))
    for i in range(A.shape[0]):
        for j in range(B.shape[1]):
            for k in range(B.shape[0]):
                result[i][j] += A[i][k] * B[k][j]
    return result

# second way
def matrix_multiplication_2(A, B):
    result = np.zeros((A.shape[0], B.shape[1]))
    for i, B_col in enumerate(B.T):
        result[:,i] = A @ B_col
    return result

# third way
def matrix_multiplication_3(A, B):
    result = np.zeros((A.shape[0], B.shape[1]))
    for i, A_row in enumerate(A):
        result[i,:] = A_row @ B
    return result

# fourth way
def matrix_multiplication_4(A, B):
    result = np.zeros((A.shape[0], B.shape[1]))
    for i in range(A.shape[1]):
        result += A[:, i][:, None] * B[i]
    return result
    

# Define the matrices
A = np.array([[-2, 2, 3], [2, -1, 1]])
B = np.array([[2, 1], [1, 1], [3, 3]])

C1 = matrix_multiplication_1(A, B)
C2 = matrix_multiplication_2(A, B)
C3 = matrix_multiplication_3(A, B)
C4 = matrix_multiplication_4(A, B)

print("\nFirst way: \n", C1)
print("\nSecond way: \n", C2)
print("\nThird way: \n", C3)
print("\nFourth way: \n", C4)
