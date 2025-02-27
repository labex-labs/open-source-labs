# Ajustar los modelos de regresión isotónica y lineal

Ahora ajustaremos tanto el modelo de regresión isotónica como el lineal a los datos generados.

```python
ir = IsotonicRegression(out_of_bounds="clip")
y_ = ir.fit_transform(x, y)

lr = LinearRegression()
lr.fit(x[:, np.newaxis], y)  # x necesita ser 2d para LinearRegression
```
