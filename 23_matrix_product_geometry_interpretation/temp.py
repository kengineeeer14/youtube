import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

a1 = np.array([1, 2, 3])
a2 = np.array([2, 5, 2])
a3 = np.array([6, -3, 1])

# A = np.column_stack((a1, a2, a3))
A = np.array([a1, a2, a3])
b = np.array([8, 4, 2])

# Define the x and y coordinates of the surface
x = np.linspace(-3, 3, 100)
y = np.linspace(-3, 3, 100)
X, Y = np.meshgrid(x, y)

# Define the function that defines the surface
Z1 = b[0]/a1[2] - a1[0]/a1[2]*X - a1[1]/a1[2]*Y
Z2 = b[1]/a2[2] - a2[0]/a2[2]*X - a2[1]/a2[2]*Y
Z3 = b[2]/a3[2] - a3[0]/a3[2]*X - a3[1]/a3[2]*Y

# Create the figure and axes
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Set the limits of the x, y, and z axes
ax.set_xlim([-5, 5])
ax.set_ylim([-5, 5])
ax.set_zlim([-5, 5])

# Plot the surface
surf1 = ax.plot_surface(X, Y, Z1, alpha=0.5)
surf2 = ax.plot_surface(X, Y, Z2, alpha=0.5)
# plt.show()
# Set the limits of the color scale for the surfaces
surf1.set_clim(-5, 5)
surf2.set_clim(-5, 5)

# Show the plot
plt.show()