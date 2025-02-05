# 简单图像与颜色条

在这一步中，我们将创建一个简单的图像及其颜色条。我们将使用 `pyplot` 中的 `imshow()` 函数来创建图像，并使用 `colorbar()` 函数来创建颜色条。

```python
def demo_simple_image(ax):
    Z, extent = get_demo_image()

    im = ax.imshow(Z, extent=extent)
    cb = plt.colorbar(im)
    cb.ax.yaxis.set_tick_params(labelright=False)
```
