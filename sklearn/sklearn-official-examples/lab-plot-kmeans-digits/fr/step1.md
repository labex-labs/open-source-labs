# Charger l'ensemble de données

Nous commencerons par charger l'ensemble de données de chiffres à l'aide de la fonction `load_digits()` de scikit-learn. Cette fonction renvoie les caractéristiques et les étiquettes pour l'ensemble de données.

```python
import numpy as np
from sklearn.datasets import load_digits

data, labels = load_digits(return_X_y=True)
(n_samples, n_features), n_digits = data.shape, np.unique(labels).size
```
