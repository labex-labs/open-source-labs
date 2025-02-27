# Ajustar un modelo de regresión lineal

A continuación, ajustamos un modelo de regresión lineal al conjunto de entrenamiento.

```python
from sklearn import linear_model

ols = linear_model.LinearRegression()
_ = ols.fit(X_train, y_train)
```
