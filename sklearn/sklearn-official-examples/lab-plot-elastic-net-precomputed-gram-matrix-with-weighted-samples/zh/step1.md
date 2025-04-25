# 加载数据集并创建样本权重

我们首先加载数据集并创建一些样本权重。我们使用 scikit-learn 中的`make_regression`函数来生成一个包含 100,000 个样本的随机回归数据集。然后，我们生成一个对数正态分布的权重向量，并将其归一化，使其总和等于样本总数。

```python
import numpy as np
from sklearn.datasets import make_regression

rng = np.random.RandomState(0)

n_samples = int(1e5)
X, y = make_regression(n_samples=n_samples, noise=0.5, random_state=rng)

sample_weight = rng.lognormal(size=n_samples)
# normalize the sample weights
normalized_weights = sample_weight * (n_samples / (sample_weight.sum()))
```
