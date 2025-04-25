# 创建数据集

我们创建了一个包含两个多变量协变二维数据集 X 和 Y 的数据集。然后，我们提取协方差方向，即每个数据集中解释两个数据集之间最大共享方差的成分。

```python
import numpy as np

n = 500
# 2 个潜在变量：
l1 = np.random.normal(size=n)
l2 = np.random.normal(size=n)

latents = np.array([l1, l1, l2, l2]).T
X = latents + np.random.normal(size=4 * n).reshape((n, 4))
Y = latents + np.random.normal(size=4 * n).reshape((n, 4))

X_train = X[: n // 2]
Y_train = Y[: n // 2]
X_test = X[n // 2 :]
Y_test = Y[n // 2 :]

print("Corr(X)")
print(np.round(np.corrcoef(X.T), 2))
print("Corr(Y)")
print(np.round(np.corrcoef(Y.T), 2))
```
