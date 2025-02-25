# Построение простой области между кривыми с использованием fill_betweenx

В этом шаге мы научимся использовать функцию `fill_betweenx` для создания простого графика. Мы заполним область между двумя кривыми.

```python
import matplotlib.pyplot as plt
import numpy as np

y = np.arange(0.0, 2, 0.01)
x1 = np.sin(2 * np.pi * y)
x2 = 1.2 * np.sin(4 * np.pi * y)

fig, ax = plt.subplots(figsize=(6, 6))

ax.fill_betweenx(y, x1, x2, color='green', alpha=0.5)
ax.plot(x1, y, color='blue')
ax.plot(x2, y, color='red')

plt.show()
```
