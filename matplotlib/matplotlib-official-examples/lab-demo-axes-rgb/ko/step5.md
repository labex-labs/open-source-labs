# 개별 채널을 가진 RGBAxes 플롯 생성

이 단계에서는 `make_rgb_axes()` 함수를 사용하여 개별 채널을 가진 RGBAxes 플롯을 생성합니다. `Axes` 객체의 `imshow()` 메서드를 사용하여 R, G, B 채널을 표시합니다.

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
