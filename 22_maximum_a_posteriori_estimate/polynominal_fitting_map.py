import numpy as np
import matplotlib.pyplot as plt

# Hyperparameter
alpha = 0.0001   # precision of a prior distribution
beta = 0.09    # precision of the likelihood function

# Generate training set
N = 10     # number of training data
M = 9       # oder of polynominal (please choose M such that M+1 =< N.)
f = 1       # frequency of sin wave.
A = 1       # amplitude of the sine wave 
start = 0   # lower bound of x
stop = 1    # upper bound of x
sigma = 0.3 # standard deviation of the noise
x = np.linspace(start, stop, num = N, endpoint = True)  # generate x value
y = np.random.normal(A*np.sin(2*np.pi*f*x),sigma)       # generate y value

# Compose Matrix for optimization
X = np.zeros((N,M+1))   # (N times M+1)
for i in range(N):
    for j in range(M+1):
        X[i][j] = x[i]**j

# MAP estimation
w = np.linalg.inv(X.T @ X + (alpha/beta) * np.eye(len(X.T))) @ X.T @ y
# Variance estimation
sigma2_hat = np.linalg.norm(X @ w - y, ord=2)**2/N
sigma_hat = np.sqrt(sigma2_hat)

# Show estimate result
for i in range(M):
    print("Parameter estimate w" + str(i) + ": " + str(w[i]))

print("Estimate of variance : " + str(sigma2_hat))

# plot
xp = np.linspace(start, stop, num = 5000, endpoint = True)
y_ideal = A*np.sin(2*np.pi*f*xp)
Np = xp.shape[0]
y_est = np.zeros(Np)
for i in range(Np):
    for j in range(M+1):
        y_est[i] += (xp[i]**j)*w[j]

plt.rcParams['font.family'] = 'Times New Roman'
plt.scatter(x, y, color="black")
plt.plot(xp,y_ideal,linestyle="dashed", color="black")
plt.plot(xp,y_est, color="red")
plt.ylim(0, 1)
plt.ylim(-A-A*0.5, A+A*0.5)
plt.legend(['Training set','True','MAP estimate'])
plt.xlabel('x')
plt.ylabel('y')
plt.show()
