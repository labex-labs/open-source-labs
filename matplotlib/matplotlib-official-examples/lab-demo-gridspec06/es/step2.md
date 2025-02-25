# Crear datos

En este paso, crearemos algunos datos para graficar. Usaremos la función `squiggle_xy` para generar algunas ondas senoidales y cosenoidales con diferentes frecuencias.

```python
def squiggle_xy(a, b, c, d):
    i = np.arange(0.0, 2*np.pi, 0.05)
    return np.sin(i*a)*np.cos(i*b), np.sin(i*c)*np.cos(i*d)
```
