# Ajustar el modelo de regresión isotónica

Ahora, podemos ajustar el modelo de regresión isotónica a nuestros datos. Creamos una instancia de la clase `IsotonicRegression` y llamamos al método `fit` con nuestros datos de entrada y valores objetivo.

```python
# Fit isotonic regression model
ir = IsotonicRegression()
ir.fit(X, y)
```
