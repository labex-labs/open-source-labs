# シンプルな画像とカラーバー

このステップでは、シンプルな画像とそのカラーバーを作成します。画像を作成するために `pyplot` から `imshow()` 関数を、カラーバーを作成するために `colorbar()` 関数を使用します。

```python
def demo_simple_image(ax):
    Z, extent = get_demo_image()

    im = ax.imshow(Z, extent=extent)
    cb = plt.colorbar(im)
    cb.ax.yaxis.set_tick_params(labelright=False)
```
