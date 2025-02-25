# Masquer les triangles indésirables

Nous allons masquer les triangles indésirables en calculant la moyenne des coordonnées x et y des sommets de chaque triangle et en la comparant au rayon minimum.

```python
triang.set_mask(np.hypot(x[triang.triangles].mean(axis=1),
                         y[triang.triangles].mean(axis=1))
                < min_radius)
```
