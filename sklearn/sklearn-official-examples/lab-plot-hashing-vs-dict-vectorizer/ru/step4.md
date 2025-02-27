# FeatureHasher

Мы проведем бенчмарк `FeatureHasher`, который является методом, который строит вектор заданной длины, применяя хэш-функцию к признакам (например, токенам), а затем используя хэш-значения непосредственно в качестве индексов признаков и обновляя результирующий вектор по этим индексам.

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
