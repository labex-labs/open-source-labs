# RGBAxes プロットを作成する

このステップでは、`RGBAxes`クラスを使って RGBAxes プロットを作成します。`RGBAxes`オブジェクトの`imshow_rgb()`メソッドを使って RGB 画像を表示します。

```python
def demo_rgb1():
    # Create a figure and a RGBAxes object
    fig = plt.figure()
    ax = RGBAxes(fig, [0.1, 0.1, 0.8, 0.8], pad=0.0)

    # Get the R, G, and B channels
    r, g, b = get_rgb()

    # Display the RGB image using the imshow_rgb() method
    ax.imshow_rgb(r, g, b)
```
