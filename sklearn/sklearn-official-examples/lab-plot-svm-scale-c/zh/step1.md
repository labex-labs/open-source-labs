# 导入库并生成合成数据集

我们首先导入必要的库，并生成一个适用于 L1 和 L2 正则化的合成数据集。

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.svm import LinearSVC
from sklearn.model_selection import validation_curve, ShuffleSplit

n_samples, n_features = 100, 300
X, y = make_classification(n_samples=n_samples, n_features=n_features, n_informative=5, random_state=1)

rng = np.random.RandomState(1)
y = np.sign(0.5 - rng.rand(n_samples))
X = rng.randn(n_samples, n_features // 5) + y[:, np.newaxis]
X += 5 * rng.randn(n_samples, n_features // 5)
```
