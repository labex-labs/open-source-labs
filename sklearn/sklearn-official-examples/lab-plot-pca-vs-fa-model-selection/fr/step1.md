# Créer les données

Nous allons créer un ensemble de données simulées composé de 500 échantillons, 25 caractéristiques et un rang de 5. Nous ajouterons également un bruit homoscédaastique et hétéroscédaastique à l'ensemble de données.

```python
import numpy as np
from scipy import linalg

n_samples, n_features, rank = 500, 25, 5
sigma = 1.0
rng = np.random.RandomState(42)
U, _, _ = linalg.svd(rng.randn(n_features, n_features))
X = np.dot(rng.randn(n_samples, rank), U[:, :rank].T)

# Ajout de bruit homoscédaastique
X_homo = X + sigma * rng.randn(n_samples, n_features)

# Ajout de bruit hétéroscédaastique
sigmas = sigma * rng.rand(n_features) + sigma / 2.0
X_hetero = X + rng.randn(n_samples, n_features) * sigmas
```
