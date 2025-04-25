# データの読み込みと準備

必要なライブラリをインポートし、アイリスデータセットを読み込んで始めます。その後、データをシャッフルし、訓練に使用するために標準化します。

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.linear_model import SGDClassifier

# アイリスデータセットを読み込む
iris = datasets.load_iris()

# 最初の 2 つの特徴量を取得する
X = iris.data[:, :2]
y = iris.target
colors = "bry"

# データをシャッフルする
idx = np.arange(X.shape[0])
np.random.seed(13)
np.random.shuffle(idx)
X = X[idx]
y = y[idx]

# データを標準化する
mean = X.mean(axis=0)
std = X.std(axis=0)
X = (X - mean) / std
```
