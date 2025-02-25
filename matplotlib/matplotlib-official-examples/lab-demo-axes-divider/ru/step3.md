# Простое изображение и цветовая полоса

В этом шаге мы создадим простое изображение и его цветовую полосу. Мы будем использовать функцию `imshow()` из `pyplot`, чтобы создать изображение, и функцию `colorbar()`, чтобы создать цветовую полосу.

```python
def demo_simple_image(ax):
    Z, extent = get_demo_image()

    im = ax.imshow(Z, extent=extent)
    cb = plt.colorbar(im)
    cb.ax.yaxis.set_tick_params(labelright=False)
```
