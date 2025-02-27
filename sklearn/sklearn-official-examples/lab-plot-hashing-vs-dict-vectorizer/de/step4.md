# FeatureHasher

Wir werden den `FeatureHasher` benchmarken, der eine Methode ist, die einen Vektor von vorgegebener Länge erstellt, indem eine Hash-Funktion auf die Merkmale (z.B. Tokens) angewendet wird, und dann die Hash-Werte direkt als Merkmalseindizes verwendet und der resultierende Vektor an diesen Indizes aktualisiert wird.

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
