# Charger les données

Nous commençons par charger l'ensemble de données iris et en ajoutant 36 caractéristiques non informatives.

```python
import numpy as np
from sklearn.datasets import load_iris

X, y = load_iris(return_X_y=True)

# Add non-informative features
rng = np.random.RandomState(0)
X = np.hstack((X, 2 * rng.random((X.shape[0], 36))))
```
