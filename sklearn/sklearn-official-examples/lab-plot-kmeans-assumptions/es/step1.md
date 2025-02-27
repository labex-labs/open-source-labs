# Generación de datos

Utilizaremos la función `make_blobs` de scikit-learn para generar diferentes conjuntos de datos con distribuciones variables. En el siguiente bloque de código, generamos cuatro conjuntos de datos:

- Una mezcla de cúmulos gaussianos
- Cúmulos con distribución anisotrópica
- Cúmulos con varianza desigual
- Cúmulos de tamaños desiguales

```python
import numpy as np
from sklearn.datasets import make_blobs

n_samples = 1500
random_state = 170
transformation = [[0.60834549, -0.63667341], [-0.40887718, 0.85253229]]

X, y = make_blobs(n_samples=n_samples, random_state=random_state)
X_aniso = np.dot(X, transformation)  # Cúmulos anisotrópicos
X_varied, y_varied = make_blobs(
    n_samples=n_samples, cluster_std=[1.0, 2.5, 0.5], random_state=random_state
)  # Varianza desigual
X_filtered = np.vstack(
    (X[y == 0][:500], X[y == 1][:100], X[y == 2][:10])
)  # Cúmulos de tamaños desiguales
y_filtered = [0] * 500 + [1] * 100 + [2] * 10
```
