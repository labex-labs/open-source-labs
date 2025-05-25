# 그리기 시점 위치 지정으로 이미지와 컬러바 - 쉬운 방법

이 단계에서는 쉬운 방법으로 그리기 시점 위치 지정을 사용하여 이미지와 해당 컬러바를 생성합니다. 축과 컬러바에 대한 분할자를 생성하기 위해 `mpl_toolkits.axes_grid1`의 `make_axes_locatable`을 사용합니다.

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
