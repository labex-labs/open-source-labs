# Mapear a los puntos `x`, `y`, `z`

Mapeamos los pares `radius` (radio), `angle` (ángulo) a los puntos `x`, `y`, `z`.

```python
x = (radii*np.cos(angles)).flatten()
y = (radii*np.sin(angles)).flatten()
z = (np.cos(radii)*np.cos(3*angles)).flatten()
```
