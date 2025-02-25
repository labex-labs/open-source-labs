# Генерация вложенных графиков с использованием `GridSpec`

В этом шаге мы будем использовать `GridSpec` для генерации вложенных графиков. Создадим фигуру с 2 строками и 2 столбцами. Также укажем `width_ratios` и `height_ratios`, чтобы контролировать относительные размеры вложенных графиков.

```python
fig = plt.figure()
gs = GridSpec(2, 2, width_ratios=[1, 2], height_ratios=[4, 1])
ax1 = fig.add_subplot(gs[0])
ax2 = fig.add_subplot(gs[1])
ax3 = fig.add_subplot(gs[2])
ax4 = fig.add_subplot(gs[3])
```
