import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the vectors
a1 = np.array([[1], [2], [3]])
a2 = np.array([[2], [3], [2]])
a3 = np.array([[4], [-1], [4]])

A = np.column_stack((a1, a2, a3))
b = np.array([[7], [5], [3]])
# print(A)
Ainv = np.linalg.inv(A) # Inverse of A
x = Ainv@b              # Solution to Ax = b

# Create the figure and axes
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Set the limits of the axes
ax.set_xlim([-10, 10])
ax.set_ylim([-10, 10])
ax.set_zlim([-10, 10])

# Plot the vectors
ax.quiver(0, 0, 0, a1[0], a1[1], a1[2], color='red')
ax.quiver(0, 0, 0, a2[0], a2[1], a2[2], color='red')
ax.quiver(0, 0, 0, a3[0], a3[1], a3[2], color='red')
ax.quiver(0, 0, 0, b[0], b[1], b[2], color='blue')
ax.quiver(0, 0, 0, x[0]*a1[0], x[0]*a1[1], x[0]*a1[2], color = "green")
ax.quiver(x[0]*a1[0], x[0]*a1[1], x[0]*a1[2], (x[0]*a1[0]+x[1]*a2[0])-x[0]*a1[0], (x[0]*a1[1]+x[1]*a2[1])-x[0]*a1[1], (x[0]*a1[2]+x[1]*a2[2])-x[0]*a1[2], color = "green")
ax.quiver((x[0]*a1[0]+x[1]*a2[0]), (x[0]*a1[1]+x[1]*a2[1]), (x[0]*a1[2]+x[1]*a2[2]), (x[0]*a1[0]+x[1]*a2[0]+x[2]*a3[0])-(x[0]*a1[0]+x[1]*a2[0]), (x[0]*a1[1]+x[1]*a2[1]+x[2]*a3[1])-(x[0]*a1[1]+x[1]*a2[1]), (x[0]*a1[2]+x[1]*a2[2]+x[2]*a3[2])-(x[0]*a1[2]+x[1]*a2[2]), color = "green")
# Set the labels for the axes
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Show the plot
# plt.savefig("23_matrix_product_geometry_interpretation/figure/column3by3.png")  
plt.show()