# Cargar los datos

Cargaremos el conjunto de datos de diabetes de scikit-learn utilizando el método load_diabetes.

```python
from sklearn.datasets import load_diabetes

X, y = load_diabetes(return_X_y=True, as_frame=True)
```
