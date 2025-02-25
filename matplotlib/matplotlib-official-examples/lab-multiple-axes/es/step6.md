# Definir la función de animación

El sexto paso es definir la función de animación. Esta función se llamará para cada fotograma de la animación y actualizará la posición del punto en la subtrama izquierda, la posición y los datos de la curva senoidal en la subtrama derecha y la posición del parche de conexión.

```python
def animate(i):
    x = np.linspace(0, i, int(i * 25 / np.pi))
    sine.set_data(x, np.sin(x))
    x, y = np.cos(i), np.sin(i)
    point.set_data([x], [y])
    con.xy1 = x, y
    con.xy2 = i, y
    return point, sine, con
```
