# Erstellen eines benutzerdefinierten Achsennetzes mit fester Größe und Abstand

Wir werden ein benutzerdefiniertes Achsennetz mit fester Größe und Abstand erstellen. Wir werden die `Divider`-Klasse verwenden, um das Achsenrechteck in ein Netz mit Größen zu teilen, die durch `horiz * vert` angegeben werden. Anschließend werden wir vier Achsen zur Figur hinzufügen, indem wir die `add_axes()`-Methode verwenden und die Positionen jeder Achse mithilfe der `new_locator()`-Methode der `Divider`-Klasse angeben.

```python
# Sizes are in inches.
horiz = [Size.Fixed(1.), Size.Fixed(.5), Size.Fixed(1.5), Size.Fixed(.5)]
vert = [Size.Fixed(1.5), Size.Fixed(.5), Size.Fixed(1.)]

rect = (0.1, 0.1, 0.8, 0.8)
fig = plt.figure(figsize=(6, 6))
fig.suptitle("Fixed axes sizes, fixed paddings")

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
