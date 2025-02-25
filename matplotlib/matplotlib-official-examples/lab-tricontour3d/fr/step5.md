# Masquer les triangles indésirables

Nous allons masquer les triangles indésirables en utilisant la moyenne des coordonnées x et y.

```python
triang.set_mask(np.hypot(x[triang.triangles].mean(axis=1),
                         y[triang.triangles].mean(axis=1))
                < min_radius)
```
