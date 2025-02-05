# 加载糖尿病数据集

我们首先从scikit-learn中加载糖尿病数据集，并仅从数据集中选择一个特征。

```python
import numpy as np
from sklearn import datasets

# 加载糖尿病数据集
diabetes_X, diabetes_y = datasets.load_diabetes(return_X_y=True)

# 仅使用一个特征
diabetes_X = diabetes_X[:, np.newaxis, 2]
```
