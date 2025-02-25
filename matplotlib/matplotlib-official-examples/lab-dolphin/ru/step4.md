# Завершение графика

Соберем все вместе и завершим график.

```python
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm
from matplotlib.patches import Circle, PathPatch
from matplotlib.path import Path
from matplotlib.transforms import Affine2D

# Фиксация случайного состояния для воспроизводимости
np.random.seed(19680801)

r = np.random.rand(50)
t = np.random.rand(50) * np.pi * 2.0
x = r * np.cos(t)
y = r * np.sin(t)

fig, ax = plt.subplots(figsize=(6, 6))
круг = Circle((0, 0), 1, facecolor='none',
                edgecolor=(0, 0.8, 0.8), linewidth=3, alpha=0.5)
ax.add_patch(круг)

im = plt.imshow(np.random.random((100, 100)),
                origin='lower', cmap=cm.winter,
                interpolation='spline36',
                extent=([-1, 1, -1, 1]))
im.set_clip_path(круг)

plt.plot(x, y, 'o', color=(0.9, 0.9, 1.0), alpha=0.8)

путь_дельфина = Path(вершины, коды)
патч_дельфина = PathPatch(путь_дельфина, facecolor=(0.6, 0.6, 0.6),
                          edgecolor=(0.0, 0.0, 0.0))
ax.add_patch(патч_дельфина)

вершины = Affine2D().rotate_deg(60).transform(вершины)
путь_дельфина2 = Path(вершины, коды)
патч_дельфина2 = PathPatch(путь_дельфина2, facecolor=(0.5, 0.5, 0.5),
                           edgecolor=(0.0, 0.0, 0.0))
ax.add_patch(патч_дельфина2)

plt.show()
```
