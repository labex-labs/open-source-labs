# Création de sous-graphiques à l'aide de `VBoxDivider`

Nous créons deux sous-graphiques l'un en-dessous de l'autre en utilisant la classe `VBoxDivider`. Nous ajustons l'emplacement des axes pour qu'ils aient des largeurs égales tout en conservant leurs rapports d'aspect.

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
