import numpy as np


def rms(y, w, X):
    """
    Return the root mean square of the error.
    """
    N = len(y)
    y_hat = X@w
    sum_e2 = 0
    for i in range(N):
        sum_e2 += (y_hat[i] - y[i])**2
    e_rms = np.sqrt(sum_e2/N)
    return e_rms
        

def opt(y, X, lam = 0):
    """
    Return optimization value of the parameter.
    """
    w = np.linalg.inv(X.T @ X + lam * np.eye(len(X.T))) @ X.T @ y
    return w


def centering(X):
    """
    Do centering
    """
    n, m = np.shape(X)
    ave_X = np.zeros(m)
    for j in range(m):
        sum_X = 0
        for i in range(n):
            sum_X += X[i][j]
        ave_X[j] = sum_X/n
    Xc = np.zeros((n, m))
    for j in range(m):
        for i in range(n):
            Xc[i][j] = X[i][j] - ave_X[j]
    return Xc, ave_X


def opt_reg_wo0(y, X, lam):
    """
    optimization with regularization
    0-oreder coefficient is ignored in regularization term.
    X must be centered.
    """
    wd = np.linalg.inv(X.T @ X + lam * np.eye(len(X.T))) @ X.T @ y
    w0 = np.mean(y)
    w = np.hstack([w0, wd])
    return w


if __name__=='__main__':
    pass