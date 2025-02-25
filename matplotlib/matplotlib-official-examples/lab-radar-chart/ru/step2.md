# Определить функцию для диаграммы радара

Далее мы определим функцию для создания диаграммы радара. Эта функция будет принимать два аргумента: `num_vars` и `frame`. `num_vars` - это количество переменных для диаграммы радара, а `frame` задает форму рамки, окружающей оси.

```python
from matplotlib.patches import Circle, RegularPolygon
from matplotlib.path import Path
from matplotlib.projections import register_projection
from matplotlib.projections.polar import PolarAxes
from matplotlib.spines import Spine
from matplotlib.transforms import Affine2D

def radar_factory(num_vars, frame='circle'):
    # код функции будет здесь
```
