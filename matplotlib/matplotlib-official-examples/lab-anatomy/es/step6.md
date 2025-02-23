# Anotar la figura

Finalmente, anotaremos la figura para mostrar los nombres de varios elementos de Matplotlib usando los métodos `text()` y `Circle()`. También usaremos el método `withStroke()` para agregar un contorno blanco al texto y a los marcadores para una mejor visibilidad.

```python
# Anotar la figura
from matplotlib.patches import Circle
from matplotlib.patheffects import withStroke

royal_blue = [0, 20/256, 82/256]

def annotate(x, y, text, code):
    # Marcador de círculo
    c = Circle((x, y), radio=0.15, clip_on=False, zorder=10, linewidth=2.5,
               edgecolor=royal_blue + [0.6], facecolor='none',
               path_effects=[withStroke(linewidth=7, foreground='white')])
    ax.add_artist(c)

    # use path_effects como un fondo para los textos
    # dibuja los path_effects y el texto coloreado por separado para que los
    # path_effects no puedan recortar otros textos
    for path_effects in [[withStroke(linewidth=7, foreground='white')], []]:
        color = 'white' si path_effects else royal_blue
        ax.text(x, y-0.2, text, zorder=100,
                ha='center', va='top', weight='bold', color=color,
                style='italic', fontfamily='Courier New',
                path_effects=path_effects)

        color = 'white' si path_effects else 'black'
        ax.text(x, y-0.33, code, zorder=100,
                ha='center', va='top', weight='normal', color=color,
                fontfamily='monospace', fontsize='medium',
                path_effects=path_effects)

annotate(3.5, -0.13, "Etiqueta de submarcador", "ax.xaxis.set_minor_formatter")
annotate(-0.03, 1.0, "Marcador principal", "ax.yaxis.set_major_locator")
annotate(0.00, 3.75, "Submarcador", "ax.yaxis.set_minor_locator")
annotate(-0.15, 3.00, "Etiqueta de marcador principal", "ax.yaxis.set_major_formatter")
annotate(1.68, -0.39, "Etiqueta del eje x", "ax.set_xlabel")
annotate(-0.38, 1.67, "Etiqueta del eje y", "ax.set_ylabel")
annotate(1.52, 4.15, "Título", "ax.set_title")
annotate(1.75, 2.80, "Línea", "ax.plot")
annotate(2.25, 1.54, "Marcadores", "ax.scatter")
annotate(3.00, 3.00, "Cuadrícula", "ax.grid")
annotate(3.60, 3.58, "Leyenda", "ax.legend")
annotate(2.5, 0.55, "Ejes", "fig.subplots")
annotate(4, 4.5, "Figura", "plt.figure")
annotate(0.65, 0.01, "Eje x", "ax.xaxis")
annotate(0, 0.36, "Eje y", "ax.yaxis")
annotate(4.0, 0.7, "Espina", "ax.spines")
```

**Nota**: En el código original, los nombres de los atributos y métodos de Matplotlib se mantienen en inglés para una consistencia técnica. En la traducción, se han mantenido en inglés donde era necesario para evitar confusiones en el contexto de la programación. Además, se han corregido algunos términos en la traducción para que tengan un mejor sentido en español, como "submarcador" en lugar de "minor tick" y "marcador principal" en lugar de "major tick".
