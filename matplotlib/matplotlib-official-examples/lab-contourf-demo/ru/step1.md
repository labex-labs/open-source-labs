# Импортируем библиотеки и создаем данные

Сначала нам нужно импортировать необходимые библиотеки и создать некоторые данные для построения.

```python
import matplotlib.pyplot as plt
import numpy as np

# Create data
origin = 'lower'
delta = 0.025
x = y = np.arange(-3.0, 3.01, delta)
X, Y = np.meshgrid(x, y)
Z1 = np.exp(-X**2 - Y**2)
Z2 = np.exp(-(X - 1)**2 - (Y - 1)**2)
Z = (Z1 - Z2) * 2
```
