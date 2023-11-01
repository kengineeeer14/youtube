a11 = 1; a12 = 2; a21 = -2; a22 = 1
b1 = 4; b2 = -3


# Define the system of equations
A = [[a11, a12], [a21, a22]]  # replace a1, a2, b1, b2 with your coefficients
b = [b1, b2]  # replace c1, c2 with your constants

# Implement Gaussian elimination
x = (b[0]*A[1][1] - b[1]*A[0][1]) / (A[0][0]*A[1][1] - A[0][1]*A[1][0])
y = (b[0] - A[0][0]*x) / A[0][1]

print('Solution:', (x, y))