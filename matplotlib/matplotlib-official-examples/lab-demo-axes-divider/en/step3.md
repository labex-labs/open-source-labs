# Simple Image and Colorbar

In this step, we will create a simple image and its colorbar. We will be using `imshow()` function from `pyplot` to create the image, and `colorbar()` function to create the colorbar.

```python
def demo_simple_image(ax):
    Z, extent = get_demo_image()

    im = ax.imshow(Z, extent=extent)
    cb = plt.colorbar(im)
    cb.ax.yaxis.set_tick_params(labelright=False)
```
