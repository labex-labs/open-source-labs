# Combinando as Cores

Agora combinaremos os componentes de cor RGB em um único array com a forma `(17, 17, 17, 3)`.

```python
colors = np.zeros(sphere.shape + (3,))
colors[..., 0] = rc
colors[..., 1] = gc
colors[..., 2] = bc
```
