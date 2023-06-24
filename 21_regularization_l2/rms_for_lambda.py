import numpy as np
import matplotlib.pyplot as plt
from func21 import opt, rms

# Generate training set
M = 9       # oder of polynominal (please choose M such that M+1 =< N.)
N = 10      # number of training data
N_test = N*2    # number of test data
f = 1       # frequency of sin wave.
A = 1       # amplitude of the sine wave 
start = 0   # lower bound of x
stop = 1    # upper bound of x
sigma = 0.3 # standard deviation of the noise

log_lam_min = -35
log_lam_max = 0
lam_arr = np.linspace(log_lam_min, log_lam_max, (log_lam_max-log_lam_min) + 1)

rms_train = np.zeros(log_lam_max-log_lam_min + 1)
rms_test = np.zeros(log_lam_max-log_lam_min + 1)

# rms 
x_train = np.linspace(start, stop, num = N, endpoint = True)  # generate x value
y_train = np.random.normal(A*np.sin(2*np.pi*f*x_train),sigma)       # generate y value
x_test = np.linspace(start, stop, num = N_test, endpoint = True)  # generate x value
y_test = np.random.normal(A*np.sin(2*np.pi*f*x_test),sigma)       # generate y value
for lam in range(log_lam_min, log_lam_max+1, 1):
    # Compose Matrix for optimization
    X_train = np.zeros((N,M+1))   # (N times M+1)
    for i in range(N):
        for j in range(M+1):
            X_train[i][j] = x_train[i]**j
    # Compose Matrix for optimizations
    X_test = np.zeros((N_test,M+1))   # (N times M+1)
    for i in range(N_test):
        for j in range(M+1):
            X_test[i][j] = x_test[i]**j
    # optimization
    w = opt(y_train, X_train, np.exp(lam))
    i = lam - log_lam_min
    # rms for training data
    rms_train[i] = rms(y_train,w,X_train)
    # rms for test data
    rms_test[i] = rms(y_test,w,X_test)


plt.rcParams['font.family'] = 'Times New Roman'
plt.plot(lam_arr, rms_train, marker='.',markersize=20, linestyle="dashed", color="black")
plt.plot(lam_arr, rms_test, marker='.',markersize=20, linestyle="dashed", color="red")
plt.legend(['Training set','Test set'])
plt.xlabel('ln$\lambda$')
plt.ylabel('RMS')
plt.grid()
plt.show()