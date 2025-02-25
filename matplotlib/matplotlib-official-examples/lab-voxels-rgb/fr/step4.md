# Combinaison des couleurs

Nous allons maintenant combiner les composantes de couleur RGB en un seul tableau de forme `(17, 17, 17, 3)`.

```python
colors = np.zeros(sphere.shape + (3,))
colors[..., 0] = rc
colors[..., 1] = gc
colors[..., 2] = bc
```
