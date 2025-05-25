# FeatureHasher

Vamos avaliar o `FeatureHasher`, que é um método que constrói um vetor de comprimento pré-definido aplicando uma função hash aos recursos (por exemplo, tokens), depois usando os valores hash diretamente como índices de recursos e atualizando o vetor resultante nesses índices.

```python
from sklearn.feature_extraction import FeatureHasher
import numpy as np

t0 = time()
hasher = FeatureHasher(n_features=2**18)
X = hasher.transform(token_freqs(d) for d in raw_data)
duration = time() - t0
print(f"feito em {duration:.3f} s")
print(f"Encontrados {len(np.unique(X.nonzero()[1]))} tokens únicos")
```
