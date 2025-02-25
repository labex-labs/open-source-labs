# Отображаем на точки `x`, `y`, `z`

Мы отображаем пары `радиус`, `угол` на точки `x`, `y`, `z`.

```python
x = (radii*np.cos(angles)).flatten()
y = (radii*np.sin(angles)).flatten()
z = (np.cos(radii)*np.cos(3*angles)).flatten()
```
