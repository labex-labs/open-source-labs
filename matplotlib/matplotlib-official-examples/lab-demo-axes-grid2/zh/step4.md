# 演示 1 - 每个轴上都有颜色条

我们将使用以下代码创建一个包含 3 张图像的网格，每个轴上都有一个颜色条：

```python
grid = ImageGrid(
    fig, 211, nrows_ncols=(1, 3), axes_pad=0.05, label_mode="1", share_all=True,
    cbar_location="top", cbar_mode="each", cbar_size="7%", cbar_pad="1%")
grid[0].set(xticks=[-2, 0], yticks=[-2, 0, 2])

for i, (ax, z) in enumerate(zip(grid, ZS)):
    im = ax.imshow(z, origin="lower", extent=extent)
    cb = ax.cax.colorbar(im)
    # 更改颜色条刻度
    if i in [1, 2]:
        cb.set_ticks([-1, 0, 1])

for ax, im_title in zip(grid, ["图像 1", "图像 2", "图像 3"]):
    add_inner_title(ax, im_title, loc='lower left')
```

- 我们使用 `ImageGrid` 创建一个包含 3 张图像的网格。
- 我们将 `cbar_mode` 设置为 "each"，以便在每个轴上添加一个颜色条。
- 我们将 `share_all` 参数设置为 True，以便在所有图像之间共享 x 轴和 y 轴。
- 我们将 `cbar_location` 参数设置为 "top"，以便将颜色条定位在顶部。
- 我们为第一张图像设置 `xticks` 和 `yticks`。
- 我们遍历每张图像，并使用 `imshow` 将图像添加到轴上。
- 我们使用 `ax.cax.colorbar` 为每个轴添加一个颜色条。
- 我们为第二张和第三张图像设置颜色条刻度。
- 我们使用 `add_inner_title` 为每张图像添加一个标题。
