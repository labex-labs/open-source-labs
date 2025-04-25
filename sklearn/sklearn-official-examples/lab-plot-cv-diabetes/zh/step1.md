# 加载并准备数据集

首先，我们将加载并准备糖尿病数据集。本次练习我们仅使用前 150 个样本。

```python
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets

X, y = datasets.load_diabetes(return_X_y=True)
X = X[:150]
y = y[:150]
```
