# Cargar los datos

Comenzamos cargando el conjunto de datos iris y agregando 36 características no informativas a él.

```python
import numpy as np
from sklearn.datasets import load_iris

X, y = load_iris(return_X_y=True)

# Add non-informative features
rng = np.random.RandomState(0)
X = np.hstack((X, 2 * rng.random((X.shape[0], 36))))
```
