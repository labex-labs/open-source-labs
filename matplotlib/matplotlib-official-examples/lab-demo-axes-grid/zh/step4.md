# 创建一个 2x2 图像网格，每个图像都有自己的颜色条且颜色条范围不同

我们的最后一个网格同样是一个 2x2 图像网格，每个图像都有自己的颜色条，但这次我们将为每个图像使用不同的颜色条范围。在绘制每个图像时，我们将使用 `vmin` 和 `vmax` 设置颜色条范围。

```python
# 创建一个 2x2 图像网格，每个图像都有自己的颜色条且颜色条范围不同
grid = ImageGrid(
    fig,  # 图形对象
    143,  # 子图位置
    nrows_ncols=(2, 2),  # 行数和列数
    axes_pad=(0.45, 0.15),  # 轴之间的间距
    label_mode="1",  # 标签模式
    share_all=True,  # 在所有图像之间共享颜色条
    cbar_location="right",  # 颜色条位置
    cbar_mode="each",  # 颜色条模式
    cbar_size="7%",  # 颜色条大小
    cbar_pad="2%"  # 颜色条与图像之间的间距
)

# 在网格上绘制图像并添加颜色条
limits = ((0, 1), (-2, 2), (-1.7, 1.4), (-1.5, 1))  # 不同的颜色条范围
for ax, cax, vlim in zip(grid, grid.cbar_axes, limits):
    im = ax.imshow(Z, extent=extent, vmin=vlim[0], vmax=vlim[1])
    cb = cax.colorbar(im)
    cb.set_ticks((vlim[0], vlim[1]))
```
