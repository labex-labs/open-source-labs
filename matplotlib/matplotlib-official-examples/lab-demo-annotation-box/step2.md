# Annotating with TextArea

Now let's annotate the first point using a TextArea.

```python
from matplotlib.offsetbox import AnnotationBbox, TextArea

# Annotate the 1st position with a text box ('Test 1')
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
