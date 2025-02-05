# 添加随机特征

我们将向原始数据中添加一些随机特征，以便更好地说明套索（Lasso）模型执行的特征选择。将使用 `numpy` 中的 `RandomState` 函数生成随机特征。

```python
import numpy as np
import pandas as pd

rng = np.random.RandomState(42)
n_random_features = 14
X_random = pd.DataFrame(
    rng.randn(X.shape[0], n_random_features),
    columns=[f"random_{i:02d}" for i in range(n_random_features)],
)
X = pd.concat([X, X_random], axis=1)
X[X.columns[::3]].head()
```
