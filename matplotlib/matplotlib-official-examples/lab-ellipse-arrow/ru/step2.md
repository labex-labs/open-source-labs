# Создаем эллипс

Далее вам нужно создать эллипс с использованием класса `Ellipse`. Вы можете указать центр эллипса, ширину и высоту эллипса, а также угол вращения.

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
