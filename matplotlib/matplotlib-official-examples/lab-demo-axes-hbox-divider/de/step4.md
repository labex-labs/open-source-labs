# Subplots mit `VBoxDivider` erstellen

Wir erstellen zwei übereinander liegende Subplots mit der Klasse `VBoxDivider`. Wir passen die Position der Achsen an, sodass sie gleich breite Höhen haben, während ihre Seitenverhältnisse beibehalten werden.

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
