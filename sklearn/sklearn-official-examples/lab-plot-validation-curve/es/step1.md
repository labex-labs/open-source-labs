# Carga del conjunto de datos

Comenzaremos cargando el conjunto de datos de dígitos de scikit-learn y seleccionando un subconjunto de los datos para la clasificación binaria de los dígitos 1 y 2.

```python
from sklearn.datasets import load_digits

X, y = load_digits(return_X_y=True)
subset_mask = np.isin(y, [1, 2])  # binary classification: 1 vs 2
X, y = X[subset_mask], y[subset_mask]
```
