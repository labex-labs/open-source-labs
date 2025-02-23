# Импортируем библиотеки и определяем изображение

В первом шаге мы импортируем необходимые библиотеки и определяем изображение, которое будет использоваться в примере. Изображение представляет собой комбинацию двух гауссовых функций.

```python
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.transforms as mtransforms

def get_image():
    delta = 0.25
    x = y = np.arange(-3.0, 3.0, delta)
    X, Y = np.meshgrid(x, y)
    Z1 = np.exp(-X**2 - Y**2)
    Z2 = np.exp(-(X - 1)**2 - (Y - 1)**2)
    Z = (Z1 - Z2)
    return Z
```
