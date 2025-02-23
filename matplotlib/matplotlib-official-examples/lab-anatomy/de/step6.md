# Die Figur annotieren

Schließlich werden wir die Figur annotieren, um die Namen verschiedener Matplotlib-Elemente anzuzeigen, indem wir die Methoden `text()` und `Circle()` verwenden. Wir werden auch die Methode `withStroke()` verwenden, um einem Text und Markern einen weißen Umriss hinzuzufügen, um eine bessere Sichtbarkeit zu gewährleisten.

```python
# Annotate the figure
from matplotlib.patches import Circle
from matplotlib.patheffects import withStroke

royal_blue = [0, 20/256, 82/256]

def annotate(x, y, text, code):
    # Kreismarker
    c = Circle((x, y), radius=0.15, clip_on=False, zorder=10, linewidth=2.5,
               edgecolor=royal_blue + [0.6], facecolor='none',
               path_effects=[withStroke(linewidth=7, foreground='white')])
    ax.add_artist(c)

    # Verwenden Sie path_effects als Hintergrund für die Texte
    # Zeichnen Sie die path_effects und den farbigen Text separat, damit die
    # path_effects andere Texte nicht abschneiden können
    for path_effects in [[withStroke(linewidth=7, foreground='white')], []]:
        color = 'white' if path_effects else royal_blue
        ax.text(x, y-0.2, text, zorder=100,
                ha='center', va='top', weight='bold', color=color,
                style='italic', fontfamily='Courier New',
                path_effects=path_effects)

        color = 'white' if path_effects else 'black'
        ax.text(x, y-0.33, code, zorder=100,
                ha='center', va='top', weight='normal', color=color,
                fontfamily='monospace', fontsize='medium',
                path_effects=path_effects)

annotate(3.5, -0.13, "Kleine Strichebezeichnung", "ax.xaxis.set_minor_formatter")
annotate(-0.03, 1.0, "Große Striche", "ax.yaxis.set_major_locator")
annotate(0.00, 3.75, "Kleine Striche", "ax.yaxis.set_minor_locator")
annotate(-0.15, 3.00, "Große Strichebezeichnung", "ax.yaxis.set_major_formatter")
annotate(1.68, -0.39, "x-Beschriftung", "ax.set_xlabel")
annotate(-0.38, 1.67, "y-Beschriftung", "ax.set_ylabel")
annotate(1.52, 4.15, "Titel", "ax.set_title")
annotate(1.75, 2.80, "Linie", "ax.plot")
annotate(2.25, 1.54, "Marker", "ax.scatter")
annotate(3.00, 3.00, "Raster", "ax.grid")
annotate(3.60, 3.58, "Legende", "ax.legend")
annotate(2.5, 0.55, "Achsen", "fig.subplots")
annotate(4, 4.5, "Figur", "plt.figure")
annotate(0.65, 0.01, "x-Achse", "ax.xaxis")
annotate(0, 0.36, "y-Achse", "ax.yaxis")
annotate(4.0, 0.7, "Rahmen", "ax.spines")
```
