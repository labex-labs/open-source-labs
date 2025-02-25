# Crear dos histogramas con barras apiladas

Podemos crear dos histogramas con barras apiladas llamando a la función `hist` dos veces y estableciendo el parámetro `histtype` en `'barstacked'`. En este ejemplo, crearemos dos histogramas con barras apiladas.

```python
plt.hist(x, density=True, histtype='barstacked', rwidth=0.8)
plt.hist(w, density=True, histtype='barstacked', rwidth=0.8)
plt.show()
```
