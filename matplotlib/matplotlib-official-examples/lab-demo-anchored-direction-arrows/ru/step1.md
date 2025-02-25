# Импортируем необходимые библиотеки

Сначала нам нужно импортировать необходимые библиотеки, такие как Matplotlib, NumPy, менеджер шрифтов Matplotlib и AnchoredDirectionArrows из mpl_toolkits.axes_grid1. Мы будем использовать эти библиотеки для создания направленных стрелок с привязкой.

```python
import matplotlib.pyplot as plt
import numpy as np

import matplotlib.font_manager as fm
from mpl_toolkits.axes_grid1.anchored_artists import AnchoredDirectionArrows
```
