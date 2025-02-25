# Создайте заштрихованную область

Создайте заштрихованную область с использованием участка `Polygon`. Сгенерируйте значения x и y для области с использованием `linspace` и функции, определенной на шаге 1. Затем определите вершины области в виде списка кортежей. Наконец, создайте объект `Polygon` и добавьте его к оси с использованием `add_patch`.

```python
from matplotlib.patches import Polygon

ix = np.linspace(a, b)
iy = func(ix)
verts = [(a, 0), *zip(ix, iy), (b, 0)]
poly = Polygon(verts, facecolor='0.9', edgecolor='0.5')
ax.add_patch(poly)
```
