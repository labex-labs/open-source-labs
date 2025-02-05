# 加载必要的库和 MNIST 数据集

第一步是加载必要的库和数据集。我们将使用 `pandas`、`numpy`、`matplotlib` 和 `scikit-learn` 库。我们还将使用 scikit-learn 中的 `fetch_openml` 函数来加载 MNIST 数据集。

```python
import time
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.utils._testing import ignore_warnings
from sklearn.exceptions import ConvergenceWarning
from sklearn.utils import shuffle

# 加载 MNIST 数据集
def load_mnist(n_samples=None, class_0="0", class_1="8"):
    """加载 MNIST，选择两个类别，打乱顺序并仅返回 n_samples 个样本。"""
    # 从 http://openml.org/d/554 加载数据
    mnist = fetch_openml("mnist_784", version=1, as_frame=False, parser="pandas")

    # 仅选取两个类别进行二分类
    mask = np.logical_or(mnist.target == class_0, mnist.target == class_1)

    X, y = shuffle(mnist.data[mask], mnist.target[mask], random_state=42)
    if n_samples is not None:
        X, y = X[:n_samples], y[:n_samples]
    return X, y

X, y = load_mnist(n_samples=10000)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=0)
```
