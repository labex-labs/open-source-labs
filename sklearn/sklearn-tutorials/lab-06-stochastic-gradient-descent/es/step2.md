# Cargar datos

A continuación, cargaremos el conjunto de datos iris de scikit-learn. Este conjunto de datos es un conjunto de datos clásico de aprendizaje automático que consta de mediciones de flores de iris, junto con sus etiquetas de especies.

```python
iris = load_iris()
X = iris.data
y = iris.target
```
