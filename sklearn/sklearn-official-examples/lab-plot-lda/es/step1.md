# Generar datos aleatorios

Primero, necesitamos generar datos aleatorios con una característica discriminativa y características ruidosas. Utilizaremos la función `make_blobs` de scikit-learn para generar dos grupos de datos con una característica discriminativa. Luego agregaremos ruido aleatorio a las otras características.

```python
import numpy as np
from sklearn.datasets import make_blobs

def generate_data(n_samples, n_features):
    """Generate random blob-ish data with noisy features.

    This returns an array of input data with shape `(n_samples, n_features)`
    and an array of `n_samples` target labels.

    Only one feature contains discriminative information, the other features
    contain only noise.
    """
    X, y = make_blobs(n_samples=n_samples, n_features=1, centers=[[-2], [2]])

    # add non-discriminative features
    if n_features > 1:
        X = np.hstack([X, np.random.randn(n_samples, n_features - 1)])
    return X, y
```
