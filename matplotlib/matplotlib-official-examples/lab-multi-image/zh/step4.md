# 更新图像

最后，我们将更新图像以响应其他图像规范的变化。这将使我们能够更改一张图像的颜色映射和颜色比例，并让所有其他图像相应地更新。

```python
def update(changed_image):
    for im in images:
        if (changed_image.get_cmap()!= im.get_cmap()
                or changed_image.get_clim()!= im.get_clim()):
            im.set_cmap(changed_image.get_cmap())
            im.set_clim(changed_image.get_clim())

for im in images:
    im.callbacks.connect('changed', update)
```
