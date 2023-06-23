import numpy as np
import matplotlib.pyplot as plt
from func21 import opt, rms

# Generate training set
lam = 0     # Coefficient of regularization term
N = 10      # number of training data
N_test = N*2    # number of test data
f = 1       # frequency of sin wave.
A = 1       # amplitude of the sine wave 
start = 0   # lower bound of x
stop = 1    # upper bound of x
sigma = 0.3 # standard deviation of the noise
M_max = 9       # oder of polynominal (please choose M such that M+1 =< N.)
rms_train = np.zeros(M_max+1)
rms_test = np.zeros(M_max+1)

# rms 
x_train = np.linspace(start, stop, num = N, endpoint = True)  # generate x value
y_train = np.random.normal(A*np.sin(2*np.pi*f*x_train),sigma)       # generate y value
x_test = np.linspace(start, stop, num = N_test, endpoint = True)  # generate x value
y_test = np.random.normal(A*np.sin(2*np.pi*f*x_test),sigma)       # generate y value
for M in range(M_max+1):
    # Compose Matrix for optimization
    X_train = np.zeros((N,M+1))   # (N times M+1)
    for i in range(N):
        for j in range(M+1):
            X_train[i][j] = x_train[i]**j
    # Compose Matrix for optimization
    X_test = np.zeros((N_test,M+1))   # (N times M+1)
    for i in range(N_test):
        for j in range(M+1):
            X_test[i][j] = x_test[i]**j
    # optimization
    w = opt(y_train, X_train, lam)
    print(w)
    # rms for training data
    rms_train[M] = rms(y_train,w,X_train)
    # rms for test data
    rms_test[M] = rms(y_test,w,X_test)

M_arr = [i for i in range(M_max+1)]
plt.rcParams['font.family'] = 'Times New Roman'
plt.plot(M_arr, rms_train, marker='.',markersize=20, linestyle="dashed", color="black")
plt.plot(M_arr, rms_test, marker='.',markersize=20, linestyle="dashed", color="red")
plt.legend(['Training set','Test set'])
plt.xlabel('M')
plt.ylabel('RMS')
plt.show()
