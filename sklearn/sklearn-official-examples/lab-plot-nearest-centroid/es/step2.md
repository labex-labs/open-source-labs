# Cargar los datos

A continuación, cargamos el conjunto de datos iris de Scikit-learn y seleccionamos solo las primeras dos características para fines de visualización.

```python
iris = datasets.load_iris()
X = iris.data[:, :2]
y = iris.target
```
