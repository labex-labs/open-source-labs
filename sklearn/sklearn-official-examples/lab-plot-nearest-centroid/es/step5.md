# Predecir y medir la precisión

Predecimos las etiquetas de clase para los datos de entrada y medimos la precisión del clasificador.

```python
y_pred = clf.predict(X)
print("Precisión: ", np.mean(y == y_pred))
```
