# Realizar predicciones

Ahora usaremos cada uno de los regresores para hacer las 20 primeras predicciones.

```python
# Realizar predicciones
xt = X[:20]

pred1 = reg1.predict(xt)
pred2 = reg2.predict(xt)
pred3 = reg3.predict(xt)
pred4 = ereg.predict(xt)
```
