# 加载数据

我们首先加载鸢尾花数据集，并向其中添加 36 个无信息特征。

```python
import numpy as np
from sklearn.datasets import load_iris

X, y = load_iris(return_X_y=True)

# Add non-informative features
rng = np.random.RandomState(0)
X = np.hstack((X, 2 * rng.random((X.shape[0], 36))))
```
