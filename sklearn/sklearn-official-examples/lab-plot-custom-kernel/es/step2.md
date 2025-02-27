# Cargar datos

En este paso, cargaremos el conjunto de datos iris usando el módulo datasets de scikit-learn. Seleccionaremos las primeras dos características del conjunto de datos y la asignaremos a la variable X. También asignaremos la variable objetivo a Y.

```python
iris = datasets.load_iris()
X = iris.data[:, :2]
Y = iris.target
```
