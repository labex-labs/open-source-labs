# データの作成

500 個のサンプル、25 個の特徴量、ランク 5 の疑似データセットを作成します。また、同分散および異分散ノイズをデータセットに追加します。

```python
import numpy as np
from scipy import linalg

n_samples, n_features, rank = 500, 25, 5
sigma = 1.0
rng = np.random.RandomState(42)
U, _, _ = linalg.svd(rng.randn(n_features, n_features))
X = np.dot(rng.randn(n_samples, rank), U[:, :rank].T)

# 同分散ノイズの追加
X_homo = X + sigma * rng.randn(n_samples, n_features)

# 異分散ノイズの追加
sigmas = sigma * rng.rand(n_features) + sigma / 2.0
X_hetero = X + rng.randn(n_samples, n_features) * sigmas
```
