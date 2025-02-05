# 数据生成

我们将生成一个包含两个聚类和一些离群点的数据集。聚类将通过从标准正态分布中随机采样生成。其中一个聚类将是球形的，另一个将略有变形。离群点将通过从均匀分布中随机采样生成。

```python
import numpy as np
from sklearn.model_selection import train_test_split

n_samples, n_outliers = 120, 40
rng = np.random.RandomState(0)
covariance = np.array([[0.5, -0.1], [0.7, 0.4]])
cluster_1 = 0.4 * rng.randn(n_samples, 2) @ covariance + np.array([2, 2])  # 一般
cluster_2 = 0.3 * rng.randn(n_samples, 2) + np.array([-2, -2])  # 球形
outliers = rng.uniform(low=-4, high=4, size=(n_outliers, 2))

X = np.concatenate([cluster_1, cluster_2, outliers])
y = np.concatenate(
    [np.ones((2 * n_samples), dtype=int), -np.ones((n_outliers), dtype=int)]
)

X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=42)
```
