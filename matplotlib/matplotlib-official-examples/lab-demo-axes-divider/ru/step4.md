# Изображение и цветовая полоса с позиционированием при рисовании - сложный способ

В этом шаге мы создадим изображение и его цветовую полосу с позиционированием при рисовании сложным способом. Мы будем использовать `SubplotDivider` из `mpl_toolkits.axes_grid1`, чтобы создать разделитель для осей и цветовой полосы.

```python
def demo_locatable_axes_hard(fig):
    from mpl_toolkits.axes_grid1 import Size, SubplotDivider

    divider = SubplotDivider(fig, 2, 2, 2, aspect=True)

    # оси для изображения
    ax = fig.add_subplot(axes_locator=divider.new_locator(nx=0, ny=0))
    # оси для цветовой полосы
    ax_cb = fig.add_subplot(axes_locator=divider.new_locator(nx=2, ny=0))

    divider.set_horizontal([
        Size.AxesX(ax),  # основные оси
        Size.Fixed(0.05),  # отступ, 0.1 дюйм
        Size.Fixed(0.2),  # цветовая полоса, 0.3 дюйм
    ])
    divider.set_vertical([Size.AxesY(ax)])

    Z, extent = get_demo_image()

    im = ax.imshow(Z, extent=extent)
    plt.colorbar(im, cax=ax_cb)
    ax_cb.yaxis.set_tick_params(labelright=False)
```
