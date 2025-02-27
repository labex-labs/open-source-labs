# Cargar el conjunto de datos

A continuación, cargaremos el conjunto de datos Iris utilizando la función `load_iris()` de scikit-learn. Luego, separaremos las variables de características (X) y objetivo (y).

```python
iris = datasets.load_iris()
X = iris.data
y = iris.target
```
