# Изображение и цветовая полоса с позиционированием при рисовании - простой способ

В этом шаге мы создадим изображение и его цветовую полосу с позиционированием при рисовании простым способом. Мы будем использовать `make_axes_locatable` из `mpl_toolkits.axes_grid1`, чтобы создать разделитель для осей и цветовой полосы.

```python
def demo_locatable_axes_easy(ax):
    from mpl_toolkits.axes_grid1 import make_axes_locatable

    divider = make_axes_locatable(ax)

    ax_cb = divider.append_axes("right", size="5%", pad=0.05)
    fig = ax.get_figure()
    fig.add_axes(ax_cb)

    Z, extent = get_demo_image()
    im = ax.imshow(Z, extent=extent)

    plt.colorbar(im, cax=ax_cb)
    ax_cb.yaxis.tick_right()
    ax_cb.yaxis.set_tick_params(labelright=False)
```
