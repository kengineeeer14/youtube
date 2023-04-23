import numpy as np
import matplotlib.pyplot as plt
import math

def expec(x):
    """Return the expectation of the array x.

    >>> x = [1, 2]
    >>> expec(x)
    1.5
    """
    l = len(x)
    value = sum(x)/l
    return value

mu = 0      # 母集団の平均値
sigma2 = 4  # 母集団の分散

N = 2      # サンプル数(Nは2以上で設定してください．)
k = 100000    # 試行回数

mu_ML = np.zeros(k)
sigma2_ML = np.zeros(k)
sigma2_unb = np.zeros(k)

for j in range(k):
    x_sample = np.zeros(N)
    for i in range(N):
        x_sample[i] = np.random.normal(mu,sigma2**(1/2))

    # 最尤推定
    mu_ML[j] = sum(x_sample)/N
    sigma2_ML[j] = sum((x_sample - np.ones(N)*mu_ML[j])**2)/N

    # 不偏分散
    sigma2_unb[j] = N/(N-1)*sigma2_ML[j]

# 期待値計算
mu_ML_e = expec(mu_ML)
sigma2_ML_e = expec(sigma2_ML)
sigma2_unb_e = expec(sigma2_unb)

# 結果表示
print('標本平均の期待値は', mu_ML_e)
print('標本分散の期待値は', sigma2_ML_e)
print('不偏分散の期待値は', sigma2_unb_e)

# グラフ描画
M = 100    # グラフを生成するポイント数
x = np.linspace(-5, 5, M)
p = np.zeros(M)
p_ML = np.zeros(M)
p_unb = np.zeros(M)
for i in range(M):
    p[i] = 1/((2*math.pi*sigma2)**(1/2))*math.exp(-1/(2*(sigma2))*(x[i]-mu)**2)
    p_ML[i] = 1/((2*math.pi*sigma2_ML_e)**(1/2))*math.exp(-1/(2*(sigma2_ML_e))*(x[i]-mu_ML_e)**2)
    p_unb[i] = 1/((2*math.pi*sigma2_unb_e)**(1/2))*math.exp(-1/(2*(sigma2_unb_e))*(x[i]-mu_ML_e)**2)
plt.plot(x, p, c = 'black')
plt.plot(x, p_ML, c = 'red')
plt.plot(x, p_unb, c = 'blue')
# plt.ylim((0,0.4))
# plt.xlim((-5,5))
# plt.legend(['True distribution','ML'])
plt.show()