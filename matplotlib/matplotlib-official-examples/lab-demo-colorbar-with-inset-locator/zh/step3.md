# 使用内嵌轴添加色条

现在，我们将使用 `inset_axes` 为每幅图像添加一个色条。第一个色条将添加到 `ax1`，第二个添加到 `ax2`。

```python
# 为ax1添加色条
axins1 = inset_axes(
    ax1,
    width="50%",  # 宽度：父边界框宽度的50%
    height="5%",  # 高度：5%
    loc="upper right",
)
axins1.xaxis.set_ticks_position("bottom")
fig.colorbar(im1, cax=axins1, orientation="horizontal", ticks=[1, 2, 3])

# 为ax2添加色条
axins2 = inset_axes(
    ax2,
    width="5%",  # 宽度：父边界框宽度的5%
    height="50%",  # 高度：50%
    loc="lower left",
    bbox_to_anchor=(1.05, 0., 1, 1),
    bbox_transform=ax2.transAxes,
    borderpad=0,
)
fig.colorbar(im2, cax=axins2, ticks=[1, 2, 3])
```
