# 生成合成数据集

首先，我们生成一个样本数量少于特征总数的数据集。这会导致一个欠定系统，即解不唯一，我们不能单独应用普通最小二乘法。正则化会在目标函数中引入一个惩罚项，它会修改优化问题，并有助于缓解系统的欠定性质。我们将生成一个目标 `y`，它是正弦信号的线性组合，其系数正负交替。在 `X` 的 100 个频率中，只有最低的 10 个频率用于生成 `y`，而其余特征则没有信息价值。这就导致了一个高维稀疏特征空间，在这种情况下，某种程度的 L1 惩罚是必要的。

```python
import numpy as np

rng = np.random.RandomState(0)
n_samples, n_features, n_informative = 50, 100, 10
time_step = np.linspace(-2, 2, n_samples)
freqs = 2 * np.pi * np.sort(rng.rand(n_features)) / 0.01
X = np.zeros((n_samples, n_features))

for i in range(n_features):
    X[:, i] = np.sin(freqs[i] * time_step)

idx = np.arange(n_features)
true_coef = (-1) ** idx * np.exp(-idx / 10)
true_coef[n_informative:] = 0  # 使系数稀疏化
y = np.dot(X, true_coef)

# 使用 numpy.random.random_sample 引入随机相位
# 使用 numpy.random.normal 添加一些高斯噪声
for i in range(n_features):
    X[:, i] = np.sin(freqs[i] * time_step + 2 * (rng.random_sample() - 0.5))
    X[:, i] += 0.2 * rng.normal(0, 1, n_samples)

y += 0.2 * rng.normal(0, 1, n_samples)

# 使用 sklearn 中的 train_test_split 将数据拆分为训练集和测试集
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, shuffle=False)
```
