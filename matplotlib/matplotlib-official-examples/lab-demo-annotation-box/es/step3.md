# Anotando con DrawingArea

A continuación, vamos a anotar el segundo punto con un parche circular usando DrawingArea.

```python
from matplotlib.offsetbox import DrawingArea
from matplotlib.patches import Circle

# Anota la 2ª posición con un parche circular
da = DrawingArea(20, 20, 0, 0)
p = Circle((10, 10), 10)
da.add_artist(p)

ab = AnnotationBbox(da, xy2,
                    xybox=(1., xy2[1]),
                    xycoords='data',
                    boxcoords=("axes fraction", "data"),
                    box_alignment=(0.2, 0.5),
                    arrowprops=dict(arrowstyle="->"),
                    bboxprops=dict(alpha=0.5))

ax.add_artist(ab)

plt.show()
```
