# TextArea 로 주석 달기

이제 TextArea 를 사용하여 첫 번째 점에 주석을 달아 보겠습니다.

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
