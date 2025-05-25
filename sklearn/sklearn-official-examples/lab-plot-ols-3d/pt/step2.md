# Ajustar um Modelo de Regressão Linear

Em seguida, ajustamos um modelo de regressão linear ao conjunto de treino.

```python
from sklearn import linear_model

ols = linear_model.LinearRegression()
_ = ols.fit(X_train, y_train)
```
