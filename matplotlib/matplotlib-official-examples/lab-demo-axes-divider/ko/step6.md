# 고정 패딩을 사용한 나란히 두 이미지

이 단계에서는 고정 패딩을 사용하여 나란히 두 개의 이미지를 생성합니다. 축과 컬러바에 대한 분할자를 생성하기 위해 `mpl_toolkits.axes_grid1`의 `make_axes_locatable`을 사용합니다.

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
