# Cargar los datos

Usaremos el conjunto de datos de cáncer de mama de scikit-learn. Este conjunto de datos tiene 30 características y una variable objetivo binaria que indica si un paciente tiene cáncer maligno o benigno.

```python
from sklearn.datasets import load_breast_cancer

X, y = load_breast_cancer(return_X_y=True)
```
