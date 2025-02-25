# Импортируем необходимые библиотеки и создаем данные

```python
import matplotlib.pyplot as plt
import numpy as np

# Create data
t = np.arange(0.0, 100.0, 0.1)
s = np.sin(0.1 * np.pi * t) * np.exp(-t * 0.01)
```

Сначала мы импортируем необходимые библиотеки, то есть Matplotlib и NumPy. Затем мы создаем данные для построения графика. В этом примере мы создаем numpy-массив "t" и вычисляем другой numpy-массив "s" с использованием t.
