# Cargar y preparar los datos

Primero, cargaremos el conjunto de datos de diabetes y lo prepararemos para el modelado. Usaremos la función `load_diabetes` de scikit-learn para cargar el conjunto de datos en dos matrices, `X` e `y`.

```python
from sklearn.datasets import load_diabetes

X, y = load_diabetes(return_X_y=True)
```
