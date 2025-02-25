# Импортировать библиотеки и создать фигуру

Первым шагом является импорт необходимых библиотек и создание фигуры. Мы используем модуль `matplotlib.pyplot` для создания фигуры и модуль `mpl_toolkits.axes_grid1` для создания места для метки оси y.

```python
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable
from mpl_toolkits.axes_grid1.axes_divider import make_axes_area_auto_adjustable

fig = plt.figure()
ax = fig.add_axes([0, 0, 1, 1])
```
