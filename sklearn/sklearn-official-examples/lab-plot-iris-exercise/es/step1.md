# Cargar los datos

Comenzaremos cargando el conjunto de datos Iris y seleccionando solo las primeras dos características con fines de visualización.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets, svm

iris = datasets.load_iris()
X = iris.data
y = iris.target

X = X[y!= 0, :2]
y = y[y!= 0]
```
