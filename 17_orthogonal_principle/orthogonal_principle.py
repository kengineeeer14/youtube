'''
This code dipicts the orthogonality of the least squared method answer.
'''

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

########################################
X1 = np.array([5, 0, 0])    # X行列の1列目
X2 = np.array([0, 5, 0])    # X行列の2列目
y = np.array([2.5, 2.5, 5])
#########################################

X = np.array([X1, X2]).T
# Least squares method
w = np.linalg.inv(X.T @ X) @ X.T @ y
# plot
#描画エリアの作成
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
yhat = X @ w

# plot
Xp = np.array([y[0], yhat[0]])
Yp = np.array([y[1], yhat[1]])
Zp = np.array([y[2], yhat[2]])
ax.plot(Xp, Yp, Zp, color = 'red')

ax.plot(np.array([0, X1[0]]),np.array([0, X1[1]]),np.array([0, X1[2]]),color = 'black')
ax.plot(np.array([0, X2[0]]),np.array([0, X2[1]]),np.array([0, X2[2]]), color = 'black')
#描画
plt.show()