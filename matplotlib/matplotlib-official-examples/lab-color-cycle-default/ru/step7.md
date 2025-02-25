# Настраиваем деления на оси y

Мы настраиваем деления на оси y для самых левых подграфиков.

```python
for irow in range(2):
    axs[irow, 0].yaxis.set_ticks(np.arange(0, 10, 2))
```
