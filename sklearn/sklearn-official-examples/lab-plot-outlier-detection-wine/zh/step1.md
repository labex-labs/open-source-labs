# 导入库并加载数据集

我们将首先导入必要的库，并从 scikit-learn 中加载葡萄酒数据集。葡萄酒数据集包含有关不同类型葡萄酒的信息，包括它们的化学特性。

```python
import numpy as np
from sklearn.covariance import EllipticEnvelope
from sklearn.svm import OneClassSVM
import matplotlib.pyplot as plt
from sklearn.datasets import load_wine

# Load dataset
X1 = load_wine()["data"][:, [1, 2]]  # two clusters
X2 = load_wine()["data"][:, [6, 9]]  # "banana"-shaped
```
