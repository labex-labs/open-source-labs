# データの読み込み

まず、iris データセットを読み込み、それに 36 の非情報的な特徴を追加します。

```python
import numpy as np
from sklearn.datasets import load_iris

X, y = load_iris(return_X_y=True)

# Add non-informative features
rng = np.random.RandomState(0)
X = np.hstack((X, 2 * rng.random((X.shape[0], 36))))
```
