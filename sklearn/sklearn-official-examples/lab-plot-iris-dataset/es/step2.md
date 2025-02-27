# Cargar el Conjunto de Datos Iris

Cargaremos el Conjunto de Datos Iris utilizando la función `load_iris` incorporada en Scikit-learn.

```python
iris = datasets.load_iris()
X = iris.data[:, :2]  # solo tomamos las primeras dos características.
y = iris.target
```
