# Generar datos de muestra

Primero, generaremos algunos datos de muestra para la demostración. Utilizaremos el conjunto de datos iris y le agregaremos algunos datos ruidosos no correlacionados.

```python
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

# El conjunto de datos iris
X, y = load_iris(return_X_y=True)

# Algunos datos ruidosos no correlacionados
E = np.random.RandomState(42).uniform(0, 0.1, size=(X.shape[0], 20))

# Agregar los datos ruidosos a las características informativas
X = np.hstack((X, E))

# Dividir el conjunto de datos para seleccionar características y evaluar el clasificador
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=0)
```
