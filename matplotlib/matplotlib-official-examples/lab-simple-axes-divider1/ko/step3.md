# 고정된 크기와 패딩을 가진 사용자 정의 축 그리드 생성

고정된 크기와 패딩을 가진 사용자 정의 축 그리드를 생성합니다. `Divider` 클래스를 사용하여 축 사각형을 `horiz * vert`로 지정된 크기를 가진 그리드로 나눕니다. 그런 다음 `add_axes()` 메서드를 사용하여 그림에 네 개의 축을 추가하고, `Divider` 클래스의 `new_locator()` 메서드를 사용하여 각 축의 위치를 지정합니다.

```python
# Sizes are in inches.
horiz = [Size.Fixed(1.), Size.Fixed(.5), Size.Fixed(1.5), Size.Fixed(.5)]
vert = [Size.Fixed(1.5), Size.Fixed(.5), Size.Fixed(1.)]

rect = (0.1, 0.1, 0.8, 0.8)
fig = plt.figure(figsize=(6, 6))
fig.suptitle("Fixed axes sizes, fixed paddings")

div = Divider(fig, rect, horiz, vert, aspect=False)

# The rect parameter will actually be ignored and overridden by axes_locator.
ax1 = fig.add_axes(rect, axes_locator=div.new_locator(nx=0, ny=0))
label_axes(ax1, "nx=0, ny=0")
ax2 = fig.add_axes(rect, axes_locator=div.new_locator(nx=0, ny=2))
label_axes(ax2, "nx=0, ny=2")
ax3 = fig.add_axes(rect, axes_locator=div.new_locator(nx=2, ny=2))
label_axes(ax3, "nx=2, ny=2")
ax4 = fig.add_axes(rect, axes_locator=div.new_locator(nx=2, nx1=4, ny=0))
label_axes(ax4, "nx=2, nx1=4, ny=0")

plt.show()
```
