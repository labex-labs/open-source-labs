# Definir la superficie

A continuación, definimos la superficie. En este ejemplo, usamos una transformación de Möbius para tomar un par `u`, `v` y devolver una triple `x`, `y`, `z`.

```python
x = (1 + 0.5 * v * np.cos(u / 2.0)) * np.cos(u)
y = (1 + 0.5 * v * np.cos(u / 2.0)) * np.sin(u)
z = 0.5 * v * np.sin(u / 2.0)
```
