# Entrenar el modelo

Ahora, creamos un objeto de regresión lineal y entrenamos el modelo utilizando los conjuntos de entrenamiento.

```python
from sklearn import linear_model

# Crear objeto de regresión lineal
regr = linear_model.LinearRegression()

# Entrenar el modelo utilizando los conjuntos de entrenamiento
regr.fit(diabetes_X_train, diabetes_y_train)
```
