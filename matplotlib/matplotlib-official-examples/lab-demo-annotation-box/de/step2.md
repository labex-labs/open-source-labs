# Annotation mit TextArea

Annotieren wir nun den ersten Punkt mit einem TextArea.

```python
from matplotlib.offsetbox import AnnotationBbox, TextArea

# Annotiere die erste Position mit einem Textfeld ('Test 1')
offsetbox = TextArea("Test 1")

ab = AnnotationBbox(offsetbox, xy1,
                    xybox=(-20, 40),
                    xycoords='data',
                    boxcoords="offset points",
                    arrowprops=dict(arrowstyle="->"),
                    bboxprops=dict(boxstyle="sawtooth"))

ax.add_artist(ab)

plt.show()
```
