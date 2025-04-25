# サンプルデータの生成

このステップでは、自由度の少ない 2 つのスタデント T 分布を使った非常に非ガウス的なプロセスを用いてサンプルデータを生成します。

```python
import numpy as np

from sklearn.decomposition import PCA, FastICA

rng = np.random.RandomState(42)
S = rng.standard_t(1.5, size=(20000, 2))
S[:, 0] *= 2.0

# Mix data
A = np.array([[1, 1], [0, 2]])  # Mixing matrix

X = np.dot(S, A.T)  # Generate observations
```
