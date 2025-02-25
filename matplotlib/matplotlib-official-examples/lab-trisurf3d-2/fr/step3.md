# Définir la surface

Ensuite, nous définissons la surface. Dans cet exemple, nous utilisons une transformation de Möbius pour prendre une paire `u`, `v` et retourner un triplet `x`, `y`, `z`.

```python
x = (1 + 0.5 * v * np.cos(u / 2.0)) * np.cos(u)
y = (1 + 0.5 * v * np.cos(u / 2.0)) * np.sin(u)
z = 0.5 * v * np.sin(u / 2.0)
```
