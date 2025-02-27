# Données

Nous générons un ensemble de données de classification avec 2000 échantillons, 2 caractéristiques et 3 classes cibles. Nous divisons ensuite les données comme suit :

- entraînement : 600 échantillons (pour entraîner le classifieur)
- validation : 400 échantillons (pour étalonner les probabilités prédites)
- test : 1000 échantillons

```python
import numpy as np
from sklearn.datasets import make_blobs

np.random.seed(0)

X, y = make_blobs(
    n_samples=2000, n_features=2, centers=3, random_state=42, cluster_std=5.0
)
X_train, y_train = X[:600], y[:600]
X_valid, y_valid = X[600:1000], y[600:1000]
X_train_valid, y_train_valid = X[:1000], y[:1000]
X_test, y_test = X[1000:], y[1000:]
```
