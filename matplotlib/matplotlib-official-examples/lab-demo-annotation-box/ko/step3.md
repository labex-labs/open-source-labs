# DrawingArea 로 주석 달기

다음으로, DrawingArea 를 사용하여 두 번째 점에 원 패치를 사용하여 주석을 달아 보겠습니다.

```python
from matplotlib.offsetbox import DrawingArea
from matplotlib.patches import Circle

# Annotate the 2nd position with a circle patch
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
