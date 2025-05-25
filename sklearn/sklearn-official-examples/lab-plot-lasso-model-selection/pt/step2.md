# Adicionando Recursos Aleatórios

Vamos adicionar alguns recursos aleatórios aos dados originais para melhor ilustrar a seleção de recursos realizada pelo modelo Lasso. Os recursos aleatórios serão gerados usando a função `RandomState` do `numpy`.

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
