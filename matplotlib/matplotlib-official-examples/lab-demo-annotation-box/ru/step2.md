# Аннотация с использованием TextArea

Теперь давайте добавим аннотацию к первой точке с использованием TextArea.

```python
from matplotlib.offsetbox import AnnotationBbox, TextArea

# Добавим аннотацию к первой позиции в виде текстового поля ('Test 1')
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
