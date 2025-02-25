# Два изображения рядом с фиксированным отступом

В этом шаге мы создадим два изображения рядом с фиксированным отступом. Мы будем использовать `make_axes_locatable` из `mpl_toolkits.axes_grid1`, чтобы создать разделитель для осей и цветовой полосы.

```python
def demo_images_side_by_side(ax):
    from mpl_toolkits.axes_grid1 import make_axes_locatable

    divider = make_axes_locatable(ax)

    Z, extent = get_demo_image()
    ax2 = divider.append_axes("right", size="100%", pad=0.05)
    fig1 = ax.get_figure()
    fig1.add_axes(ax2)

    ax.imshow(Z, extent=extent)
    ax2.imshow(Z, extent=extent)
    ax2.yaxis.set_tick_params(labelleft=False)
```
