# Image and Colorbar with Draw-Time Positioning - A Hard Way

In this step, we will create an image and its colorbar with draw-time positioning in a hard way. We will be using `SubplotDivider` from `mpl_toolkits.axes_grid1` to create a divider for the axes and colorbar.

```python
def demo_locatable_axes_hard(fig):
    from mpl_toolkits.axes_grid1 import Size, SubplotDivider

    divider = SubplotDivider(fig, 2, 2, 2, aspect=True)

    # axes for image
    ax = fig.add_subplot(axes_locator=divider.new_locator(nx=0, ny=0))
    # axes for colorbar
    ax_cb = fig.add_subplot(axes_locator=divider.new_locator(nx=2, ny=0))

    divider.set_horizontal([
        Size.AxesX(ax),  # main axes
        Size.Fixed(0.05),  # padding, 0.1 inch
        Size.Fixed(0.2),  # colorbar, 0.3 inch
    ])
    divider.set_vertical([Size.AxesY(ax)])

    Z, extent = get_demo_image()

    im = ax.imshow(Z, extent=extent)
    plt.colorbar(im, cax=ax_cb)
    ax_cb.yaxis.set_tick_params(labelright=False)
```
