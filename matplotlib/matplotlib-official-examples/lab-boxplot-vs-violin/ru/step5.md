# Добавить сеточные линии и метки

Мы добавим горизонтальные сеточные линии, установим метки по оси x и оси y для графиков.

```python
for ax in axs:
    ax.yaxis.grid(True)
    ax.set_xticks([y + 1 for y in range(len(all_data))], labels=['x1', 'x2', 'x3', 'x4'])
    ax.set_xlabel('Four separate samples')
    ax.set_ylabel('Observed values')
```
