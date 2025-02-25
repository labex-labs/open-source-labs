# Crear una imagen con un zoom en el recuadro insertado y un recuadro insertado marcado

En la segunda subtrama, crearemos una imagen con un zoom en el recuadro insertado y un recuadro insertado marcado. Esto mostrará cómo usar el método `.mark_inset` para marcar la región de interés y conectarla con los ejes del recuadro insertado.

```python
# Carga los datos de muestra para la imagen
Z = cbook.get_sample_data("axes_grid/bivariate_normal.npy")  # matriz 15x15
extent = (-3, 4, -4, 3)
Z2 = np.zeros((150, 150))
ny, nx = Z.shape
Z2[30:30+ny, 30:30+nx] = Z

# Muestra la imagen en la subtrama
ax2.imshow(Z2, extent=extent, origin="lower")

# Crea un recuadro insertado con zoom en la esquina superior izquierda del gráfico
axins2 = zoomed_inset_axes(ax2, zoom=6, loc=1)

# Muestra la imagen en el gráfico del recuadro insertado
axins2.imshow(Z2, extent=extent, origin="lower")

# Establece los límites x e y del gráfico del recuadro insertado para mostrar la región de interés
x1, x2, y1, y2 = -1.5, -0.9, -2.5, -1.9
axins2.set_xlim(x1, x2)
axins2.set_ylim(y1, y2)

# Establece el número de marcas de graduación en los ejes del recuadro insertado
axins2.yaxis.get_major_locator().set_params(nbins=7)
axins2.xaxis.get_major_locator().set_params(nbins=7)

# Oculta las etiquetas de las marcas de graduación en los ejes del recuadro insertado
axins2.tick_params(labelleft=False, labelbottom=False)

# Marca la región de interés y la conecta con los ejes del recuadro insertado
mark_inset(ax2, axins2, loc1=2, loc2=4, fc="none", ec="0.5")
```
