# FeatureHasher

We will benchmark the `FeatureHasher`, which is a method that builds a vector of pre-defined length by applying a hash function to the features (e.g., tokens), then using the hash values directly as feature indices and updating the resulting vector at those indices.

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
