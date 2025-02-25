# `VBoxDivider` を使ってサブプロットを作成する

`VBoxDivider` クラスを使って上下に 2 つのサブプロットを作成します。また、アスペクト比を維持したまま、軸の幅が等しくなるように軸の位置を調整します。

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
