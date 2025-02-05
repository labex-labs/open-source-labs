# 数据生成

我们将使用 scikit-learn 中的 `make_blobs` 函数来生成具有不同分布的不同数据集。在以下代码块中，我们生成四个数据集：

- 高斯混合聚类
- 各向异性分布的聚类
- 方差不等的聚类
- 大小不均的聚类

```python
import numpy as np
from sklearn.datasets import make_blobs

n_samples = 1500
random_state = 170
transformation = [[0.60834549, -0.63667341], [-0.40887718, 0.85253229]]

X, y = make_blobs(n_samples=n_samples, random_state=random_state)
X_aniso = np.dot(X, transformation)  # 各向异性聚类
X_varied, y_varied = make_blobs(
    n_samples=n_samples, cluster_std=[1.0, 2.5, 0.5], random_state=random_state
)  # 方差不等
X_filtered = np.vstack(
    (X[y == 0][:500], X[y == 1][:100], X[y == 2][:10])
)  # 大小不均的聚类
y_filtered = [0] * 500 + [1] * 100 + [2] * 10
```
