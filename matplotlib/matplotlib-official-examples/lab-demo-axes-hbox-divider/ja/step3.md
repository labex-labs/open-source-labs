# `HBoxDivider` を使ってサブプロットを作成する

`HBoxDivider` クラスを使って横並びに 2 つのサブプロットを作成します。また、アスペクト比を維持したまま、軸の高さが等しくなるように軸の位置を調整します。

```python
fig, (ax1, ax2) = plt.subplots(1, 2)
ax1.imshow(arr1)
ax2.imshow(arr2)

pad = 0.5  # pad in inches
divider = HBoxDivider(
    fig, 111,
    horizontal=[Size.AxesX(ax1), Size.Fixed(pad), Size.AxesX(ax2)],
    vertical=[Size.AxesY(ax1), Size.Scaled(1), Size.AxesY(ax2)])
ax1.set_axes_locator(divider.new_locator(0))
ax2.set_axes_locator(divider.new_locator(2))

plt.show()
```
