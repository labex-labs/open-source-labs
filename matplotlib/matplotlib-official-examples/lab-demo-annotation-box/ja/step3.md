# DrawingArea で注釈を付ける

次に、DrawingArea を使って円形のパッチを使って 2 番目の点に注釈を付けましょう。

```python
from matplotlib.offsetbox import DrawingArea
from matplotlib.patches import Circle

# 2 番目の位置に円形のパッチで注釈を付ける
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
