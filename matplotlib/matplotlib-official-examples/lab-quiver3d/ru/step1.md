# Импорт библиотек и настройка графика

Первым шагом является импорт необходимых библиотек и настройка графика. В этом примере мы будем использовать модуль `pyplot` Matplotlib и его трехмерный инструментарий для создания трехмерного графика.

```python
import matplotlib.pyplot as plt
import numpy as np

ax = plt.figure().add_subplot(projection='3d')
```
