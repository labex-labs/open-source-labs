# Einfaches Bild und Farbskala

In diesem Schritt werden wir ein einfaches Bild und seine Farbskala erstellen. Wir werden die Funktion `imshow()` aus `pyplot` verwenden, um das Bild zu erstellen, und die Funktion `colorbar()` verwenden, um die Farbskala zu erstellen.

```python
def demo_simple_image(ax):
    Z, extent = get_demo_image()

    im = ax.imshow(Z, extent=extent)
    cb = plt.colorbar(im)
    cb.ax.yaxis.set_tick_params(labelright=False)
```
