# Predecir datos de los modelos estimados

Predeciremos los datos del modelo lineal y del regresor RANSAC y compararemos sus resultados.

```python
# Predecir datos de los modelos estimados
line_X = np.arange(X.min(), X.max())[:, np.newaxis]
line_y = lr.predict(line_X)
line_y_ransac = ransac.predict(line_X)
```
