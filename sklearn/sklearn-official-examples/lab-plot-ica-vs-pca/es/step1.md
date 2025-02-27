# Generar datos de muestra

En este paso, generamos datos de muestra utilizando un proceso altamente no gaussiano, una distribución de Student T con un bajo número de grados de libertad.

```python
import numpy as np

from sklearn.decomposition import PCA, FastICA

rng = np.random.RandomState(42)
S = rng.standard_t(1.5, size=(20000, 2))
S[:, 0] *= 2.0

# Mezclar datos
A = np.array([[1, 1], [0, 2]])  # Matriz de mezcla

X = np.dot(S, A.T)  # Generar observaciones
```
