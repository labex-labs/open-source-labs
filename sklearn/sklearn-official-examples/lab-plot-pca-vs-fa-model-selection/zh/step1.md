# 创建数据

我们将创建一个模拟数据集，它包含500个样本、25个特征，秩为5。我们还将向数据集中添加同方差和异方差噪声。

```python
import numpy as np
from scipy import linalg

n_samples, n_features, rank = 500, 25, 5
sigma = 1.0
rng = np.random.RandomState(42)
U, _, _ = linalg.svd(rng.randn(n_features, n_features))
X = np.dot(rng.randn(n_samples, rank), U[:, :rank].T)

# 添加同方差噪声
X_homo = X + sigma * rng.randn(n_samples, n_features)

# 添加异方差噪声
sigmas = sigma * rng.rand(n_features) + sigma / 2.0
X_hetero = X + rng.randn(n_samples, n_features) * sigmas
```
