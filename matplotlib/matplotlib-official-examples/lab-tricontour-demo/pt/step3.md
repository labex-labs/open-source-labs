# Mascar triângulos indesejados

Usaremos o método `set_mask` para mascarar os triângulos indesejados.

```python
triang.set_mask(np.hypot(x[triang.triangles].mean(axis=1),
                         y[triang.triangles].mean(axis=1))
                < min_radius)
```
