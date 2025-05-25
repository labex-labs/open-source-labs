# Definir a Superfície

Em seguida, definimos a superfície. Neste exemplo, usamos um mapeamento de Möbius para pegar um par `u`, `v` e retornar um triplo `x`, `y`, `z`.

```python
x = (1 + 0.5 * v * np.cos(u / 2.0)) * np.cos(u)
y = (1 + 0.5 * v * np.cos(u / 2.0)) * np.sin(u)
z = 0.5 * v * np.sin(u / 2.0)
```
