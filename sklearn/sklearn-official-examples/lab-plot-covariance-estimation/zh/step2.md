# 计算测试数据上的似然度

我们使用 `sklearn.covariance` 模块中的 `ShrunkCovariance` 类和 `scipy.linalg` 模块中的 `log_likelihood` 函数来计算测试数据上的负对数似然度。我们遍历一系列可能的收缩系数值，并计算每个值的似然度。

```python
from sklearn.covariance import ShrunkCovariance, empirical_covariance, log_likelihood
from scipy import linalg

shrinkages = np.logspace(-2, 0, 30)
negative_logliks = [
    -ShrunkCovariance(shrinkage=s).fit(X_train).score(X_test) for s in shrinkages
]

real_cov = np.dot(coloring_matrix.T, coloring_matrix)
emp_cov = empirical_covariance(X_train)
loglik_real = -log_likelihood(emp_cov, linalg.inv(real_cov))
```
