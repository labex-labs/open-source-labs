# Основное использование pcolormesh

Обычно мы задаем pcolormesh, определяя края четырехугольников и значения для каждого из них. Обратите внимание, что здесь _x_ и _y_ в каждой размерности имеют на один элемент больше, чем Z.

```python
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(19680801)
Z = np.random.rand(6, 10)
x = np.arange(-0.5, 10, 1)  # len = 11
y = np.arange(4.5, 11, 1)  # len = 7

fig, ax = plt.subplots()
ax.pcolormesh(x, y, Z)
```
