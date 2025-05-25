# Mascar triângulos indesejados

Mascaremos os triângulos indesejados usando a média das coordenadas x e y.

```python
triang.set_mask(np.hypot(x[triang.triangles].mean(axis=1),
                         y[triang.triangles].mean(axis=1))
                < min_radius)
```
