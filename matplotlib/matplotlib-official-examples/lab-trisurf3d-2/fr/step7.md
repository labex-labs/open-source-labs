# Projeter sur les points `x`, `y`, `z`

Nous projetons les paires `rayon`, `angle` sur les points `x`, `y`, `z`.

```python
x = (radii*np.cos(angles)).flatten()
y = (radii*np.sin(angles)).flatten()
z = (np.cos(radii)*np.cos(3*angles)).flatten()
```
