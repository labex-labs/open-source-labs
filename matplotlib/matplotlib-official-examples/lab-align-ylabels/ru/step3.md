# Автоматически выровнять метки по оси y

Третий шаг - автоматически выровнять метки по оси y с использованием метода `.Figure.align_ylabels`.

```python
fig, axs = plt.subplots(2, 2)
fig.subplots_adjust(left=0.2, wspace=0.6)
make_plot(axs)
fig.align_ylabels(axs[:, 1])
plt.show()
```
