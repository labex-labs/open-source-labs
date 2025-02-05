# 使用TextArea进行注释

现在让我们使用TextArea为第一个点添加注释。

```python
from matplotlib.offsetbox import AnnotationBbox, TextArea

# 使用文本框（“Test 1”）为第一个位置添加注释
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
