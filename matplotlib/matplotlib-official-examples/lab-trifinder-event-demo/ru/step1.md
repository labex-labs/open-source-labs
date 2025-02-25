# Создание объекта Triangulation

Во - первых, нам нужно создать объект Triangulation. Мы будем использовать класс `Triangulation` из `matplotlib.tri`. В этом примере мы создадим объект Triangulation с случайными данными.

```python
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.tri import Triangulation

# Generate random data
x = np.random.rand(10)
y = np.random.rand(10)
triang = Triangulation(x, y)
```
