# Crear el eje secundario

Ahora crearemos el eje secundario y convertiremos el eje x de grados a radianes. Usaremos `deg2rad` como función directa y `rad2deg` como función inversa.

```python
def deg2rad(x):
    return x * np.pi / 180

def rad2deg(x):
    return x * 180 / np.pi

secax = ax.secondary_xaxis('top', functions=(deg2rad, rad2deg))
secax.set_xlabel('ángulo [rad]')
```
