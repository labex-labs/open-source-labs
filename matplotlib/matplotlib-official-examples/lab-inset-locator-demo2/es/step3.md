# Crear un recuadro insertado con zoom con una barra de escala

En la primera subtrama, crearemos un recuadro insertado con zoom con una barra de escala. Esto mostrará cómo usar el método `.zoomed_inset_axes` para crear un recuadro insertado con zoom.

```python
# Establece la relación de aspecto del gráfico en 1
ax.set_aspect(1)

# Crea un recuadro insertado con zoom en la esquina superior derecha del gráfico
axins = zoomed_inset_axes(ax, zoom=0.5, loc='upper right')

# Establece el número de marcas de graduación en los ejes del recuadro insertado
axins.yaxis.get_major_locator().set_params(nbins=7)
axins.xaxis.get_major_locator().set_params(nbins=7)

# Oculta las etiquetas de las marcas de graduación en los ejes del recuadro insertado
axins.tick_params(labelleft=False, labelbottom=False)

# Define una función para agregar una barra de escala al gráfico
def add_sizebar(ax, size):
    asb = AnchoredSizeBar(ax.transData,
                          size,
                          str(size),
                          loc=8,
                          pad=0.1, borderpad=0.5, sep=5,
                          frameon=False)
    ax.add_artist(asb)

# Agrega una barra de escala al gráfico principal y al gráfico del recuadro insertado
add_sizebar(ax, 0.5)
add_sizebar(axins, 0.5)
```
