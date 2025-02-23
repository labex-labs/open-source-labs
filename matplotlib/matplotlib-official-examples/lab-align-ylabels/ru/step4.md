# Ручное выравнивание меток по оси y

Четвёртый шаг - ручное выравнивание меток по оси y с использованием метода `~.Axis.set_label_coords` объекта оси y.

```python
fig, axs = plt.subplots(2, 2)
fig.subplots_adjust(left=0.2, wspace=0.6)
make_plot(axs)

labex = -0.3  # координаты осей

for j in range(2):
    axs[j, 1].yaxis.set_label_coords(labex, 0.5)

plt.show()
```
