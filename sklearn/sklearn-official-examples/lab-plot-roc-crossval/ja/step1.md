# データの読み込みと準備

まず、Scikit-learn ライブラリを使ってアイリスデータセットを読み込みます。アイリスデータセットには 3 種類のアイリス植物が含まれており、2 値分類問題を作成するために 1 つのクラスを除外することでデータセットを 2 値化します。また、問題をより難しくするためにノイズのある特徴を追加します。

```python
import numpy as np
from sklearn.datasets import load_iris

iris = load_iris()
target_names = iris.target_names
X, y = iris.data, iris.target
X, y = X[y!= 2], y[y!= 2]
n_samples, n_features = X.shape

# add noisy features
random_state = np.random.RandomState(0)
X = np.concatenate([X, random_state.randn(n_samples, 200 * n_features)], axis=1)
```
