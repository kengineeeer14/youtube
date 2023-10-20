import numpy as np
import matplotlib.pyplot as plt

a1 = np.array([[1], [2]])
a2 = np.array([[3], [1]])

A = np.column_stack((a1, a2))
b = np.array([4, 3])
Ainv = np.linalg.inv(A)
x = Ainv@b

fig = plt.figure(figsize = (5, 4))
ax = fig.add_subplot(111)
ax.grid()
ax.set_xlabel("x", fontsize = 16)
ax.set_ylabel("y", fontsize = 16)
ax.set_xlim(0, 5)
ax.set_ylim(0, 4)
ax.axhline(0, color = "gray")
ax.axvline(0, color = "gray")
ax.set_yticks(np.arange(0, 4, 1))
ax.set_xticks(np.arange(0, 5, 1))
ax.quiver(0, 0, A[0,0], A[1,0], color = "red",
            width = 0.015, angles = 'xy', scale_units = 'xy', scale = 1)
ax.quiver(0, 0, A[0,1], A[1,1], color = "red",
          width = 0.015, angles = 'xy', scale_units = 'xy', scale = 1)
ax.quiver(0, 0, b[0], b[1], color = "blue",
          width = 0.015, angles = 'xy', scale_units = 'xy',     scale = 1)
ax.text(A[0,0], A[1,0], "[%d, %d]"%(A[0,0],A[1,0]), color = "red", size = 10)
ax.text(A[0,1], A[1,1], "[%d, %d]"%(A[0,1],A[1,1]), color = "red", size = 10)
ax.text(b[0], b[1], "[%d, %d]"%(b[0],b[1]), color = "blue", size = 10)

ax.quiver(0, 0, x[0]*A[0,0], x[0]*A[1,0], color = "green",
          angles = 'xy', scale_units = 'xy', scale = 1)
ax.quiver(x[0]*A[0,0], x[0]*A[1,0], x[1]*A[0,1], x[1]*A[1,1], color = "green",
          angles = 'xy', scale_units = 'xy', scale = 1)
# plt.savefig("23_matrix_product_geometry_interpretation/figure/column2by2.png")  
plt.show()