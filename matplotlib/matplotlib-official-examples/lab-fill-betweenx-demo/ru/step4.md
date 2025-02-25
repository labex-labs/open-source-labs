# Использование замаскированных массивов

В этом шаге мы научимся использовать замаскированные массивы для заполнения области между двумя горизонтальными кривыми.

```python
import matplotlib.pyplot as plt
import numpy as np

y = np.arange(0.0, 2, 0.01)
x1 = np.sin(2 * np.pi * y)
x2 = 1.2 * np.sin(4 * np.pi * y)
x2 = np.ma.masked_greater(x2, 1.0)

fig, ax = plt.subplots(figsize=(6, 6))

ax.plot(x1, y, color='black')
ax.plot(x2, y, color='black')

ax.fill_betweenx(y, x1, x2, where=x2 >= x1, facecolor='green', alpha=0.5)
ax.fill_betweenx(y, x1, x2, where=x2 <= x1, facecolor='red', alpha=0.5)

plt.show()
```
