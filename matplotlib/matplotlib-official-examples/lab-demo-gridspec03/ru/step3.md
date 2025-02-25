# Управление расстоянием вокруг и между вложенными графиками

В этом шаге мы будем использовать `GridSpec` для управления расстоянием вокруг и между вложенными графиками. Создадим фигуру с 2 сетками (`gridspec`), каждая из которых имеет 3 строки и 3 столбца. Укажем параметры `left`, `right`, `bottom`, `top`, `wspace` и `hspace` для управления расстоянием.

```python
fig = plt.figure()
gs1 = GridSpec(3, 3, left=0.05, right=0.48, wspace=0.05)
ax1 = fig.add_subplot(gs1[:-1, :])
ax2 = fig.add_subplot(gs1[-1, :-1])
ax3 = fig.add_subplot(gs1[-1, -1])

gs2 = GridSpec(3, 3, left=0.55, right=0.98, hspace=0.05)
ax4 = fig.add_subplot(gs2[:, :-1])
ax5 = fig.add_subplot(gs2[:-1, -1])
ax6 = fig.add_subplot(gs2[-1, -1])
```
