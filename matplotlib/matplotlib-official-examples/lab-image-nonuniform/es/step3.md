# Crear subtramas y NonUniformImage

Ahora, creamos subtramas y agregamos la NonUniformImage a cada una de ellas. Crearemos cuatro subtramas, dos con interpolación 'nearest' y dos con interpolación 'bilinear'. El argumento de palabras clave de interpolación define el tipo de interpolación utilizado para mostrar la imagen.

```python
# Crear subtramas
fig, axs = plt.subplots(nrows=2, ncols=2, layout='constrained')
fig.suptitle('NonUniformImage class', fontsize='large')

# Interpolación Nearest
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

# Interpolación Bilinear
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
