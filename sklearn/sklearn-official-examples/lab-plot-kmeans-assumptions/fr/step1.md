# Génération de données

Nous utiliserons la fonction `make_blobs` de scikit-learn pour générer différents ensembles de données avec des distributions variables. Dans le bloc de code suivant, nous générons quatre ensembles de données :

- Un mélange de grappes gaussiennes
- Des grappes distribuées de manière anisotrope
- Des grappes avec des variances inégales
- Des grappes de tailles inégales

```python
import numpy as np
from sklearn.datasets import make_blobs

n_samples = 1500
random_state = 170
transformation = [[0.60834549, -0.63667341], [-0.40887718, 0.85253229]]

X, y = make_blobs(n_samples=n_samples, random_state=random_state)
X_aniso = np.dot(X, transformation)  # Grappes anisotropes
X_varied, y_varied = make_blobs(
    n_samples=n_samples, cluster_std=[1.0, 2.5, 0.5], random_state=random_state
)  # Variances inégales
X_filtered = np.vstack(
    (X[y == 0][:500], X[y == 1][:100], X[y == 2][:10])
)  # Grappes de tailles inégales
y_filtered = [0] * 500 + [1] * 100 + [2] * 10
```
