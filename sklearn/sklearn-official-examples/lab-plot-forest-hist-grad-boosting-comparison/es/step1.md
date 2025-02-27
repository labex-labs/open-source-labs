# Cargar el conjunto de datos

Cargaremos el conjunto de datos de viviendas de California utilizando la función `fetch_california_housing` de scikit-learn. Este conjunto de datos consta de 20,640 muestras y 8 características.

```python
from sklearn.datasets import fetch_california_housing

X, y = fetch_california_housing(return_X_y=True, as_frame=True)
n_samples, n_features = X.shape

print(f"El conjunto de datos consta de {n_samples} muestras y {n_features} características")
```
