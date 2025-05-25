# RGBAxes 플롯 생성

이 단계에서는 `RGBAxes` 클래스를 사용하여 RGBAxes 플롯을 생성합니다. `RGBAxes` 객체의 `imshow_rgb()` 메서드를 사용하여 RGB 이미지를 표시합니다.

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
