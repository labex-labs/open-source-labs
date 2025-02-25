# 描画時の位置指定による画像とカラーバー - 難しい方法

このステップでは、描画時の位置指定により画像とそのカラーバーを作成します。これは難しい方法で行います。`mpl_toolkits.axes_grid1` から `SubplotDivider` を使用して、軸とカラーバー用の分割器を作成します。

```python
def demo_locatable_axes_hard(fig):
    from mpl_toolkits.axes_grid1 import Size, SubplotDivider

    divider = SubplotDivider(fig, 2, 2, 2, aspect=True)

    # 画像用の軸
    ax = fig.add_subplot(axes_locator=divider.new_locator(nx=0, ny=0))
    # カラーバー用の軸
    ax_cb = fig.add_subplot(axes_locator=divider.new_locator(nx=2, ny=0))

    divider.set_horizontal([
        Size.AxesX(ax),  # メイン軸
        Size.Fixed(0.05),  # パディング, 0.1インチ
        Size.Fixed(0.2),  # カラーバー, 0.3インチ
    ])
    divider.set_vertical([Size.AxesY(ax)])

    Z, extent = get_demo_image()

    im = ax.imshow(Z, extent=extent)
    plt.colorbar(im, cax=ax_cb)
    ax_cb.yaxis.set_tick_params(labelright=False)
```
