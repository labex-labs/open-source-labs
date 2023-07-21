# Create an Ellipse

Next, you need to create an ellipse using the `Ellipse` class. You can specify the center of the ellipse, the width and height of the ellipse, and the angle of rotation.

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
