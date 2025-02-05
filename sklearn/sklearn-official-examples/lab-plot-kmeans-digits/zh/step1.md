# 加载数据集

我们将首先使用 scikit-learn 的 `load_digits()` 函数加载数字数据集。此函数返回数据集的特征和标签。

```python
import numpy as np
from sklearn.datasets import load_digits

data, labels = load_digits(return_X_y=True)
(n_samples, n_features), n_digits = data.shape, np.unique(labels).size
```
