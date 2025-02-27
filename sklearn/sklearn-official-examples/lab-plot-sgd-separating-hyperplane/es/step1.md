# Importar las bibliotecas necesarias y generar datos

Primero, necesitamos importar las bibliotecas necesarias y generar un conjunto de datos adecuado para la clasificación. En este ejemplo, generaremos 50 puntos separables utilizando la función `make_blobs` de Scikit-learn.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import SGDClassifier
from sklearn.datasets import make_blobs

# creamos 50 puntos separables
X, Y = make_blobs(n_samples=50, centers=2, random_state=0, cluster_std=0.60)
```
