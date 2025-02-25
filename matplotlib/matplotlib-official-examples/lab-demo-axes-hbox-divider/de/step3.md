# Subplots mit `HBoxDivider` erstellen

Wir erstellen zwei nebeneinander liegende Subplots mit der Klasse `HBoxDivider`. Wir passen auch die Position der Achsen an, sodass sie gleich hohe Breiten haben, während ihre Seitenverhältnisse beibehalten werden.

```python
fig, (ax1, ax2) = plt.subplots(1, 2)
ax1.imshow(arr1)
ax2.imshow(arr2)

pad = 0.5  # Abstand in Zoll
divider = HBoxDivider(
    fig, 111,
    horizontal=[Size.AxesX(ax1), Size.Fixed(pad), Size.AxesX(ax2)],
    vertical=[Size.AxesY(ax1), Size.Scaled(1), Size.AxesY(ax2)])
ax1.set_axes_locator(divider.new_locator(0))
ax2.set_axes_locator(divider.new_locator(2))

plt.show()
```
