import numpy as np
import matplotlib.pyplot as plt
from func21 import centering, opt_reg_wo0, opt

# Generate training set
lam = np.exp(-10)
N = 10      # number of training data
M = 9   # oder of polynominal (please choose M such that M+1 =< N.)
f = 1       # frequency of sin wave.
A = 1       # amplitude of the sine wave 
start = 10   # lower bound   of x
stop = 11    # upper bound of x
sigma = 0.3             # standard deviation of the noise
y_offset = 2
x = np.linspace(start, stop, num = N, endpoint = True)  # generate x value
y = np.random.normal(A*np.sin(2*np.pi*f*x),sigma) + y_offset       # generate y value

# Compose Matrix for optimization
X = np.zeros((N,M+1))   # (N times M+1)
for i in range(N):
    for j in range(M+1):
        X[i][j] = x[i]**j

Xc, ave_X = centering(X)
w = opt_reg_wo0(y, Xc, lam)
w[0] = w[0] - w[1:].T@ave_X[1:]
w2 = opt(y, X, lam)

# plot
xp = np.linspace(start, stop, num = 1000, endpoint = True)
y_ideal = A*np.sin(2*np.pi*f*xp) + y_offset
Np = xp.shape[0]
y_est = np.zeros(Np)
y_est2 = np.zeros(Np)
for i in range(Np):
    for j in range(M+1):
        y_est[i] += (xp[i]**j)*w[j]
        y_est2[i] += (xp[i]**j)*w2[j]

plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams["font.size"] = 20
plt.scatter(x*np.ones(np.shape(x)), y)
plt.plot(xp,y_ideal,linestyle="dashed")
plt.plot(xp,y_est)
plt.plot(xp,y_est2)
# plt.ylim(-A-A*0.5, A+A*0.5)
plt.legend(['Training set','True','Estimate1','Estimate2'])
plt.xlabel('x')
plt.ylabel('y')
plt.show()