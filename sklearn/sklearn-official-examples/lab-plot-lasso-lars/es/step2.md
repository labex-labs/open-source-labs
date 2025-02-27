# Calcular el camino de Lasso

A continuación, calculamos el camino de Lasso utilizando el algoritmo LARS. La función `lars_path` del módulo `linear_model` de Scikit-Learn se utiliza para calcular el camino de Lasso. La función toma las características de entrada, la variable objetivo y el método como parámetros. En este caso, usamos el método "lasso" para la regularización L1.

```python
from sklearn import linear_model

_, _, coefs = linear_model.lars_path(X, y, method="lasso", verbose=True)
```
