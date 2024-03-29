import numpy as np
import matplotlib.pyplot as plt
import elimination

A = np.array([[1, 3], [2, 1]], dtype=float)
b = np.array([4, 3], dtype=float)
x = elimination.calc_solution(A, b)

fig = plt.figure(figsize = (5, 5))
ax = fig.add_subplot(111)
ax.grid()
ax.set_xlabel("x", fontsize = 16)
ax.set_ylabel("y", fontsize = 16)
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
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
# plt.savefig("24_elimination/figure/column2by2.png")  
plt.show()