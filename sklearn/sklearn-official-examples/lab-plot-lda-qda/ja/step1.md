# ライブラリのインポートとデータセットの生成

まず、必要なライブラリをインポートし、2つのデータセットを生成します。1つは共分散が固定されたもので、もう1つは共分散が変化するものです。

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy import linalg
from matplotlib import colors
import matplotlib as mpl
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis, QuadraticDiscriminantAnalysis

# 共分散が固定されたデータセットを生成する関数
def dataset_fixed_cov():
    n, dim = 300, 2
    np.random.seed(0)
    C = np.array([[0.0, -0.23], [0.83, 0.23]])
    X = np.r_[np.dot(np.random.randn(n, dim), C), np.dot(np.random.randn(n, dim), C) + np.array([1, 1])]
    y = np.hstack((np.zeros(n), np.ones(n)))
    return X, y

# 共分散が変化するデータセットを生成する関数
def dataset_cov():
    n, dim = 300, 2
    np.random.seed(0)
    C = np.array([[0.0, -1.0], [2.5, 0.7]]) * 2.0
    X = np.r_[np.dot(np.random.randn(n, dim), C), np.dot(np.random.randn(n, dim), C.T) + np.array([1, 4])]
    y = np.hstack((np.zeros(n), np.ones(n)))
    return X, y
```
