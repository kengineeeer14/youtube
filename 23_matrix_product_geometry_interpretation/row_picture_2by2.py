import numpy as np
import matplotlib.pyplot as plt


a1 = np.array([1, 3])
a2 = np.array([2, 1])

A = np.array([a1, a2])
b = np.array([4, 3])
Ainv = np.linalg.inv(A)
x = Ainv@b
xmin = x[0]-5
xmax = x[0]+5
ymin = x[1]-5
ymax = x[1]+5
fig = plt.figure(figsize = (5, 5))
ax = fig.add_subplot(111)
ax.grid()
if A[0][1] == 0:
    x0min = -A[0,1]/A[0,0]*ymin + b[0]/A[0,0]
    x0max = -A[0,1]/A[0,0]*ymax + b[0]/A[0,0]
    plt.plot([x0min, x0max], [ymin, ymax], color = "black")
else:
    y0min = -A[0,0]/A[0,1]*xmin + b[0]/A[0,1]
    y0max = -A[0,0]/A[0,1]*xmax + b[0]/A[0,1]
    plt.plot([xmin, xmax], [y0min, y0max], color = "black")
    
if A[1][1] == 0:
    x1min = -A[1,1]/A[1,0]*ymin + b[1]/A[1,0]
    x1max = -A[1,1]/A[1,0]*ymax + b[1]/A[1,0]
    plt.plot([x1min, x1max], [ymin, ymax], color = "black")
else:
    y1min = -A[1,0]/A[1,1]*xmin + b[1]/A[1,1]
    y1max = -A[1,0]/A[1,1]*xmax + b[1]/A[1,1]
    plt.plot([xmin, xmax], [y1min, y1max], color = "black")
plt.scatter(x[0], x[1], color = "red")
ax.text(x[0], x[1], "[%.2f, %.2f]"%(x[0],x[1]), color = "red", size = 20)
ax.set_xlabel("x", fontsize = 16)
ax.set_ylabel("y", fontsize = 16)
ax.set_xlim(xmin, xmax)
ax.set_ylim(ymin, ymax)
ax.axhline(0, color = "gray")
ax.axvline(0, color = "gray")
# plt.savefig("23_matrix_product_geometry_interpretation/figure/row2by2.png")  
plt.show()

