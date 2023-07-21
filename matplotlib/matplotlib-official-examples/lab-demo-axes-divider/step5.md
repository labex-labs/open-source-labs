# Image and Colorbar with Draw-Time Positioning - An Easy Way

In this step, we will create an image and its colorbar with draw-time positioning in an easy way. We will be using `make_axes_locatable` from `mpl_toolkits.axes_grid1` to create a divider for the axes and colorbar.

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
