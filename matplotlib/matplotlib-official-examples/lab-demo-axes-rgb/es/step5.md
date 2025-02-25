# Crear un trazado de RGBAxes con canales separados

En este paso, crearemos un trazado de RGBAxes con canales separados utilizando la función `make_rgb_axes()`. Usaremos el método `imshow()` de los objetos `Axes` para mostrar los canales R, G y B.

```python
def demo_rgb2():
    # Crear una figura y un objeto Axes
    fig, ax = plt.subplots()

    # Crear los objetos Axes de R, G y B utilizando la función make_rgb_axes()
    ax_r, ax_g, ax_b = make_rgb_axes(ax, pad=0.02)

    # Obtener los canales R, G y B y crear el cubo RGB
    r, g, b = get_rgb()
    im_r, im_g, im_b, im_rgb = make_cube(r, g, b)

    # Mostrar la imagen RGB y los canales R, G y B
    ax.imshow(im_rgb)
    ax_r.imshow(im_r)
    ax_g.imshow(im_g)
    ax_b.imshow(im_b)

    # Establecer los parámetros de las marcas de graduación y los colores de las espinas para todos los objetos Axes
    for ax in fig.axes:
        ax.tick_params(direction='in', color='w')
        ax.spines[:].set_color("w")
```
