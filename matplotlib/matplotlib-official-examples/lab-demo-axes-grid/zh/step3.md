# 创建一个 2x2 图像网格，每个图像都有自己的颜色条

我们的下一个网格将是一个 2x2 图像网格，每个图像都有自己的颜色条。我们将再次使用 `ImageGrid` 函数，但这次我们将 `cbar_mode` 设置为 `"each"`，以指定每个图像都应该有自己的颜色条。

```python
# 创建一个 2x2 图像网格，每个图像都有自己的颜色条
grid = ImageGrid(
    fig,  # 图形对象
    142,  # 子图位置
    nrows_ncols=(2, 2),  # 行数和列数
    axes_pad=0.1,  # 轴之间的间距
    label_mode="1",  # 标签模式
    share_all=True,  # 在所有图像之间共享颜色条
    cbar_location="top",  # 颜色条位置
    cbar_mode="each",  # 颜色条模式
    cbar_size="7%",  # 颜色条大小
    cbar_pad="2%"  # 颜色条与图像之间的间距
)

# 在网格上绘制图像并添加颜色条
for ax, cax in zip(grid, grid.cbar_axes):
    im = ax.imshow(Z, extent=extent)
    cax.colorbar(im)
    cax.tick_params(labeltop=False)
```
