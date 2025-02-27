# FeatureHasher

`FeatureHasher` をベンチマークします。これは、特徴量（例えば、トークン）にハッシュ関数を適用することで事前に定義された長さのベクトルを構築し、そのハッシュ値を直接特徴量インデックスとして使用し、それらのインデックスで結果のベクトルを更新する方法です。

```python
from sklearn.feature_extraction import FeatureHasher
import numpy as np

t0 = time()
hasher = FeatureHasher(n_features=2**18)
X = hasher.transform(token_freqs(d) for d in raw_data)
duration = time() - t0
print(f"done in {duration:.3f} s")
print(f"Found {len(np.unique(X.nonzero()[1]))} unique tokens")
```
