# Crear la gráfica

Ahora crearemos la gráfica utilizando Matplotlib agregando dos objetos `PathPatch` a la gráfica. Uno será una forma rellena de naranja, mientras que el otro será un contorno blanco.

```python
# Establecer los límites de la gráfica
xmin, ymin = verts.min(axis=0) - 1
xmax, ymax = verts.max(axis=0) + 1

# Crear la gráfica
fig = plt.figure(figsize=(5, 5), facecolor="0.75")  # fondo gris
ax = fig.add_axes([0, 0, 1, 1], frameon=False, aspect=1,
                  xlim=(xmin, xmax),  # centrar
                  ylim=(ymax, ymin),  # centrar, vuelta al revés
                  xticks=[], yticks=[])  # sin marcas de graduación

# Agregar el contorno blanco
ax.add_patch(patches.PathPatch(path, facecolor='none', edgecolor='w', lw=6))

# Agregar la forma de naranja
ax.add_patch(patches.PathPatch(path, facecolor='orange', edgecolor='k', lw=2))

# Mostrar la gráfica
plt.show()
```
