# Realizar predicciones en nuevos datos

Utilizaremos tanto el regresor de bosque aleatorio como el regresor de salida múltiple para realizar predicciones en nuestros datos de prueba.

```python
y_rf = regr_rf.predict(X_test)
y_multirf = regr_multirf.predict(X_test)
```
