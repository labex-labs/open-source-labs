# 必要なライブラリとMNISTデータセットを読み込む

最初のステップは、必要なライブラリとデータセットを読み込むことです。`pandas`、`numpy`、`matplotlib`、および`scikit-learn`ライブラリを使用します。また、scikit-learnの`fetch_openml`関数を使ってMNISTデータセットを読み込みます。

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

# MNISTデータセットを読み込む
def load_mnist(n_samples=None, class_0="0", class_1="8"):
    """MNISTを読み込み、2つのクラスを選択し、シャッフルしてn_samplesのみを返す。"""
    # http://openml.org/d/554からデータを読み込む
    mnist = fetch_openml("mnist_784", version=1, as_frame=False, parser="pandas")

    # 2値分類のために2つのクラスのみを取り出す
    mask = np.logical_or(mnist.target == class_0, mnist.target == class_1)

    X, y = shuffle(mnist.data[mask], mnist.target[mask], random_state=42)
    if n_samples is not None:
        X, y = X[:n_samples], y[:n_samples]
    return X, y

X, y = load_mnist(n_samples=10000)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=0)
```
