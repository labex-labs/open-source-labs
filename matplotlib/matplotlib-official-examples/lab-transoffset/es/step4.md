# Agregar texto al diagrama de dispersión

Ahora agregaremos texto a nuestro diagrama de dispersión usando `offset_copy`. Primero crearemos una transformación que posicione el texto con un desplazamiento especificado en coordenadas de pantalla con respecto a una ubicación dada en cualquier coordenada. Luego, usaremos la función `text` de `matplotlib.pyplot` para agregar el texto al gráfico.

```python
# Create the transform
trans_offset = mtransforms.offset_copy(ax.transData, fig=fig,
                                       x=0.05, y=0.10, units='inches')

# Add text to the plot
for x, y in zip(xs, ys):
    plt.text(x, y, '%d, %d' % (int(x), int(y)), transform=trans_offset)
```
