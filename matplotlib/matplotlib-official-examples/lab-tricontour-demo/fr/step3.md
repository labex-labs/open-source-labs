# Masquer les triangles indésirables

Nous allons utiliser la méthode `set_mask` pour masquer les triangles indésirables.

```python
triang.set_mask(np.hypot(x[triang.triangles].mean(axis=1),
                         y[triang.triangles].mean(axis=1))
                < min_radius)
```
