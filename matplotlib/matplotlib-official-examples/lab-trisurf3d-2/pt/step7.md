# Mapear para os Pontos `x`, `y`, `z`

Mapeamos os pares `radius`, `angle` para os pontos `x`, `y`, `z`.

```python
x = (radii*np.cos(angles)).flatten()
y = (radii*np.sin(angles)).flatten()
z = (np.cos(radii)*np.cos(3*angles)).flatten()
```
