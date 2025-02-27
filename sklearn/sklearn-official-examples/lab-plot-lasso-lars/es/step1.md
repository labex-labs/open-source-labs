# Cargar datos

El primer paso es cargar el conjunto de datos de diabetes de Scikit-Learn.

```python
from sklearn import datasets

X, y = datasets.load_diabetes(return_X_y=True)
```
