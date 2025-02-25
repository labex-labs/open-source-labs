# Imagen y barra de color simples

En este paso, crearemos una imagen simple y su barra de color. Utilizaremos la función `imshow()` de `pyplot` para crear la imagen y la función `colorbar()` para crear la barra de color.

```python
def demo_simple_image(ax):
    Z, extent = get_demo_image()

    im = ax.imshow(Z, extent=extent)
    cb = plt.colorbar(im)
    cb.ax.yaxis.set_tick_params(labelright=False)
```
