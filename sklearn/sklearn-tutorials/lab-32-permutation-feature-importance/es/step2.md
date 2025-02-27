# Entrenar el modelo

A continuación, entrenaremos un modelo de regresión con los datos de entrenamiento. En este ejemplo, utilizaremos un modelo de regresión Ridge.

```python
from sklearn.linear_model import Ridge

# Entrenar el modelo de regresión Ridge
model = Ridge(alpha=1e-2).fit(X_train, y_train)
```
