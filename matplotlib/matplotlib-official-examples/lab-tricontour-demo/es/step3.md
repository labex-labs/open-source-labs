# Ocultar triángulos no deseados

Utilizaremos el método `set_mask` para ocultar los triángulos no deseados.

```python
triang.set_mask(np.hypot(x[triang.triangles].mean(axis=1),
                         y[triang.triangles].mean(axis=1))
                < min_radius)
```
