# Cargar datos

```python
X, y = datasets.load_breast_cancer(return_X_y=True)
X, y = shuffle(X, y, random_state=42)
y_true = y.copy()
y[50:] = -1
total_samples = y.shape[0]
```

Se carga y mezcla el conjunto de datos `breast_cancer`. Luego copiamos las etiquetas reales a `y_true` y eliminamos todas las etiquetas excepto las primeras 50 muestras de `y`. Esto se utilizará para simular un escenario de aprendizaje semi-supervisado.
