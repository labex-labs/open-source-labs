# Настройка графика

Сначала нам нужно настроить график с двумя подграфиками. Мы будем использовать функцию `subplots`, чтобы создать сетку подграфиков размером 2x2, а затем определим координаты x и y двух точек.

```python
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

fig, axs = plt.subplots(2, 2)
x1, y1 = 0.3, 0.3
x2, y2 = 0.7, 0.7
```
