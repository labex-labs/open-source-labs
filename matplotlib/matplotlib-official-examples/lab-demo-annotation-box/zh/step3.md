# 使用 DrawingArea 进行注释

接下来，让我们使用 DrawingArea 用一个圆形补丁为第二个点添加注释。

```python
from matplotlib.offsetbox import DrawingArea
from matplotlib.patches import Circle

# 用一个圆形补丁为第二个位置添加注释
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
