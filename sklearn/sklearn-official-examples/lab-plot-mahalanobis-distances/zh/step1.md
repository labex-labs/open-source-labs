# 生成数据

首先，我们生成一个包含 125 个样本和 2 个特征的数据集。两个特征均呈高斯分布，均值为 0。然而，特征 1 的标准差等于 2，特征 2 的标准差等于 1。接下来，我们用高斯异常值样本替换 25 个样本，其中特征 1 的标准差等于 1，特征 2 的标准差等于 7。

```python
import numpy as np

# for consistent results
np.random.seed(7)

n_samples = 125
n_outliers = 25
n_features = 2

# generate Gaussian data of shape (125, 2)
gen_cov = np.eye(n_features)
gen_cov[0, 0] = 2.0
X = np.dot(np.random.randn(n_samples, n_features), gen_cov)
# add some outliers
outliers_cov = np.eye(n_features)
outliers_cov[np.arange(1, n_features), np.arange(1, n_features)] = 7.0
X[-n_outliers:] = np.dot(np.random.randn(n_outliers, n_features), outliers_cov)
```
