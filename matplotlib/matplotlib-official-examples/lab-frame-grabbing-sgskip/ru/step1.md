# Импортируем необходимые библиотеки

Сначала нам нужно импортировать необходимые библиотеки для создания анимации. Мы будем использовать `numpy` для генерации случайных чисел, `matplotlib` для построения графиков и `FFMpegWriter` для записи кадров в файл.

```python
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.animation import FFMpegWriter
```
