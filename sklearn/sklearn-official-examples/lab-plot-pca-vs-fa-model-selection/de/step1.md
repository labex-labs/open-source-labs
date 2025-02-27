# Daten erstellen

Wir werden einen simulierten Datensatz erstellen, der aus 500 Proben, 25 Merkmalen und einem Rang von 5 besteht. Wir werden auch homoskedastische und heteroskedastische Störungen zum Datensatz hinzufügen.

```python
import numpy as np
from scipy import linalg

n_samples, n_features, rank = 500, 25, 5
sigma = 1.0
rng = np.random.RandomState(42)
U, _, _ = linalg.svd(rng.randn(n_features, n_features))
X = np.dot(rng.randn(n_samples, rank), U[:, :rank].T)

# Homoskedastische Störung hinzufügen
X_homo = X + sigma * rng.randn(n_samples, n_features)

# Heteroskedastische Störung hinzufügen
sigmas = sigma * rng.rand(n_features) + sigma / 2.0
X_hetero = X + rng.randn(n_samples, n_features) * sigmas
```
