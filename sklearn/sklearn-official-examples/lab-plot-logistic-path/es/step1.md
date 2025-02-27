# Cargar el conjunto de datos Iris

Cargaremos el conjunto de datos Iris desde la biblioteca scikit-learn. El conjunto de datos contiene cuatro características: longitud del sépalo, ancho del sépalo, longitud del pétalo y ancho del pétalo. Usaremos solo las dos primeras características para la clasificación binaria.

```python
from sklearn import datasets

iris = datasets.load_iris()
X = iris.data
y = iris.target

X = X[y!= 2] # Use only first two features for binary classification
y = y[y!= 2]

X /= X.max() # Normalize X to speed-up convergence
```
