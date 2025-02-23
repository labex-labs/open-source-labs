# Definir formas

Definiremos las formas que queremos dibujar utilizando Matplotlib. En este ejemplo, dibujaremos un círculo, un rectángulo, un segmento circular, un polígono regular, una elipse, una flecha, un recuadro de camino y un recuadro decorado.

```python
shapes = [
    mpatches.Circle((0, 0), 0.1, ec="none"),
    mpatches.Rectangle((-0.025, -0.05), 0.05, 0.1, ec="none"),
    mpatches.Wedge((0, 0), 0.1, 30, 270, ec="none"),
    mpatches.RegularPolygon((0, 0), 5, radius=0.1),
    mpatches.Ellipse((0, 0), 0.2, 0.1),
    mpatches.Arrow(-0.05, -0.05, 0.1, 0.1, width=0.1),
    mpatches.PathPatch(mpath.Path([(0, 0), (0.5, 0.5), (1, 0)], [1, 2, 2]), ec="none"),
    mpatches.FancyBboxPatch((-0.025, -0.05), 0.05, 0.1, ec="none",
                            boxstyle=mpatches.BoxStyle("Round", pad=0.02)),
]
```
