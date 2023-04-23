import numpy as np
import matplotlib.pyplot as plt
import math

mu = 0      # 母集団の平均値
sigma2 = 4  # 母集団の分散


N = 100      # サンプル数
x_sample = np.zeros(N)
for i in range(N):
    x_sample[i] = np.random.normal(mu,sigma2**(1/2))

# 最尤推定
mu_ML = sum(x_sample)/N
sigma2_ML = sum((x_sample - np.ones(N)*mu_ML)**2)/N

# 結果表示
print('標本平均は', mu_ML)
print('標本分散は', sigma2_ML)

# グラフ描画
M = 100    # グラフを生成するポイント数

x = np.linspace(-5, 5, M)
p = np.zeros(M)
p_ML = np.zeros(M)
for i in range(M):
    p[i] = 1/((2*math.pi*sigma2)**(1/2))*math.exp(-1/(2*(sigma2))*(x[i]-mu)**2)
    p_ML[i] = 1/((2*math.pi*sigma2_ML)**(1/2))*math.exp(-1/(2*(sigma2_ML))*(x[i]-mu_ML)**2)
plt.plot(x, p)
plt.plot(x, p_ML, c='red')
plt.ylim((0,0.4))
plt.xlim((-5,5))
plt.legend(['True distribution','Predictive distribution'])
plt.show()