# Cargar y preparar los datos

Comenzamos importando las bibliotecas necesarias y cargando el conjunto de datos iris. Luego barajaremos los datos y los estandarizaremos para usarlos en el entrenamiento.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.linear_model import SGDClassifier

# cargar el conjunto de datos iris
iris = datasets.load_iris()

# tomar las primeras dos características
X = iris.data[:, :2]
y = iris.target
colors = "bry"

# barajar los datos
idx = np.arange(X.shape[0])
np.random.seed(13)
np.random.shuffle(idx)
X = X[idx]
y = y[idx]

# estandarizar los datos
mean = X.mean(axis=0)
std = X.std(axis=0)
X = (X - mean) / std
```
