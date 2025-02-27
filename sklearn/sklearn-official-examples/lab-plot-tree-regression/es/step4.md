# Predecir

Usaremos los modelos para hacer predicciones en un rango de valores de 0 a 5.

```python
X_test = np.arange(0.0, 5.0, 0.01)[:, np.newaxis]
y_1 = regr_1.predict(X_test)
y_2 = regr_2.predict(X_test)
```
