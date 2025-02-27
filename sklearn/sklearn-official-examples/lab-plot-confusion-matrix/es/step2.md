# Cargar datos

Usaremos el conjunto de datos iris de scikit-learn. El conjunto de datos contiene 150 muestras, cada una con cuatro características y una etiqueta de destino.

```python
iris = datasets.load_iris()
X = iris.data
y = iris.target
class_names = iris.target_names
```
