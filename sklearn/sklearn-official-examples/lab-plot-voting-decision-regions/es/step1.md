# Cargar los datos

Cargaremos el conjunto de datos de iris usando el módulo `datasets` de Scikit-Learn. Solo usaremos dos características: la longitud del sépalo y la longitud del pétalo.

```python
from sklearn import datasets

iris = datasets.load_iris()
X = iris.data[:, [0, 2]]
y = iris.target
```
