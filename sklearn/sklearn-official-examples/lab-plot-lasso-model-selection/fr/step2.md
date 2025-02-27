# Ajout de fonctionnalités aléatoires

Nous allons ajouter quelques fonctionnalités aléatoires aux données d'origine pour mieux illustrer la sélection de fonctionnalités effectuée par le modèle Lasso. Les fonctionnalités aléatoires seront générées à l'aide de la fonction `RandomState` de `numpy`.

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
