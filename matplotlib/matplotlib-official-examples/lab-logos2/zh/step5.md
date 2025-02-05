# 创建徽标

在这一步中，我们将创建带有 Matplotlib 徽标的完整图形。

```python
def make_logo(height_px, lw_bars, lw_grid, lw_border, rgrid, with_text=False):
    """
    创建带有 Matplotlib 徽标的完整图形。

    参数
    ----------
    height_px : int
        图形的高度（以像素为单位）。
    lw_bars : float
        条形图边框的线宽。
    lw_grid : float
        网格的线宽。
    lw_border : float
        图标边框的线宽。
    rgrid : 浮点数序列
        径向网格位置。
    with_text : bool
        是否只绘制图标，还是包含文本“matplotlib”。
    """
    dpi = 100
    height = height_px / dpi
    figsize = (5 * height, height) if with_text else (height, height)
    fig = plt.figure(figsize=figsize, dpi=dpi)
    fig.patch.set_alpha(0)

    if with_text:
        create_text_axes(fig, height_px)
    ax_pos = (0.535, 0.12,.17, 0.75) if with_text else (0.03, 0.03,.94,.94)
    ax = create_icon_axes(fig, ax_pos, lw_bars, lw_grid, lw_border, rgrid)

    return fig, ax
```
