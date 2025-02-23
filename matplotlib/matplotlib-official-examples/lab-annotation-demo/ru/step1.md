# Указание точек текста и точек аннотации

Чтобы добавить аннотацию к какой-либо точке, вы должны указать точку аннотации `xy=(x, y)`. Кроме того, вы можете указать точку для вставки текста `xytext=(x, y)` для этой аннотации. По желанию вы можете указать систему координат для `xy` и `xytext` с помощью одной из следующих строк для `xycoords` и `textcoords` (по умолчанию 'data'):

- 'figure points' : точки от нижнего левого угла рисунка
- 'figure pixels' : пиксели от нижнего левого угла рисунка
- 'figure fraction' : (0, 0) - нижний левый угол рисунка, (1, 1) - верхний правый
- 'axes points' : точки от нижнего левого угла осей
- 'axes pixels' : пиксели от нижнего левого угла осей
- 'axes fraction' : (0, 0) - нижний левый угол осей, (1, 1) - верхний правый
- 'offset points' : Укажите смещение (в точках) от значения xy
- 'offset pixels' : Укажите смещение (в пикселях) от значения xy
- 'data' : использовать систему координат данных осей

Примечание: для физических систем координат (точек или пикселей) начало координат находится в (нижней, левой) части рисунка или осей.

По желанию вы можете указать свойства стрелки, которые рисуют стрелку от текста до аннотируемой точки, передав словарь с свойствами стрелки. Допустимые ключи:

- `width`: ширина стрелки в точках
- `frac`: доля длины стрелки, занимаемая головой
- `headwidth`: ширина основания головы стрелки в точках
- `shrink`: сдвинуть конец и основание на некоторый процент от аннотируемой точки и текста
- `любой ключ для matplotlib.patches.polygon` (например, facecolor)

```python
import matplotlib.pyplot as plt
import numpy as np

from matplotlib.patches import Ellipse
from matplotlib.text import OffsetFrom

# Создаем наш рисунок и данные, которые будем использовать для построения графика
fig, ax = plt.subplots(figsize=(4, 4))

t = np.arange(0.0, 5.0, 0.01)
s = np.cos(2*np.pi*t)

# Строим линию и добавляем несколько простых аннотаций
line, = ax.plot(t, s)
ax.annotate('figure pixels',
            xy=(10, 10), xycoords='figure pixels')
ax.annotate('figure points',
            xy=(107, 110), xycoords='figure points',
            fontsize=12)
ax.annotate('figure fraction',
            xy=(.025,.975), xycoords='figure fraction',
            horizontalalignment='left', verticalalignment='top',
            fontsize=20)

# Следующие примеры демонстрируют, как рисуются эти стрелки.

ax.annotate('point offset from data',
            xy=(3, 1), xycoords='data',
            xytext=(-10, 90), textcoords='offset points',
            arrowprops=dict(facecolor='black', shrink=0.05),
            horizontalalignment='center', verticalalignment='bottom')

ax.annotate('axes fraction',
            xy=(2, 1), xycoords='data',
            xytext=(0.36, 0.68), textcoords='axes fraction',
            arrowprops=dict(facecolor='black', shrink=0.05),
            horizontalalignment='right', verticalalignment='top')

# Также вы можете использовать отрицательные точки или пиксели, чтобы указать от (правой, верхней) стороны.
# Например, (-10, 10) - это 10 точек слева от правой стороны осей и 10
# точек выше нижней стороны

ax.annotate('pixel offset from axes fraction',
            xy=(1, 0), xycoords='axes fraction',
            xytext=(-20, 20), textcoords='offset pixels',
            horizontalalignment='right',
            verticalalignment='bottom')

ax.set(xlim=(-1, 5), ylim=(-3, 5))
```
