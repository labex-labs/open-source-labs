# 축 분할기 설정

`Divider` 클래스와 `mpl_toolkits.axes_grid1.axes_size` 모듈의 `AxesX` 및 `AxesY` 클래스를 사용하여 축 분할기를 설정합니다. 그런 다음 `new_locator` 메서드를 사용하여 각 축의 위치를 설정합니다.

```python
horiz = [Size.AxesX(ax[0]), Size.Fixed(.5), Size.AxesX(ax[1])]
vert = [Size.AxesY(ax[0]), Size.Fixed(.5), Size.AxesY(ax[2])]
divider = Divider(fig, rect, horiz, vert, aspect=False)

ax[0].set_axes_locator(divider.new_locator(nx=0, ny=0))
ax[1].set_axes_locator(divider.new_locator(nx=2, ny=0))
ax[2].set_axes_locator(divider.new_locator(nx=0, ny=2))
ax[3].set_axes_locator(divider.new_locator(nx=2, ny=2))
```
