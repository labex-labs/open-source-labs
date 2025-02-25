# Добавляем горизонтальные и вертикальные линии

Теперь мы добавляем горизонтальные и вертикальные линии в каждый подграфик, используя цвета из цикла свойств.

```python
for icol in range(2):
    if icol == 0:
        lwx, lwy = thin, lwbase
    else:
        lwx, lwy = lwbase, thick
    for irow in range(2):
        for i, color in enumerate(colors):
            axs[irow, icol].axhline(i, color=color, lw=lwx)
            axs[irow, icol].axvline(i, color=color, lw=lwy)
```
