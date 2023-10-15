import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

a1 = np.array([2, 1, 2])
a2 = np.array([1, 1, 1])
a3 = np.array([3, 2, 1])

# A = np.column_stack((a1, a2, a3))
A = np.array([a1, a2, a3])
b = np.array([4, 4, 4])

# Define the x and y coordinates of the surface
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)

# Define the function that defines the surface
Z1 = b[0]/a1[2] - a1[0]/a1[2]*X - a1[1]/a1[2]*Y
Z2 = b[1]/a2[2] - a2[0]/a2[2]*X - a2[1]/a2[2]*Y
Z3 = b[2]/a3[2] - a3[0]/a3[2]*X - a3[1]/a3[2]*Y

# Create the figure and axes
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the surface
ax.plot_surface(X, Y, Z1, alpha=0.2)
ax.plot_surface(X, Y, Z2, alpha=0.2)
ax.plot_surface(X, Y, Z3, alpha=0.2)

# Plot the line where surface intersects
# a1 and a2
c12 = a1[2]/a2[2]
a2_d = c12*a2; b2_d = c12*b[1]
diffa12 = a1 - a2_d; diffb12 = b[0] - b2_d
a12 = -diffa12[0]/diffa12[1] # y = a12*x + b12
b12 = diffb12/diffa12[1] # y = a12*x + b12
x12 = [-10, 10]
y12 = [a12*x12[0]+b12, a12*x12[1]+b12]
z12 = [b[0]/a1[2] - a1[0]/a1[2]*x12[0] - a1[1]/a1[2]*y12[0], b[0]/a1[2] - a1[0]/a1[2]*x12[1] - a1[1]/a1[2]*y12[1]]
ax.plot(x12, y12, z12)

# a2 and a3
c23 = a2[2]/a3[2]
a3_d = c23*a3; b3_d = c23*b[2]
diffa23 = a2 - a3_d; diffb23 = b[1] - b3_d
a23 = -diffa23[0]/diffa23[1] # y = a23*x + b23
b23 = diffb23/diffa23[1] # y = a23*x + b23
x23 = [-10, 10]
y23 = [a23*x23[0]+b23, a23*x23[1]+b23]
z23 = [b[1]/a2[2] - a2[0]/a2[2]*x23[0] - a2[1]/a2[2]*y23[0], b[1]/a2[2] - a2[0]/a2[2]*x23[1] - a2[1]/a2[2]*y23[1]]
ax.plot(x23, y23, z23)

# a1 and a3
c31 = a3[2]/a1[2]
a1_d = c31*a1; b1_d = c31*b[0]
diffa31 = a3 - a1_d; diffb31 = b[2] - b1_d
a31 = -diffa31[0]/diffa31[1] # y = a31*x + b31
b31 = diffb31/diffa31[1] # y = a31*x + b31
x31 = [-10, 10]
y31 = [a31*x31[0]+b31, a31*x31[1]+b31]
z31 = [b[2]/a3[2] - a3[0]/a3[2]*x31[0] - a3[1]/a3[2]*y31[0], b[2]/a3[2] - a3[0]/a3[2]*x31[1] - a3[1]/a3[2]*y31[1]]
ax.plot(x31, y31, z31)

# Plot the point where the three surface intersect
invA = np.linalg.inv(A)
x = invA@b
ax.scatter(x[0], x[1], x[2], color = "red")

# Set the labels for the axes
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_xlim([-5, 5])
ax.set_ylim([-5, 5])
ax.set_zlim([-5, 5])

# Show the plot
plt.savefig("23_matrix_product_geometry_interpretation/figure/row3by3.png")  
# plt.show()