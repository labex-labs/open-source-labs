# Definir Formas

Definiremos as formas que queremos desenhar usando Matplotlib. Neste exemplo, desenharemos um círculo, um retângulo, uma cunha (wedge), um polígono regular, uma elipse, uma seta, um path patch e um fancy box patch.

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
