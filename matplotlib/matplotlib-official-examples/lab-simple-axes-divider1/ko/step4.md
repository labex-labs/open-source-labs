# 크기 조절 가능한 크기와 고정된 패딩을 가진 사용자 정의 축 그리드 생성

크기 조절 가능한 크기와 고정된 패딩을 가진 또 다른 사용자 정의 축 그리드를 생성합니다. `Size.Scaled()` 옵션을 사용하여 그림 크기에 따라 크기가 조절되는 축 크기를 지정합니다. 나머지 단계는 이전 예제와 유사합니다.

```python
# Sizes are in inches.
horiz = [Size.Scaled(1.5), Size.Fixed(.5), Size.Scaled(1.), Size.Scaled(.5)]
vert = [Size.Scaled(1.), Size.Fixed(.5), Size.Scaled(1.5)]

rect = (0.1, 0.1, 0.8, 0.8)
fig = plt.figure(figsize=(6, 6))
fig.suptitle("Scalable axes sizes, fixed paddings")

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
