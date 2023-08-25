import numpy as np
import matplotlib.pyplot as plt

A = np.array([[1, 2],[-2, 1]])
b = np.array([4, -3])
Ainv = np.linalg.inv(A)
x = Ainv@b


fig = plt.figure(figsize = (5, 5))
ax = fig.add_subplot(111)
ax.grid()
ax.set_xlabel("x", fontsize = 16)
ax.set_ylabel("y", fontsize = 16)
ax.set_xlim(-3, 7)
ax.set_ylim(-7, 3)
ax.axhline(0, color = "gray")
ax.axvline(0, color = "gray")
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

plt.show()