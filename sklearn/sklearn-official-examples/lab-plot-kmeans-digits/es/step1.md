# Cargar el conjunto de datos

Comenzaremos cargando el conjunto de datos de dígitos utilizando la función `load_digits()` de scikit-learn. Esta función devuelve las características y las etiquetas del conjunto de datos.

```python
import numpy as np
from sklearn.datasets import load_digits

data, labels = load_digits(return_X_y=True)
(n_samples, n_features), n_digits = data.shape, np.unique(labels).size
```
