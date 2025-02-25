# 楕円を作成する

次に、`Ellipse` クラスを使って楕円を作成する必要があります。楕円の中心、幅と高さ、回転角度を指定することができます。

```python
from matplotlib.patches import Ellipse

ellipse = Ellipse(
    xy=(2, 4),
    width=30,
    height=20,
    angle=35,
    facecolor="none",
    edgecolor="b"
)
ax.add_patch(ellipse)
```
