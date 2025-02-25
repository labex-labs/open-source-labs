# Создадим вторичную ось

Теперь создадим вторичную ось и преобразуем оси x из градусов в радианы. В качестве прямой функции будем использовать `deg2rad`, а в качестве обратной - `rad2deg`.

```python
def deg2rad(x):
    return x * np.pi / 180

def rad2deg(x):
    return x * 180 / np.pi

secax = ax.secondary_xaxis('top', functions=(deg2rad, rad2deg))
secax.set_xlabel('angle [rad]')
```
