# 固定パディング付きで横並びの2つの画像

このステップでは、固定パディング付きで横並びの2つの画像を作成します。`mpl_toolkits.axes_grid1` から `make_axes_locatable` を使用して、軸とカラーバー用の分割器を作成します。

```python
def demo_images_side_by_side(ax):
    from mpl_toolkits.axes_grid1 import make_axes_locatable

    divider = make_axes_locatable(ax)

    Z, extent = get_demo_image()
    ax2 = divider.append_axes("right", size="100%", pad=0.05)
    fig1 = ax.get_figure()
    fig1.add_axes(ax2)

    ax.imshow(Z, extent=extent)
    ax2.imshow(Z, extent=extent)
    ax2.yaxis.set_tick_params(labelleft=False)
```
