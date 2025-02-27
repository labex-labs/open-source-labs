# Cargar y preparar el conjunto de datos

Primero, cargaremos y prepararemos el conjunto de datos de diabetes. Solo usaremos las primeras 150 muestras para este ejercicio.

```python
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets

X, y = datasets.load_diabetes(return_X_y=True)
X = X[:150]
y = y[:150]
```
