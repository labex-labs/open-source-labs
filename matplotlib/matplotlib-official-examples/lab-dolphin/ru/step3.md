# Поворот формы дельфина

Мы будем вращать форму дельфина на 60 градусов с использованием функции `Affine2D().rotate_deg()`.

```python
from matplotlib.transforms import Affine2D

вершины = Affine2D().rotate_deg(60).transform(вершины)
путь_дельфина2 = Path(вершины, коды)
патч_дельфина2 = PathPatch(путь_дельфина2, facecolor=(0.5, 0.5, 0.5),
                           edgecolor=(0.0, 0.0, 0.0))
ax.add_patch(патч_дельфина2)
```
