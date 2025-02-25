# Crear un trazado de RGBAxes

En este paso, crearemos un trazado de RGBAxes utilizando la clase `RGBAxes`. Usaremos el método `imshow_rgb()` del objeto `RGBAxes` para mostrar la imagen RGB.

```python
def demo_rgb1():
    # Crear una figura y un objeto RGBAxes
    fig = plt.figure()
    ax = RGBAxes(fig, [0.1, 0.1, 0.8, 0.8], pad=0.0)

    # Obtener los canales R, G y B
    r, g, b = get_rgb()

    # Mostrar la imagen RGB utilizando el método imshow_rgb()
    ax.imshow_rgb(r, g, b)
```
