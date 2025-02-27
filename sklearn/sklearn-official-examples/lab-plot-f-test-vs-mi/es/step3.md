# Calcular la prueba F

Ahora calcularemos la puntuación de la prueba F para cada característica. La prueba F solo captura la dependencia lineal entre variables. Normalizaremos las puntuaciones de la prueba F dividiéndolas por la puntuación máxima de la prueba F.

```python
f_test, _ = f_regression(X, y)
f_test /= np.max(f_test)
```
