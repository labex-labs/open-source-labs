# Импортируем необходимые библиотеки и фиксируем случайное состояние

Сначала нам нужно импортировать необходимые библиотеки и зафиксировать случайное состояние для воспроизводимости результатов. Мы будем использовать `numpy` для генерации случайных данных, `matplotlib.pyplot` для создания визуализаций и `cm` из `matplotlib` для определения цветовых карточек.

```python
import matplotlib.pyplot as plt
import numpy as np
from numpy.random import randn

from matplotlib import cm

# Fixing random state for reproducibility
np.random.seed(19680801)
```
