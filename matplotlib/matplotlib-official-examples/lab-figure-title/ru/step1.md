# Создайте график затухающей и не затухающей колебания

Во - первых, мы создадим фигуру с двумя подграфиками: один для затухающей колебания, а другой для не затухающей колебания. Мы будем использовать функцию `np.linspace()` для создания массива значений времени, а затем построить соответствующие значения амплитуды для каждого типа колебания с использованием функций `np.cos()` и `np.exp()`.

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.0, 5.0, 501)

fig, (ax1, ax2) = plt.subplots(1, 2, layout='constrained', sharey=True)
ax1.plot(x, np.cos(6*x) * np.exp(-x))
ax1.set_title('затухающая')
ax1.set_xlabel('время (с)')
ax1.set_ylabel('амплитуда')

ax2.plot(x, np.cos(6*x))
ax2.set_xlabel('время (с)')
ax2.set_title('не затухающая')

fig.suptitle('Различные типы колебаний', fontsize=16)

plt.show()
```
