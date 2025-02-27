# Datos

Generamos un conjunto de datos de clasificación con 2000 muestras, 2 características y 3 clases de destino. Luego dividimos los datos de la siguiente manera:

- entrenamiento: 600 muestras (para entrenar el clasificador)
- validación: 400 muestras (para calcular las probabilidades predichas)
- prueba: 1000 muestras

```python
import numpy as np
from sklearn.datasets import make_blobs

np.random.seed(0)

X, y = make_blobs(
    n_samples=2000, n_features=2, centers=3, random_state=42, cluster_std=5.0
)
X_train, y_train = X[:600], y[:600]
X_valid, y_valid = X[600:1000], y[600:1000]
X_train_valid, y_train_valid = X[:1000], y[:1000]
X_test, y_test = X[1000:], y[1000:]
```
