# Cargar el conjunto de datos

A continuación, cargamos el conjunto de datos iris de Scikit-learn.

```python
iris = datasets.load_iris()
X = iris.data[:, 0:2]  # solo tomamos las primeras dos características para la visualización
y = iris.target
n_features = X.shape[1]
```
