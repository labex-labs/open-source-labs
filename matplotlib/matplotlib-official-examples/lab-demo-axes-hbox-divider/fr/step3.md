# Création de sous-graphiques à l'aide de `HBoxDivider`

Nous créons deux sous-graphiques côte à côte en utilisant la classe `HBoxDivider`. Nous ajustons également l'emplacement des axes pour qu'ils aient des hauteurs égales tout en conservant leurs rapports d'aspect.

```python
fig, (ax1, ax2) = plt.subplots(1, 2)
ax1.imshow(arr1)
ax2.imshow(arr2)

pad = 0.5  # espacement en pouces
divider = HBoxDivider(
    fig, 111,
    horizontal=[Size.AxesX(ax1), Size.Fixed(pad), Size.AxesX(ax2)],
    vertical=[Size.AxesY(ax1), Size.Scaled(1), Size.AxesY(ax2)])
ax1.set_axes_locator(divider.new_locator(0))
ax2.set_axes_locator(divider.new_locator(2))

plt.show()
```
