# FeatureHasher

Evaluaremos el `FeatureHasher`, que es un método que construye un vector de longitud predefinida aplicando una función de hash a las características (por ejemplo, tokens), luego utilizando los valores de hash directamente como índices de características y actualizando el vector resultante en esos índices.

```python
from sklearn.feature_extraction import FeatureHasher
import numpy as np

t0 = time()
hasher = FeatureHasher(n_features=2**18)
X = hasher.transform(token_freqs(d) for d in raw_data)
duration = time() - t0
print(f"hecho en {duration:.3f} s")
print(f"Encontrados {len(np.unique(X.nonzero()[1]))} tokens únicos")
```
