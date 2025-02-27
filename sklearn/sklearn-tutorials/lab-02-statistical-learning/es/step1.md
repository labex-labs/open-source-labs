# Comprendiendo los Conjuntos de Datos

Scikit-learn representa los conjuntos de datos como matrices bidimensionales, donde el primer eje representa las muestras y el segundo eje representa las características. Echemos un vistazo a un ejemplo utilizando el conjunto de datos iris:

```python
from sklearn import datasets

iris = datasets.load_iris()
data = iris.data
print(data.shape)
```

Salida:

```
(150, 4)
```

El conjunto de datos iris consta de 150 observaciones de iris, con cada observación descrita por 4 características. La forma de la matriz de datos es (150, 4).
