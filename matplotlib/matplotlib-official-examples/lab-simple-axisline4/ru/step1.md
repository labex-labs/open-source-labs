# Импортируем необходимые модули

Первым шагом является импорт необходимых модулей для нашей диаграммы. Мы будем использовать `numpy` для генерации наших данных по осям x и y, `matplotlib.pyplot` для создания диаграммы и `mpl_toolkits.axes_grid1` для создания второй оси y.

```python
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.axes_grid1 import host_subplot
```
