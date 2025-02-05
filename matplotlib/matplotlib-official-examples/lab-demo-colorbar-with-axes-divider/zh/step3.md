# 为绘图添加颜色条

现在，我们将使用 Matplotlib 的 `make_axes_locatable` 函数为每个子图添加颜色条。此函数接受一个现有的坐标轴，将其添加到一个新的 `AxesDivider` 中，并返回 `AxesDivider`。然后，可以使用 `AxesDivider` 的 `append_axes` 方法在原始坐标轴的给定一侧（“顶部”、“右侧”、“底部” 或 “左侧”）创建一个新的坐标轴。

```python
ax1_divider = make_axes_locatable(ax1)
cax1 = ax1_divider.append_axes("right", size="7%", pad="2%")
cb1 = fig.colorbar(im1, cax=cax1)

ax2_divider = make_axes_locatable(ax2)
cax2 = ax2_divider.append_axes("top", size="7%", pad="2%")
cb2 = fig.colorbar(im2, cax=cax2, orientation="horizontal")
cax2.xaxis.set_ticks_position("top")
```
