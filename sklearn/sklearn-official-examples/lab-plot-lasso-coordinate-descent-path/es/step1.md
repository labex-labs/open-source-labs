# Cargar el conjunto de datos

En este paso, cargaremos el conjunto de datos de diabetes de la biblioteca scikit-learn y estandarizaremos los datos.

```python
from sklearn import datasets

# Cargar el conjunto de datos de diabetes
X, y = datasets.load_diabetes(return_X_y=True)

# Estandarizar datos
X /= X.std(axis=0)
```
