# Subplots und NonUniformImage erstellen

Jetzt erstellen wir Subplots und fügen das NonUniformImage zu jedem von ihnen hinzu. Wir werden vier Subplots erstellen, zwei mit 'nearest'-Interpolation und zwei mit 'bilinear'-Interpolation. Das Schlüsselwortargument interpolation definiert den Typ der Interpolation, die zum Anzeigen des Bilds verwendet wird.

```python
# Subplots erstellen
fig, axs = plt.subplots(nrows=2, ncols=2, layout='constrained')
fig.suptitle('NonUniformImage class', fontsize='large')

# Nearest-Interpolation
ax = axs[0, 0]
im = NonUniformImage(ax, interpolation='nearest', extent=(-4, 4, -4, 4), cmap=cm.Purples)
im.set_data(x, y, z)
ax.add_image(im)
ax.set_xlim(-4, 4)
ax.set_ylim(-4, 4)
ax.set_title('nearest')

ax = axs[0, 1]
im = NonUniformImage(ax, interpolation='nearest', extent=(-64, 64, -4, 4), cmap=cm.Purples)
im.set_data(x2, y, z)
ax.add_image(im)
ax.set_xlim(-64, 64)
ax.set_ylim(-4, 4)
ax.set_title('nearest')

# Bilinear-Interpolation
ax = axs[1, 0]
im = NonUniformImage(ax, interpolation='bilinear', extent=(-4, 4, -4, 4), cmap=cm.Purples)
im.set_data(x, y, z)
ax.add_image(im)
ax.set_xlim(-4, 4)
ax.set_ylim(-4, 4)
ax.set_title('bilinear')

ax = axs[1, 1]
im = NonUniformImage(ax, interpolation='bilinear', extent=(-64, 64, -4, 4), cmap=cm.Purples)
im.set_data(x2, y, z)
ax.add_image(im)
ax.set_xlim(-64, 64)
ax.set_ylim(-4, 4)
ax.set_title('bilinear')

plt.show()
```
