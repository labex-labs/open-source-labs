# Etiquetar los puntos más inciertos

Agregaremos las etiquetas manuales a los puntos de datos etiquetados y entrenaremos el modelo con ellos.

```python
y_train[uncertainty_index] = y[uncertainty_index]
lp_model.fit(X, y_train)
```
