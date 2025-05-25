# `VBoxDivider`를 사용하여 서브플롯 생성

`VBoxDivider` 클래스를 사용하여 두 개의 서브플롯을 서로 아래에 생성합니다. 종횡비를 유지하면서 축의 너비가 같도록 축의 위치를 조정합니다.

```python
fig, (ax1, ax2) = plt.subplots(2, 1)
ax1.imshow(arr1)
ax2.imshow(arr2)

divider = VBoxDivider(
    fig, 111,
    horizontal=[Size.AxesX(ax1), Size.Scaled(1), Size.AxesX(ax2)],
    vertical=[Size.AxesY(ax1), Size.Fixed(pad), Size.AxesY(ax2)])

ax1.set_axes_locator(divider.new_locator(0))
ax2.set_axes_locator(divider.new_locator(2))

plt.show()
```
