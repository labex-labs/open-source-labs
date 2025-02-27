# Cargar el conjunto de datos

Cargaremos el conjunto de datos de dígitos utilizando `datasets.load_digits(return_X_y=True)`. También estandarizaremos los datos utilizando `StandardScaler().fit_transform(X)`. La variable objetivo será binaria, donde los valores de 0-4 se clasifican como 0 y los valores de 5-9 se clasifican como 1.

```python
X, y = datasets.load_digits(return_X_y=True)
X = StandardScaler().fit_transform(X)
y = (y > 4).astype(int)
```
