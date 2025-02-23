# Определяем функцию для получения точки повернутой вертикальной линии

Мы определим функцию, которая принимает координаты начала линии, длину линии и угол в градусах в качестве входных параметров и возвращает xy - координаты конца вертикальной линии, повернутой на указанный угол.

```python
def get_point_of_rotated_vertical(origin, line_length, degrees):
    """Return xy coordinates of the vertical line end rotated by degrees."""
    rad = np.deg2rad(-degrees)
    return [origin[0] + line_length * np.sin(rad),
            origin[1] + line_length * np.cos(rad)]
```
