# 加载数据

我们将首先加载鸢尾花数据集，并仅选择前两个特征用于可视化。

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets, svm

iris = datasets.load_iris()
X = iris.data
y = iris.target

X = X[y!= 0, :2]
y = y[y!= 0]
```
