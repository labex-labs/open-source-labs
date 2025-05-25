# 그리기 시점 위치 지정으로 이미지와 컬러바 - 어려운 방법

이 단계에서는 어려운 방법으로 그리기 시점 위치 지정을 사용하여 이미지와 해당 컬러바를 생성합니다. 축과 컬러바에 대한 분할자를 생성하기 위해 `mpl_toolkits.axes_grid1`의 `SubplotDivider`를 사용합니다.

```python
def demo_locatable_axes_hard(fig):
    from mpl_toolkits.axes_grid1 import Size, SubplotDivider

    divider = SubplotDivider(fig, 2, 2, 2, aspect=True)

    # axes for image
    ax = fig.add_subplot(axes_locator=divider.new_locator(nx=0, ny=0))
    # axes for colorbar
    ax_cb = fig.add_subplot(axes_locator=divider.new_locator(nx=2, ny=0))

    divider.set_horizontal([
        Size.AxesX(ax),  # main axes
        Size.Fixed(0.05),  # padding, 0.1 inch
        Size.Fixed(0.2),  # colorbar, 0.3 inch
    ])
    divider.set_vertical([Size.AxesY(ax)])

    Z, extent = get_demo_image()

    im = ax.imshow(Z, extent=extent)
    plt.colorbar(im, cax=ax_cb)
    ax_cb.yaxis.set_tick_params(labelright=False)
```
