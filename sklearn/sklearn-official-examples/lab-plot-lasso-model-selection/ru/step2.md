# Добавление случайных признаков

Мы добавим некоторые случайные признаки к исходным данным, чтобы лучше проиллюстрировать отбор признаков, выполняемый моделью Lasso. Случайные признаки будут генерироваться с использованием функции `RandomState` из `numpy`.

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
