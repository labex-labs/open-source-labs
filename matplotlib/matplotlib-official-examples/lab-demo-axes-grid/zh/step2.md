# 创建一个带有单个颜色条的 2x2 图像网格

我们的第一个网格将是一个带有单个颜色条的 2x2 图像网格。我们将使用 `ImageGrid` 函数来创建网格，并指定我们想要的行数和列数。我们还将指定颜色条的位置，并将 `share_all` 设置为 `True`，以便在所有图像之间共享颜色条。

```python
# 创建一个带有单个颜色条的 2x2 图像网格
grid = ImageGrid(
    fig,  # 图形对象
    141,  # 子图位置
    nrows_ncols=(2, 2),  # 行数和列数
    axes_pad=0.0,  # 轴之间的间距
    label_mode="L",  # 标签模式
    share_all=True,  # 在所有图像之间共享颜色条
    cbar_location="top",  # 颜色条位置
    cbar_mode="single"  # 颜色条模式
)

# 在网格上绘制图像
for ax in grid:
    im = ax.imshow(Z, extent=extent)

# 向网格添加颜色条
grid.cbar_axes[0].colorbar(im)
for cax in grid.cbar_axes:
    cax.tick_params(labeltop=False)
```
