# 加载糖尿病数据集

首先，我们从 scikit-learn 中加载糖尿病数据集，并将其拆分为训练集和测试集。

```python
from sklearn import datasets
import numpy as np

X, y = datasets.load_diabetes(return_X_y=True)
indices = (0, 1)

X_train = X[:-20, indices]
X_test = X[-20:, indices]
y_train = y[:-20]
y_test = y[-20:]
```
