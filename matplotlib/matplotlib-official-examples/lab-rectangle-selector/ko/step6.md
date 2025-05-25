# RectangleSelector 및 EllipseSelector 위젯 생성

RectangleSelector 및 EllipseSelector 위젯을 생성하고 이를 서브플롯에 추가합니다.

```python
selectors = []
for ax, selector_class in zip(axs, [RectangleSelector, EllipseSelector]):
    ax.set_title(f"Click and drag to draw a {selector_class.__name__}.")
    selectors.append(selector_class(
        ax, select_callback,
        useblit=True,
        button=[1, 3],  # disable middle button
        minspanx=5, minspany=5,
        spancoords='pixels',
        interactive=True))
    fig.canvas.mpl_connect('key_press_event', toggle_selector)
axs[0].set_title("Press 't' to toggle the selectors on and off.\n"
                 + axs[0].get_title())
```
