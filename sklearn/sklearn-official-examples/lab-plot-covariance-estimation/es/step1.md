# Generar datos de muestra

Generamos datos de muestra con 40 características y 20 muestras. Utilizamos la función `np.random.normal()` para crear una distribución normal.

```python
import numpy as np

n_features, n_samples = 40, 20
np.random.seed(42)
base_X_train = np.random.normal(size=(n_samples, n_features))
base_X_test = np.random.normal(size=(n_samples, n_features))

coloring_matrix = np.random.normal(size=(n_features, n_features))
X_train = np.dot(base_X_train, coloring_matrix)
X_test = np.dot(base_X_test, coloring_matrix)
```
