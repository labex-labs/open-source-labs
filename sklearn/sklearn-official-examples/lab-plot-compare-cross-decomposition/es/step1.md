# Creación del conjunto de datos

Creamos un conjunto de datos con dos conjuntos de datos bidimensionales multivariados covariantes, X e Y. Luego extraemos las direcciones de covarianza, es decir, los componentes de cada conjunto de datos que explican la mayor varianza compartida entre ambos conjuntos de datos.

```python
import numpy as np

n = 500
# 2 vars latentes:
l1 = np.random.normal(size=n)
l2 = np.random.normal(size=n)

latentes = np.array([l1, l1, l2, l2]).T
X = latentes + np.random.normal(size=4 * n).reshape((n, 4))
Y = latentes + np.random.normal(size=4 * n).reshape((n, 4))

X_train = X[: n // 2]
Y_train = Y[: n // 2]
X_test = X[n // 2 :]
Y_test = Y[n // 2 :]

print("Corr(X)")
print(np.round(np.corrcoef(X.T), 2))
print("Corr(Y)")
print(np.round(np.corrcoef(Y.T), 2))
```
