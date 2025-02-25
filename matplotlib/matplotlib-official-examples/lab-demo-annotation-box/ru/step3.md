# Аннотация с использованием DrawingArea

Далее давайте добавим аннотацию ко второй точке в виде круга с использованием DrawingArea.

```python
from matplotlib.offsetbox import DrawingArea
from matplotlib.patches import Circle

# Добавим аннотацию ко второй позиции в виде круга
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
