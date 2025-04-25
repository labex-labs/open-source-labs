# データ

2000 個のサンプル、2 つの特徴量、および 3 つのターゲット クラスを持つ分類用のデータセットを生成します。次に、データを以下のように分割します。

- 学習用：600 個のサンプル (分類器の学習に使用)
- 検証用：400 個のサンプル (予測確率の補正に使用)
- テスト用：1000 個のサンプル

```python
import numpy as np
from sklearn.datasets import make_blobs

np.random.seed(0)

X, y = make_blobs(
    n_samples=2000, n_features=2, centers=3, random_state=42, cluster_std=5.0
)
X_train, y_train = X[:600], y[:600]
X_valid, y_valid = X[600:1000], y[600:1000]
X_train_valid, y_train_valid = X[:1000], y[:1000]
X_test, y_test = X[1000:], y[1000:]
```
