import numpy as np
import matplotlib.pyplot as plt
from func21 import opt

# Generate training set
lam = np.array([0, np.exp(-10), 1])
N = 10      # number of training data
M = 9   # oder of polynominal (please choose M such that M+1 =< N.)
f = 1       # frequency of sin wave.
A = 1       # amplitude of the sine wave 
start = 0   # lower bound   of x
stop = 1    # upper bound of x
sigma = 0.3             # standard deviation of the noise
y_offset = 0
x = np.linspace(start, stop, num = N, endpoint = True)  # generate x value
y = np.random.normal(A*np.sin(2*np.pi*f*x),sigma) + y_offset       # generate y value

# Compose Matrix for optimization
X = np.zeros((N,M+1))   # (N times M+1)
for i in range(N):
    for j in range(M+1):
        X[i][j] = x[i]**j

w = np.zeros((M+1,len(lam)))
for k in range(len(lam)):
    w[:,k] = opt(y, X, lam[k])
    print(w[:,k])

# plot
xp = np.linspace(start, stop, num = 1000, endpoint = True)
y_ideal = A*np.sin(2*np.pi*f*xp) + y_offset
Np = xp.shape[0]
y_est = np.zeros((Np,len(lam)))
for k in range(len(lam)):
    for i in range(Np):
        for j in range(M+1):
            y_est[i][k] += (xp[i]**j)*w[j][k]

plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams["font.size"] = 14
plt.scatter(x*np.ones(np.shape(x)), y)
plt.plot(xp,y_ideal,linestyle="dashed")
for k in range(len(lam)):
    plt.plot(xp,y_est[:,k])
plt.ylim(-A-A*0.5, A+A*0.5)
plt.legend(['Training set','True','${\ln}\lambda=-\infty$','${\ln}\lambda=-18$','${\ln}\lambda=0$'])
plt.xlabel('x')
plt.ylabel('y')
plt.show()