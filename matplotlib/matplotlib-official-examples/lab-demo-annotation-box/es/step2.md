# Anotando con TextArea

Ahora vamos a anotar el primer punto usando un TextArea.

```python
from matplotlib.offsetbox import AnnotationBbox, TextArea

# Anota la 1ª posición con un cuadro de texto ('Test 1')
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
