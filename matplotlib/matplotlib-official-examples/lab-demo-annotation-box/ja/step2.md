# TextArea で注釈を付ける

次に、TextArea を使って最初の点に注釈を付けましょう。

```python
from matplotlib.offsetbox import AnnotationBbox, TextArea

# 1 番目の位置にテキストボックス ('Test 1') で注釈を付ける
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
