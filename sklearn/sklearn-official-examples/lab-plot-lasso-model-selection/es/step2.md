# Agregar características aleatorias

Agregaremos algunas características aleatorias a los datos originales para ilustrar mejor la selección de características realizada por el modelo Lasso. Las características aleatorias se generarán utilizando la función `RandomState` de `numpy`.

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
