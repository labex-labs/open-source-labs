# Definir función

Ahora, definiremos una función llamada `survey` que toma los `results` y `category_names` y crea una visualización de un diagrama de barras apiladas horizontales.

```python
def survey(results, category_names):
    """
    Parámetros
    ----------
    results : dict
        Un mapeo de etiquetas de pregunta a una lista de respuestas por categoría.
        Se asume que todas las listas contienen la misma cantidad de entradas y que
        coincide con la longitud de *category_names*.
    category_names : lista de str
        Las etiquetas de categoría.
    """
    # Convertir los resultados y las categorías a arrays de numpy
    labels = list(results.keys())
    data = np.array(list(results.values()))

    # Calcular las sumas acumuladas de los datos para el apilamiento horizontal
    data_cum = data.cumsum(axis=1)

    # Definir los colores de las categorías
    category_colors = plt.colormaps['RdYlGn'](
        np.linspace(0.15, 0.85, data.shape[1]))

    # Crear la gráfica y configurar las propiedades de los ejes
    fig, ax = plt.subplots(figsize=(9.2, 5))
    ax.invert_yaxis()
    ax.xaxis.set_visible(False)
    ax.set_xlim(0, np.sum(data, axis=1).max())

    # Crear las barras apiladas y agregar etiquetas a las barras
    for i, (colname, color) in enumerate(zip(category_names, category_colors)):
        widths = data[:, i]
        starts = data_cum[:, i] - widths
        rects = ax.barh(labels, widths, left=starts, height=0.5,
                        label=colname, color=color)
        r, g, b, _ = color
        text_color = 'white' if r * g * b < 0.5 else 'darkgrey'
        ax.bar_label(rects, label_type='center', color=text_color)

    # Agregar leyenda
    ax.legend(ncols=len(category_names), bbox_to_anchor=(0, 1),
              loc='lower left', fontsize='small')

    return fig, ax
```
