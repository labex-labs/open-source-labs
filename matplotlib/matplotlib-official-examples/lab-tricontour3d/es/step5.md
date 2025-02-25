# Ocultar triángulos no deseados

Ocultaremos los triángulos no deseados utilizando la media de las coordenadas x e y.

```python
triang.set_mask(np.hypot(x[triang.triangles].mean(axis=1),
                         y[triang.triangles].mean(axis=1))
                < min_radius)
```
