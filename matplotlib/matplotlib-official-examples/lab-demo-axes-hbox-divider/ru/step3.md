# Создаем вложенные графики с использованием `HBoxDivider`

Создадим два вложенных графика рядом с использованием класса `HBoxDivider`. Также настроим расположение осей так, чтобы они имели одинаковую высоту, сохраняя при этом их соотношение сторон.

```python
fig, (ax1, ax2) = plt.subplots(1, 2)
ax1.imshow(arr1)
ax2.imshow(arr2)

pad = 0.5  # отступ в дюймах
divider = HBoxDivider(
    fig, 111,
    horizontal=[Size.AxesX(ax1), Size.Fixed(pad), Size.AxesX(ax2)],
    vertical=[Size.AxesY(ax1), Size.Scaled(1), Size.AxesY(ax2)])
ax1.set_axes_locator(divider.new_locator(0))
ax2.set_axes_locator(divider.new_locator(2))

plt.show()
```
