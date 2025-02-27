# サンプルデータを生成する

まず、このデモ用にいくつかのサンプルデータを生成します。irisデータセットを使用し、それに相関のないノイズデータを追加します。

```python
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

# irisデータセット
X, y = load_iris(return_X_y=True)

# 相関のないいくつかのノイズデータ
E = np.random.RandomState(42).uniform(0, 0.1, size=(X.shape[0], 20))

# ノイズデータを情報的な特徴に追加する
X = np.hstack((X, E))

# 特徴を選択し、分類器を評価するためにデータセットを分割する
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=0)
```
