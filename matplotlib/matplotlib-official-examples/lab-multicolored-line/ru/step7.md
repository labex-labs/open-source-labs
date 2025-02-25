# Создаем подграфик

Создадим подграфик для отображения окрашенных отрезков прямой. Используем функцию `subplots` из `matplotlib.pyplot` для создания сетки подграфиков 2x1 и параметры `sharex` и `sharey`, чтобы поделить оси x и y между подграфиками.

```python
fig, axs = plt.subplots(2, 1, sharex=True, sharey=True)
line = axs[0].add_collection(lc)
fig.colorbar(line, ax=axs[0])
```
