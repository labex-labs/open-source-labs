# ライブラリのインポートとデータセットの読み込み

必要なライブラリをインポートし、scikit-learn から Wine データセットを読み込んで始めましょう。Wine データセットには、さまざまな種類のワインの情報、その化学的特性も含まれています。

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
