# Импортируем библиотеки и генерируем данные

Сначала мы импортируем необходимые библиотеки и генерируем некоторые данные для построения графика.

```python
import matplotlib.pyplot as plt
import numpy as np

from matplotlib import patheffects

# Generate data
nx = 101
x = np.linspace(0.0, 1.0, nx)
y = 0.3*np.sin(x*8) + 0.4
```
