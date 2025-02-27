# Hacer predicciones con el modelo

Después de ajustar el modelo, podemos utilizarlo para hacer predicciones en nuevos datos. Vamos a crear una nueva matriz `X_new` y predecir los valores objetivo correspondientes.

```python
# Create new data for prediction
X_new = np.linspace(0, 1, 100)
y_pred = ir.predict(X_new)
```
