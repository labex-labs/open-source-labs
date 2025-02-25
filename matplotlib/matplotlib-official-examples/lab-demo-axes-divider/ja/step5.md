# 描画時の位置指定による画像とカラーバー - 簡単な方法

このステップでは、描画時の位置指定により画像とそのカラーバーを簡単な方法で作成します。`mpl_toolkits.axes_grid1` から `make_axes_locatable` を使用して、軸とカラーバー用の分割器を作成します。

```python
def demo_locatable_axes_easy(ax):
    from mpl_toolkits.axes_grid1 import make_axes_locatable

    divider = make_axes_locatable(ax)

    ax_cb = divider.append_axes("right", size="5%", pad=0.05)
    fig = ax.get_figure()
    fig.add_axes(ax_cb)

    Z, extent = get_demo_image()
    im = ax.imshow(Z, extent=extent)

    plt.colorbar(im, cax=ax_cb)
    ax_cb.yaxis.tick_right()
    ax_cb.yaxis.set_tick_params(labelright=False)
```
