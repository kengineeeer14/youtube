import numpy as np
import matplotlib.pyplot as plt

#### try to change #############
M = 9   # oder of polynominal (please choose M such that M+1 =< N.)
################################

# Generate training set
N = 10      # number of training data
f = 1       # frequency of sin wave.
A = 1       # amplitude of the sine wave 
start = 0   # lower bound of x
stop = 1    # upper bound of x
sigma = 0.3             # standard deviation of the noise
x = np.linspace(start, stop, num = N, endpoint = True)  # generate x value
y = np.random.normal(A*np.sin(2*np.pi*f*x),sigma)       # generate y value

# Compose Matrix for optimization
X = np.zeros((N,M+1))   # (N times M+1)
for i in range(N):
    for j in range(M+1):
        X[i][j] = x[i]**j

# Optimization
w = np.linalg.inv(X.T @ X) @ X.T @ y
print(w)

# plot
xp = np.linspace(start, stop, num = 1000, endpoint = True)
y_ideal = A*np.sin(2*np.pi*f*xp)
Np = xp.shape[0]
y_est = np.zeros(Np)
for i in range(Np):
    for j in range(M+1):
        y_est[i] += (xp[i]**j)*w[j]

plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams["font.size"] = 14
plt.scatter(x, y)
plt.plot(xp,y_ideal,linestyle="dashed")
plt.plot(xp,y_est)
plt.ylim(-A-A*0.5, A+A*0.5)
plt.legend(['Training set','True','Estimate'])
plt.xlabel('x')
plt.ylabel('y')
plt.show()
