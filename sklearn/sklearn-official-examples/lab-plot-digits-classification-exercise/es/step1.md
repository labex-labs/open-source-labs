# Cargar el conjunto de datos Digits

Comenzaremos cargando el conjunto de datos Digits utilizando la función `load_digits` de scikit-learn. Esta función devuelve dos matrices: `X_digits` que contiene los datos de entrada y `y_digits` que contiene las etiquetas de destino.

```python
from sklearn import datasets

X_digits, y_digits = datasets.load_digits(return_X_y=True)
```
