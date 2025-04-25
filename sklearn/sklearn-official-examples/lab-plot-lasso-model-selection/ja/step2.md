# ランダムな特徴量の追加

Lasso モデルによって行われる特徴量選択をよりよく説明するために、元のデータにいくつかのランダムな特徴量を追加します。ランダムな特徴量は、`numpy` の `RandomState` 関数を使用して生成されます。

```python
import numpy as np
import pandas as pd

rng = np.random.RandomState(42)
n_random_features = 14
X_random = pd.DataFrame(
    rng.randn(X.shape[0], n_random_features),
    columns=[f"random_{i:02d}" for i in range(n_random_features)],
)
X = pd.concat([X, X_random], axis=1)
X[X.columns[::3]].head()
```
