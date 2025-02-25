# Ocultar triángulos no deseados

Ocultamos los triángulos no deseados calculando el punto medio de cada triángulo y comprobando si se encuentra dentro de un radio dado.

```python
xmid = x[triang.triangles].mean(axis=1)
ymid = y[triang.triangles].mean(axis=1)
mask = xmid**2 + ymid**2 < min_radius**2
triang.set_mask(mask)
```
