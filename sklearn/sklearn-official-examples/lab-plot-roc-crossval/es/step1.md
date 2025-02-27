# Cargar y preparar los datos

Primero, cargaremos el conjunto de datos iris utilizando la biblioteca Scikit-learn. El conjunto de datos iris contiene 3 clases de plantas de iris, y crearemos un problema de clasificación binaria eliminando una clase para binarizar el conjunto de datos. También agregaremos características ruidosas para complicar el problema.

```python
import numpy as np
from sklearn.datasets import load_iris

iris = load_iris()
target_names = iris.target_names
X, y = iris.data, iris.target
X, y = X[y!= 2], y[y!= 2]
n_samples, n_features = X.shape

# add noisy features
random_state = np.random.RandomState(0)
X = np.concatenate([X, random_state.randn(n_samples, 200 * n_features)], axis=1)
```
