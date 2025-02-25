# Annoter avec TextArea

Maintenant, annotons le premier point à l'aide d'un TextArea.

```python
from matplotlib.offsetbox import AnnotationBbox, TextArea

# Annoter la première position avec une boîte de texte ('Test 1')
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
