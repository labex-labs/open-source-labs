# Crear subtramas usando `HBoxDivider`

Creamos dos subtramas lado a lado utilizando la clase `HBoxDivider`. También ajustamos la ubicación de los ejes para que tengan la misma altura mientras mantienen sus proporciones de aspecto.

```python
fig, (ax1, ax2) = plt.subplots(1, 2)
ax1.imshow(arr1)
ax2.imshow(arr2)

pad = 0.5  # pad en pulgadas
divider = HBoxDivider(
    fig, 111,
    horizontal=[Size.AxesX(ax1), Size.Fixed(pad), Size.AxesX(ax2)],
    vertical=[Size.AxesY(ax1), Size.Scaled(1), Size.AxesY(ax2)])
ax1.set_axes_locator(divider.new_locator(0))
ax2.set_axes_locator(divider.new_locator(2))

plt.show()
```
