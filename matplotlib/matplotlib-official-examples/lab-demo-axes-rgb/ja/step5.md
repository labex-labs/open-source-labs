# 個別のチャネルを持つ RGBAxes プロットを作成する

このステップでは、`make_rgb_axes()`関数を使って個別のチャネルを持つ RGBAxes プロットを作成します。`Axes`オブジェクトの`imshow()`メソッドを使って R、G、B チャネルを表示します。

```python
def demo_rgb2():
    # Create a figure and an Axes object
    fig, ax = plt.subplots()

    # Create the R, G, and B Axes objects using the make_rgb_axes() function
    ax_r, ax_g, ax_b = make_rgb_axes(ax, pad=0.02)

    # Get the R, G, and B channels and create the RGB cube
    r, g, b = get_rgb()
    im_r, im_g, im_b, im_rgb = make_cube(r, g, b)

    # Display the RGB image and the R, G, and B channels
    ax.imshow(im_rgb)
    ax_r.imshow(im_r)
    ax_g.imshow(im_g)
    ax_b.imshow(im_b)

    # Set the tick parameters and spine colors for all Axes objects
    for ax in fig.axes:
        ax.tick_params(direction='in', color='w')
        ax.spines[:].set_color("w")
```
